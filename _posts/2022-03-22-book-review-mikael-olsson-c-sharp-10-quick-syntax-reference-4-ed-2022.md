---
layout: post
title: "Book Review: Mikael Olsson - C# 10 Quick Syntax Reference. A Pocket Guide to the Language, APIs, and Library (4 ed)[2022]"
description: "Brief review of a book: Mikael Olsson - C# 10 Quick Syntax Reference. A Pocket Guide to the Language, APIs, and Library (4 ed)[2022]. Score: 5 / 10"
tags: ["book", "review", "c#", "apress", "fail"]
---

![Book Cover: Mikael Olsson - C# 10 Quick Syntax Reference. A Pocket Guide to the Language, APIs, and Library (4 ed)[2022]](/content/binary/img/books/olsson-csharp-10-quick-syntax-reference-2022.jpg)

Recently, I finally felt the strength to take a partial break from the constant ingestion of the current news feed in :ukraine: and decided to read this book to get more familiar with C# 10.

As the title implies the book should give a brief overview of the C# language features including the latest version C# 10.

The book is ~200 pages in total and it comprises of 31 chapters with short coverage of different topics. And it generally gets the job done.

**It may suit you if:**

- you're familiar with C# and software development in general

- you just want a quick recap on a few topics

**It won't suit you if:**

- you're a novice in the software engineering field

- you have no prior experience with C# because in my opinion it won't be sufficient to start with .NET development with this book only (for this read Albahari's book or browse the online documentation from Microsoft)

But that's absolutely not a problem since it's not the design goal of this book.

Even though I would like to see more topics covered I understand that the book would have been 1000+ pages long to meet my expectations in this thus I'm fine with what is given by the author.

**Personal Evaluation: 5 / 10**

Then why not 10 / 10? Because I found a couple of mistakes :man_facepalming:.

### Some of them are:

1) On **page 188** in subtopic **"Extended Return Types"** we have the following:

   > To give an example, the following PowTwo async method gives
the result of the argument raised to the second power (a<sup>2</sup>). It executes
synchronously if the argument is less than plus or minus ten, and therefore
returns a ValueTask<double> type in order to not have to allocate a Task
object in such a case. 

   ---

   **Details:**

   Well, the part `if the argument is less than plus or minus ten` is generally equivalent to `if the argument is less than ten`, but it does **not** meet the author's intent in code:

   ```csharp
if (a < 10 && a > -10) {
    return System.Math.Pow(a, 2);
}
   ```

<br>

2) On **page 154** in subtopic **"Expression Body Members"** we have the following:

   > Lambda expressions provide a shorthand alternative way to define class
members in cases when the member consists of only a single expression.
This is called an expression body definition. Consider the following class:

   ```csharp
class Person
{
    public string name { get; } = "John";
    public void PrintName() {
        System.Console.WriteLine(name);
    }
}
   ```

   > **These member bodies can be rewritten as expression bodies instead,
which are easier to read.**

   ```csharp
class Person
{
    public string name => "John";
    public void PrintName() =>
        System.Console.WriteLine(name);
}
   ```

   ---

   **Details:**

   Unfortunately, the latter code snippet can **NOT** be used as a syntax sugar replacement of a former one in general case because C#'s semantic is actually different:

   ```csharp
using System;
   
public class Person
{
    public Guid Id_A { get; } = Guid.NewGuid();

    public Guid Id_B => Guid.NewGuid();

    public static void Main()
    {
        var person = new Person();
        Console.WriteLine(person.Id_A);    // 0ec409eb-e7c0-42ee-810f-fa5d00b9e033
        Console.WriteLine(person.Id_A);    // 0ec409eb-e7c0-42ee-810f-fa5d00b9e033
        Console.WriteLine(person.Id_B);    // 9fa1282f-29e7-46a6-bcec-1f1625fd9056
        Console.WriteLine(person.Id_B);    // 18d2e0c2-ee06-49ce-a64a-0c1ba0837f0c
    }
}
   ```

   As we can see, `Id_B` **can't always** be used as a replacement for `Id_A`.

<br>

3) On **page 44** in subtopic **"Pass by Reference"** we have the following:

   > For reference data types, C# uses true pass by reference. This means that
when a reference type is passed, it is not only possible to change its state
but also to replace the entire object and have the change propagate back to
the original object.

   ```csharp
void Set(int[] i) { i = new int[] { 10 }; }

static void Main()
{
    MyApp m = new MyApp();
    int[] y = { 0 };            // reference type
    m.Set(y);                   // pass object reference
    System.Console.Write(y[0]); // 10
}
   ```

   ---

   **Details:**

   In order to see where the type `MyApp` comes from I'll explicitly add it to the author's code:

   ```csharp
public class MyApp
{
    void Set(int[] i) { i = new int[] { 10 }; }

    public static void Main()
    {
        MyApp m = new MyApp();
        int[] y = { 0 };            // reference type
        m.Set(y);                   // pass object reference
        System.Console.Write(y[0]); // 10
    }
}
   ```
 
   But the thing is that C# won't actually let you to redefine the value of the variable `y` this way, and what is actually would be printed is `0` (and **NOT** `10`). 
   
   **And it has been so since the early days of C# :man_shrugging:!**
   
   In order to get `10` we would have to use the `ref` parameter decorator.
  
---

The third one upsets me the most.

So, out of curiosity I took a look at previous editions of the book too:

Author | Title | Edition | Year | Mistake 1 Location (If Present) | Mistake 2 Location (If Present) | Mistake 3 Location (If Present) | Book Technical Reviewer
--- | --- | --- | --- | --- | --- | --- | ---
Mikael Olsson | C# Quick Syntax Reference | 1 | 2013 | N/A (no such topic since `ValueTask<T>` hasn't yet been introduced by Microsoft) | N/A | Page 27 | Michael Thomas
Mikael Olsson | C# 7 Quick Syntax Reference | 2 | 2018 | Pages 172-173 | Page 140 | Pages 43-44 | Michael Thomas
Mikael Olsson | C# 8 Quick Syntax Reference | 3 | 2020 | Pages 180-181 | Page 148 | Pages 43-44 | Michael Thomas
Mikael Olsson | C# 10 Quick Syntax Reference | 4 | 2022 | Pages 188-189 | Page 154 | Pages 43-44 | Doug Holland

---

And something tells me that this list might not be complete. :worried:

**Childish mistakes in basic topics of introductory level material. That's a shame :man_facepalming:. ~~Carved in stone.~~ Published in books. For years to come.**

I think the guys should have paid a bit more attention to voluntarily taken responsibilities and not just copy-pasting the initially error-prone content.

---

I guess we should somehow enforce this test in production:

```gherkin
Feature: Knowledge Retrieval v1
Given: the technical book from Apress / Springer is available in the bookstore
When I buy the book and read it
Then I should get valuable and correct source of information and knowledge
```
