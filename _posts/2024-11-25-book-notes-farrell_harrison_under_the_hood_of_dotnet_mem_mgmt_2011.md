---
layout: post
title: "Book Notes: Farrell, Harrison - Under the Hood of .NET Memory Management [2011]"
description: "Brief book notes: Farrell, Harrison - Under the Hood of .NET Memory Management [2011]"
tags: ["book", "notes", "c#", ".net", "memory", "memory management", "gc", "garbage collector"]
comments: false
---

![Book Cover: Farrell, Harrison - Under the Hood of .NET Memory Management [2011]](/content/img/books/farrell_harrison_under_the_hood_of_dotnet_mem_mgmt_2011.jpg)

*It's quite an old book, I've read it several times before and re-read it yet another time.*

## Garbage collection
### GC roots:

- global/static object references
- CPU registers
- object finalization references / finalization queue
- Interop references / unmanaged Interop objects (.NET objects passed to COM/API calls)
- stack references

If an object doesn't ultimately have a root reference then it can't actually be accessed by code, so it is no longer in use, and can be removed.

---

## Small Object Heap (SOH)

The GC runs automatically on a separate thread under one of the conditions below:

- When the size of objects in any generation reaches a generation-specific threshold. To be precise, when:

	- Gen 0 hits ~256 K
	- Gen 1 hits ~ 2 MB (at which point the GC collects Gen 1 and 0)
	- Gen 2 hits ~10 MB (at which point the GC collects Gen 2, 1 and 0)

- `GC.Collect()` is called in code

- the OS sends a low memory notification.

It's worth bearing in mind that the above thresholds are merely starting levels, because .NET modifies the levels depending on the application's behavior.

GC operation also depends on whether the application is server- or workstation-based, and on its latency mode.

---

### Gen 0 collection

Gen 0 objects have never been looked at by the GC before, so they have two possible options when they are finally inspected:

- move to Gen 1 (if they have a root reference in their hierarchy)
- die and be compacted (if they are rootless and therefore no longer in use)

Either way, the **result of a Gen 0 GC is an empty Gen 0 (!)**, with all rooted objects in Gen 0 being copied to (and reclassified as) Gen 1, joining the other Gen 1 objects.

### Gen 1 collection

Gen 1 collections collect both Gen 1 and Gen 0 objects.

### Gen 2 collection

Gen 2 collections are known as "Full" collections because all of the generations are inspected and collected. As a result, they cause the most work and are thus the most expensive.

Ideally, you only want objects to make it to Gen 2 if they absolutely need to be there. Gen 2 is an expensive place to keep your objects, and too frequent Gen 2 collections can really hit performance.

The general rule of thumb is that there should be ten times more Gen 0 collections than Gen 1, and ten times more Gen 1 collections than Gen 2.

---

## Finalization

If you put a destructor or a `Finalize` method (henceforth known as the finalizer) in your class (see Listing), then you will actually extend the lifetime of instances of your classes for longer than you expect.

```csharp
class TestClass
{
	~TestClass() {}
}
class TestClass2
{
	void Finalize()	{}
}
```

So (to not slow down the GC with calls to finalizers' logic) the guys at Microsoft took a different approach, and decided to call the finalizer on objects asynchronously and on a dedicated thread. This runs periodically and calls the finalizer on all applicable objects, entirely independently of the GC.

However, that creates a new puzzle: how do you prevent an object that needs finalization from being compacted before its finalizer is called? The answer they came up with was to keep a queue of extra root references to all finalizable objects (one reference per object) and use this to keep them alive long enough to call their finalizer.

When object Z with finalizer is created, as well as a root reference in one of the usual places (stack, statics, etc.), an additional reference is added onto the finalization queue, which then acts as a kind of reminder to .NET that it needs to call the finalizer on this object at some point.

When Object Z loses its root reference, it would usually become a candidate for collection but, because of the extra reference on the finalization queue, it's still viewed as "rooted", and isn't collected when the GC next runs.

After the GC run, the finalization reference is also moved from the finalization queue to another queue, called the `fReachable` queue. `fReachable` acts as a kind of reminder list of all the objects on the heap that still need to have their finalizer called. Think of it like this; the finalization queue keeps a reference to all of the live finalizable objects and `fReachable` references dead objects that need their finalizer calling.

Periodically, the finalization thread will run, and it will iterate through all objects pointed to by references in the `fReachable` queue, calling the Finalize method or destructor on each one and removing its reference from `fReachable`. Only then will the finalizable object be rootless and available for collection.

### Improving finalization efficiency

```csharp
public void Dispose()
{
	Cleanup(true);
	GC.SuppressFinalize(this);
}
```

Standard Dispose pattern you can add to your finalizable class. All you do is provide a standard `Cleanup` method that is responsible for cleaning up the class. It needs a Boolean parameter, which is used to determine if `Cleanup` was called from the finalizer or directly from code. This is important because the finalizer is called on a separate thread, so if you are doing any thread-specific cleanup, then you need to avoid doing it if it's the finalizer running it.

Finally, we add a `Dispose` method which calls the `Cleanup` method, passing true. Crucially, it also calls `GC.SuppressFinalize(this)`, which deletes the reference in the finalization queue and gets around the problem.

---

## Large Object Heap (LOH)

Objects larger than 85 KB are allocated onto the Large Object Heap (LOH). Unlike the SOH, objects on the LOH aren't compacted, because of the overhead of copying large chunks of memory. **When a full (Gen 2) GC takes place (!!!)**, the address ranges of any LOH objects not in use are recorded in a "free space" allocation table. If any adjacent objects are rootless, then they are recorded as one entry within a combined address range.

When a new object is allocated onto the LOH, the Free Space table is checked to see if there is an address range large enough to hold the object. If there is, then an object is allocated at the start byte position and the free space entry is amended.

If there isn't, then the object will be allocated at the next free space above.

If the chunks are <85 K, they will be left with no possibility of reuse, as objects of that size obviously never make it onto the LOH. The result is that, as allocation demand increases, new segments are reserved for the LOH, even though space, albeit fragmented space, is still available.

---

I can't finish this section on the LOH without giving you the full picture. You know I said that objects >85 KB are allocated onto the LOH? Well, that works for everything except for some internal arrays, such as arrays of type double with a size greater than 1,000 (the threshold is different for certain types).

Normally, you would probably expect that an array of doubles would only be allocated onto the LOH when it reached an array size of about 10,600. However, for performance reasons, doubles arrays of size 999 or less allocate onto the SOH, and arrays of 1,000 or above go onto the LOH.

---

### Special case: older genration object holds a reference to smaller generation object

#### The card table

A data structure called the card table is used to record when objects are created and referenced from older objects. It's specifically designed to maintain GC performance but still allow objects' references to be tracked regardless of their generation.

When Gen 0 or Gen 1 objects are created from within Gen 2 objects, the execution engine puts an entry in the card table. This check is made before any reference is created, to see if that reference is to a "previous generation" object, and is known as the "write barrier."

Instead, .NET stores a bit pattern, with one bit representing 128 bytes of heap memory. If an object residing within the address range of that bit has created a Gen 0 or Gen 1 object, then the bit is set.

After that, when a Gen 0 or Gen 1 collection takes place, any objects residing in the address range of a set bit in the card table are included in the "in use list" inspection, as are all of their child references.

:v:
