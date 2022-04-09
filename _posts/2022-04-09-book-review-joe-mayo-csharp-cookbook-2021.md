---
layout: post
title: "Book Review: Joe Mayo - C# Cookbook. Modern Recipes for Professional Developers [2021]"
description: "Brief review of a book: Joe Mayo - C# Cookbook. Modern Recipes for Professional Developers [2021]. Score: 6.5 / 10"
tags: ["book", "review", "c#", "o'reilly", "fail"]
---

![Book Cover: Joe Mayo - C# Cookbook. Modern Recipes for Professional Developers [2021]](/content/binary/img/books/mayo-csharp-cookbook-2021.jpg)

Recently I've read and re-read a couple more books on C#, and one of them was this one.

It contains 90 recipes (9 chapters with 10 recipes each) for C# developers to consider upon various practical circumstances.

I generally like this kind of books since each recipe is generally located in one place thus you do not have to jump between chapters to grasp some idea, and it's great when you know what you're looking for :+1:.

**Personal Evaluation: 6.5 / 10**

Why not the highest mark? Because I've yet again found some inconsistencies :man_facepalming:.

---

#### :sparkles: 1. Naming

Even though I like the conciseness of each recipe, I do not like some of the author's naming conventions in code that look unnatural and weird.

For example, in recipe **"6.10 Disposing of Async Resources"** we have:

```csharp
public void Dispose()
{
    Dispose(disposing: true);
    ...
}

public async ValueTask DisposeAsync()
{
    ...
    Dispose(disposing: false);
    ...
}

protected virtual void Dispose(bool disposing) { ... }
```

But essentially, each call to `Dispose(bool disposing)` method occurs within the disposal execution path: either synchronous or asynchronous, so why on Earth does the parameter has the name `disposing`?

It looks like the author just copy-pasted the code from the example of resource disposal with finalizers and didn't bother to pay attention to properly adapting it for the new example.




---

#### :sparkles: 2. Another curious code waits for the reader in recipe **"7.1 Generating Password Hashes"**:

```csharp

static byte[] GenerateSalt()
{
    const int SaltLength = 64;
    byte[] salt = new byte[SaltLength];
    var rngRand = new RNGCryptoServiceProvider();
    
    rngRand.GetBytes(salt);
    return salt;
}

// The next two methods use that salt to generate hashes:

static byte[] GenerateMD5Hash(string password, byte[] salt)
{
    byte[] passwordBytes = Encoding.UTF8.GetBytes(password);
    byte[] saltedPassword = new byte[salt.Length + passwordBytes.Length];

    using var hash = new MD5CryptoServiceProvider();
    return hash.ComputeHash(saltedPassword);
}

static byte[] GenerateSha256Hash(string password, byte[] salt)
{
    byte[] passwordBytes = Encoding.UTF8.GetBytes(password);
    byte[] saltedPassword = new byte[salt.Length + passwordBytes.Length];
    
    using var hash = new SHA256CryptoServiceProvider();
    return hash.ComputeHash(saltedPassword);
}

// And here’s how to use the methods to generate hashes:

static void Main(string[] args)
{
    Console.WriteLine("\nPassword Hash Demo\n");
    Console.Write("What is your password? ");
    string password = Console.ReadLine();

    byte[] salt = GenerateSalt();
    byte[] md5Hash = GenerateMD5Hash(password, salt);

    string md5HashString = Convert.ToBase64String(md5Hash);
    Console.WriteLine($"\nMD5:    {md5HashString}");
    
    byte[] sha256Hash = GenerateSha256Hash(password, salt);
    string sha256HashString = Convert.ToBase64String(sha256Hash);
    
    Console.WriteLine($"\nSHA256: {sha256HashString}");
}

```

What's wrong about it? Well, it contains the methods to compute the salted password hashes, but those methods do not use the salt. And they neither use the passwords :worried:. In the code the array full of default values (zero bytes) is being hashed.

Me personally miss something semantically similar to the following lines in those methods:

```csharp
Array.Copy(salt, saltedPassword, salt.Length);
Array.Copy(passwordBytes, 0, saltedPassword, salt.Length, passwordBytes.Length);
```

So that the example would become really useful:

```csharp

static byte[] GenerateSha256Hash(string password, byte[] salt)
{
    byte[] passwordBytes = Encoding.UTF8.GetBytes(password);
    byte[] saltedPassword = new byte[salt.Length + passwordBytes.Length];

    Array.Copy(salt, saltedPassword, salt.Length);
    Array.Copy(passwordBytes, 0, saltedPassword, salt.Length, passwordBytes.Length);

    using var hash = new SHA256CryptoServiceProvider();
    return hash.ComputeHash(saltedPassword);
}

```

---

#### :sparkles: 3. Brilliant discovery awaits the reader in recipe **"6.8 Handling Parallel Tasks as They Complete"**:

<br>

> In addition to Task.WhenAll, you can use Task.WhenAny. It might be natural to think that Task.WhenAny is a good way to run multiple tasks in parallel and then be able to process each task while the others are running. However, Task.WhenAny doesn’t work the way you think it does. Look at **StartBigONSquaredAsync** and follow the following logic:
>
> 1. The while loop iterates as long as checkoutTasks still has contents.
> 2. Task.WhenAny starts all of the tasks in parallel.
> 3. The fastest task returns.
> 4. Since that task returned, remove it from checkoutTasks so we don’t run it again.
> 5. Collect the results from that task.
> 6. Do the loop again on the remaining tasks or stop when checkoutTasks is empty.
> 
> The first surprising mental hurdle in this algorithm is incorrectly thinking that subsequent loops operate on the same tasks, each returning as they complete. The reality is that each subsequent loop starts a brand-new set of tasks. This is how async works - **you can await a task multiple times, but each await starts a new task. That means the code continuously starts new instances of remaining tasks on every loop.** This looping pattern, with Task.WhenAny, doesn’t result in the O(1) performance you might have expected, like with Task.WhenAll, but rather O(N<sup>2</sup>). This solution only has three tasks, but imagine how performance would increasingly suffer as the task list grows.

<br>

Unfortunately, this is **NOT** the general rule of thumb about the Tasks in C#: the computations abstracted with the `Task` / `Task<T>` are **NOT** restarted / re-evaluated on each and every await in all possible circumstances. 

Perhaps, the author was able to mix and but not that lucky to match the concepts of Tasks in C# with asynchronous computations from F# which are "cold" computations and thus are re-evaluated on each request for the result :man_shrugging:.

I've added minor changes to the author's code for illustration purposes: added console logging calls.

<details>
<summary>
  <strong>:writing_hand: Slightly Tweaked Code</strong>
</summary>
{% highlight csharp %}
class Program
{
  static async Task Main()
  {
    try
    {
      var checkoutSvc = new CheckoutService();

      //string result = await checkoutSvc.StartBigO1Async();
      //string result = await checkoutSvc.StartBigONAsync();
      string result = await checkoutSvc.StartBigONSquaredAsync();

      Console.WriteLine($"Result: {result}");
    }
    catch (AggregateException aEx)
    {
      foreach (var ex in aEx.InnerExceptions)
        Console.WriteLine($"Unable to complete: {ex}");
    }
  }
}

public class CheckoutService
{  
  class AllTasksResult
  {
    public bool IsValidAddress { get; set; }
    public bool IsValidCredit { get; set; }
    public bool HasShoppingCart { get; set; }
  }

  public async Task<string> StartBigONAsync()
  {
    (_, bool addressResult) = await ValidateAddressAsync();
    (_, bool creditResult) = await ValidateCreditAsync();
    (_, bool cartResult) = await GetShoppingCartAsync();

    await FinalizeCheckoutAsync(
      new AllTasksResult
      {
        IsValidAddress = addressResult,
        IsValidCredit = creditResult,
        HasShoppingCart = cartResult
      });

    return "Checkout Complete";
  }

  public async Task<string> StartBigO1Async()
  {
    var checkoutTasks =
      new List<Task<(string, bool)>>
      {
        ValidateAddressAsync(),
        ValidateCreditAsync(),
        GetShoppingCartAsync()
      };

    Task<(string method, bool result)[]> allTasks =
      Task.WhenAll(checkoutTasks);

    if (allTasks.IsCompletedSuccessfully)
    {
      AllTasksResult allResult = GetResults(allTasks);

      await FinalizeCheckoutAsync(allResult);

      return "Checkout Complete";
    }
    else
    {
    throw allTasks.Exception;
  }
}

public async Task<string> StartBigONSquaredAsync()
{
  var checkoutTasks =
    new List<Task<(string, bool)>>
    {
        ValidateAddressAsync(),
        ValidateCreditAsync(),
        GetShoppingCartAsync()
    };

  var allResult = new AllTasksResult();

  while (checkoutTasks.Any())
  {
    Task<(string, bool)> task = await Task.WhenAny(checkoutTasks);
    checkoutTasks.Remove(task);

    GetResult(task, allResult);
  }

  await FinalizeCheckoutAsync(allResult);

  return "Checkout Complete";
}

void GetResult(
  Task<(string method, bool result)> task,
  AllTasksResult allResult)
{
  (string method, bool result) = task.Result;

  switch (task.Result.method)
  {
    case nameof(ValidateAddressAsync):
      allResult.IsValidAddress = result;
      break;
    case nameof(ValidateCreditAsync):
      allResult.IsValidCredit = result;
      break;
    case nameof(GetShoppingCartAsync):
      allResult.HasShoppingCart = result;
      break;
  }
}

AllTasksResult GetResults(
  Task<(string method, bool result)[]> allTasks)
{
  var allResult = new AllTasksResult();

  foreach (var (method, result) in allTasks.Result)
    switch (method)
    {
      case nameof(ValidateAddressAsync):
        allResult.IsValidAddress = result;
        break;
      case nameof(ValidateCreditAsync):
        allResult.IsValidCredit = result;
        break;
      case nameof(GetShoppingCartAsync):
        allResult.HasShoppingCart = result;
        break;
    }

  return allResult;
}

async Task<(string method, bool result)> ValidateAddressAsync()
{
  Console.WriteLine($"{nameof(ValidateAddressAsync)} started");

  return await Task.FromResult(
    (nameof(ValidateAddressAsync), true));
}

async Task<(string method, bool result)> ValidateCreditAsync()
{
  Console.WriteLine($"{nameof(ValidateCreditAsync)} started");
  
  var checkoutTasks =
    new List<Task<(string, bool)>>
    {
        CheckInternalCreditAsync(),
        CheckAgency1CreditAsync(),
        CheckAgency2CreditAsync()
    };

  Task<(string, bool)> task = await Task.WhenAny(checkoutTasks);

  (_, bool result) = task.Result;

  return await Task.FromResult(
    (nameof(ValidateCreditAsync), result));
}

async Task<(string, bool)> CheckInternalCreditAsync()
{
  return await Task.FromResult(
    (nameof(CheckInternalCreditAsync), true));
}

async Task<(string, bool)> CheckAgency1CreditAsync()
{
  return await Task.FromResult(
    (nameof(CheckAgency1CreditAsync), true));
}

async Task<(string, bool)> CheckAgency2CreditAsync()
{
  return await Task.FromResult(
    (nameof(CheckAgency2CreditAsync), true));
}

async Task<(string method, bool result)> GetShoppingCartAsync()
{
  Console.WriteLine($"{nameof(GetShoppingCartAsync)} started");
  
  return await Task.FromResult(
    (nameof(GetShoppingCartAsync), true));
}

async Task<bool> FinalizeCheckoutAsync(AllTasksResult allResult)
{
  Console.WriteLine(
    $"{nameof(AllTasksResult.IsValidAddress)}: " +
    $"{allResult.IsValidAddress}");
  Console.WriteLine(
    $"{nameof(AllTasksResult.IsValidCredit)}: " +
    $"{allResult.IsValidCredit}");
  Console.WriteLine(
    $"{nameof(AllTasksResult.HasShoppingCart)}: " +
    $"{allResult.HasShoppingCart}");

  bool success = true;
  return await Task.FromResult(success);
}
}

/*
Output example:

ValidateAddressAsync started
ValidateCreditAsync started
GetShoppingCartAsync started
IsValidAddress: True
IsValidCredit: True
HasShoppingCart: True
Result: Checkout Complete
*/
{% endhighlight %}
</details>

<br>

If the author was right then given a collection of 3 Tasks the method should run from scratch:

- all 3 of them on first iteration
- 2 of them on second iteration
- last 1 of them on third iteration

Thus, the expected and claimed by the author output should contain 6
(3 + 2 + 1 = 6) calls to log with "start messages".

And that's **not** what we observe :confused:. We actually find only 3 calls for starting the Tasks computations. Doesn't anyone wonder why :thinking:?

---

**O'Reilly Media, how could you?! :man_shrugging::crying_cat_face::man_facepalming:**

---
P.S. The book concerns list is not exhaustive.
