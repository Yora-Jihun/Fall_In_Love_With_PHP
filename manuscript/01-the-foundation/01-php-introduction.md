# Chapter 1: PHP Introduction

### Why PHP, Though?

---

## Day One

You show up at Chef Jirrum's Kitchen ten minutes early. You'll learn that this is already ten minutes late by kitchen standards. Chef Jirrum is at the counter, wiping down a surface that doesn't look dirty, and doesn't look up right away.

"Cook," he says, which is apparently your name now, "why are you here?"

You mumble something about wanting to learn to cook.

"Wrong answer," he says. "Wanting to cook, and wanting the dish, are two different things. Anyone can want a plate of adobo, that's chicken or pork, slow-braised in vinegar, soy sauce, and garlic. Not everyone wants to stand at a hot stove for forty minutes getting the vinegar-to-soy ratio exactly right."

He tosses you an apron. It's a little too big.

"It's the same with code," he says. "Plenty of people want to make a website. Very few actually want to learn how it's cooked. That's why we're here. So let's start with the one question you should be able to answer before you write a single line. What, exactly, is this PHP thing?"

## The Concept

**PHP** stands for **"PHP: Hypertext Preprocessor."** Yes, the acronym includes itself. That's exactly the kind of joke a language written by programmers would make about its own name. It started life in 1994 under a much plainer name, "Personal Home Page Tools," built by a developer named Rasmus Lerdorf to track visits to his own online résumé. It was never designed in a lab as a grand, sweeping language. It grew, tool by tool, out of a real, small problem. That origin story matters, because it explains PHP's whole personality: practical first, elegant second.

Today PHP is a general-purpose scripting language that is especially good at one specific job. It generates what a web browser shows you, by running code on the server before anything reaches the browser at all. That's what "server-side" means, and it's the single most important idea in this chapter.

Picture it this way. When you visit a website, you (the browser) are a customer sitting at a table. You never see the kitchen. You only see the plate that arrives. PHP is what happens *in the kitchen*. The code runs on a server somewhere, pulls together whatever it needs (text, data, a customer's name, today's specials), and sends out a finished plate: usually a page of plain HTML that your browser then displays. The customer never has to know or care what recipe was used back there. They just see the finished dish.

This is different from something like JavaScript running in a browser, which is more like a customer seasoning their own food at the table after it's already been served. Both matter. This book is about what happens in the kitchen.

A few honestly useful facts, worth knowing before you write a single line:

- PHP has gone through several major eras. PHP 4 and PHP 5 shaped the language for most of the 2000s and 2010s. PHP 7 (2015) brought a major performance rework. PHP 8 (2020 onward) added modern features like union types, the `match` expression, named arguments, and a JIT compiler. This book teaches modern PHP 8.x throughout. There's no reason to learn the old way first and unlearn it later.
- PHP is under active, ongoing development. New minor versions ship regularly, and the language keeps evolving, so "the current version" is a moving target by design. What matters for you as a learner is the shape of the language, which has been stable for years. This book's syntax and habits will still be correct long after the exact version number on php.net has changed again.
- Despite plenty of "PHP is dead" jokes over the years, it quietly still runs a large majority of the websites on the internet that use any server-side language at all, including huge, well-known platforms. It's also the foundation under popular tools like WordPress and frameworks like Laravel and Symfony. Understanding PHP is not a niche skill. It's closer to knowing how to cook rice. Unglamorous, and everywhere.

Chef Jirrum's take: "You don't need to know every recipe from every era to be a good cook today. You just need to know the correct way to do it. The way we do it now."

## In the Code Kitchen

Every dish needs a first attempt, even a small one. Let's cook the smallest possible thing PHP can make: proof that the kitchen is open.

Create a file named `hello.php` and type exactly this:

```php
<?php

echo "Welcome, Cook. The kitchen is open.";
```

Two things are happening here, and both matter more than they look:

1. **`<?php`** is the opening tag. It's how you tell the server, "everything from here is PHP, not plain text." Without it, the server would just serve your code as-is, the way it would serve a `.txt` file. No cooking happens.
2. **`echo`** hands something to the browser to display. We'll spend a full chapter on `echo` later. For now, just know it's the line that says "plate this and send it out."

Notice there's no closing `?>` tag at the end of the file. That's not a typo. It's the professional habit, and you're learning it from line one instead of correcting it later. When a file contains *only* PHP, the closing tag is left out on purpose, because any stray space or blank line after `?>` can accidentally leak into what gets sent to the browser. Think of it as a phantom crumb on a plate that's supposed to be spotless.

One more thing that trips up almost every new cook. **You can't just double-click `hello.php` and see it work.** Opening it directly in a browser (a `file://` address) shows you the raw code, or nothing useful at all, because there's no PHP processor involved. There's no kitchen, just the recipe card. PHP files have to be requested *through* a server that knows how to run PHP. That's exactly what the next chapter sets up on your own machine.

## Kitchen Notes (Best Practices)

- **Don't use the short `<?` tag.** Some very old PHP code uses a shortened opening tag. It depends on a server setting that isn't guaranteed to be on, so it can quietly break on someone else's setup. Always write the full `<?php`.
- **Drop the closing `?>` in pure-PHP files.** As shown above, this is a small habit that prevents a real, recurring bug (accidental output), rather than just a stylistic preference.
- **Get comfortable with the official manual early.** The PHP manual at php.net is the one source that's always current and authoritative, especially when a book, a blog post, or an old forum answer disagrees with what you're seeing on your machine. Treat this book as the kitchen lesson and the manual as the pantry label. Check the label when in doubt.

## Yoras' Mistake

Yoras saves his very first file as `hello.php.txt`, because his text editor added an extra extension without telling him. He opens it in the browser and just sees the raw `<?php echo ...` text staring back at him.

"Is this broken?" he asks, already sure the whole language is broken on day one.

It isn't broken. The server looked at the file, saw it wasn't actually a `.php` file underneath that extra `.txt`, and had no reason to cook it. It just handed it over raw, the way a kitchen would hand you an uncooked recipe card if you asked for the card instead of the dish.

**Lesson:** always confirm your file actually ends in `.php`, with your editor set to show full file extensions. If a PHP file ever shows up as raw code in the browser instead of running, that's the first thing to check.

## Take-Home Practice

You don't have a local server running yet. That's next chapter. So cook these with pen, paper, and curiosity:

1. In your own words, explain "server-side" to a friend who has never coded, using a food or restaurant comparison that isn't the one from this chapter.
2. Name three websites or apps you use regularly. Do a quick search on whether any of them are known to run on PHP, WordPress, or a PHP-based framework. You may be surprised how many are.
3. Without running any code, predict what would happen if you saved a file as `hello.php` but forgot the `<?php` opening tag entirely, and it was requested through a proper PHP server. Write down your guess, then check it once your practice kitchen (local server) is running in the next chapter.

## Recap

- PHP stands for "PHP: Hypertext Preprocessor" and started in 1994 as a small personal tool before growing into a major web language.
- PHP is **server-side**. It runs on the server and produces output (usually HTML) before anything reaches the browser. It's the kitchen, not the dining table.
- Modern PHP means PHP 8.x. This book teaches the current, professional way of writing PHP from the start.
- A PHP file needs the `<?php` opening tag, is typically run without a closing `?>` tag, and must be requested through a server that can execute PHP, not opened directly as a file.
- PHP remains one of the most widely used server-side languages on the web, powering huge platforms and popular tools like WordPress, Laravel, and Symfony.

Next chapter: setting up your own practice kitchen, so `hello.php` finally gets to run.
