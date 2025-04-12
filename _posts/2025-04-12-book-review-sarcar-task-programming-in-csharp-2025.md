---
layout: post
title: "Book Review: Vaskaran Sarcar - Task Programming in C# and .NET: Modern Day Foundation for Asynchronous Programming [2025]"
description: "Vaskaran Sarcar - Task Programming in C# and .NET: Modern Day Foundation for Asynchronous Programming [2025]. Score: 4.5 / 10 - not worth the time and money"
tags: ["book", "review", "c#", "async", "task", "tpl", ".net", "apress", "fail"]
comments: false
---

![Book Cover: Vaskaran Sarcar - Task Programming in C# and .NET: Modern Day Foundation for Asynchronous Programming [2025]](/content/img/2025-04-12-book-review-sarcar-task-programming-in-csharp-2025/sarcar-task-prog-csharp-2025.webp)

This book caught my attention due to its freshness (released just around a month ago), light topic, and size (I expected to some condensed wisdom / recipes / good refreshers), so I decided to give it a try.

Long story short:

- The feeling of disappointment appeared at the beginning, and it did not leave me until the end of the book

- **Personal evaluation: (at most) 4.5 / 10 - not worth the time and money**

- **Will I recommend it to anyone? no**

- The book can (questionably) be useful only to junior-level engineers, but I would suggest them reading something else instead (even Marvel comic books or better official Microsoft docs on the subject are incomparably better than this book) 

- The material is quite shallow and misses important information (like that it really means to have a graph of Tasks attached to each other)

- The saddest part is that it has mistakes in elementary-level code that cause the readers to think that the author is incompetent (just like the tech reviewer)

  - e.g. Chapter 6: Bonus

    ![Book page 144](/content/img/2025-04-12-book-review-sarcar-task-programming-in-csharp-2025/example-1-1.webp)

    This wording makes sense. But this sense is lost in the upcoming elementary example:

    ![Book page 145](/content/img/2025-04-12-book-review-sarcar-task-programming-in-csharp-2025/example-1-2.webp)

    Here, the presense of the call `Task.FromResult(flagValue)` makes absolutely zero effect on the output of the `TimeConsumingMethod()` call: we can leave it, we can delete it, or we can change it to something like `Task.FromResult(-42)`: in either way it does not affect the outcome simply because its task is not returned from the method (making this caching wisdom useless) :man_facepalming:

- But the great mystery was revealed in Appendix B: the author prefers to publish a shallow book on a widely-known topic across C# and Java once (or better several times) per year, and heroically prefers quantity over quality

- As usual, anyone can publish a book on Apress without a good review process in place, as the publishing house is just interested in bumping up the number of published titles

:v:
