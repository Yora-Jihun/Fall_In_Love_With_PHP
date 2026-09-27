# Chapter 1: PHP Introduction

### Why PHP, Though?

---

## Day One

You came to Chef Jirrum's Kitchen to learn how to code. So you expected a classroom. Instead, you find pots on the stove, knives on the wall, and the smell of garlic frying in oil.

"Wait," you say. "I think I'm in the wrong place."

"You're in the right place," says Chef Jirrum. He's at the counter, wiping down a surface that doesn't look dirty. "You came to learn to code, and you will. You'll just learn it the way a cook learns a kitchen."

He finally looks up. "Cook," he says. I guess that's your name now. "Why are you here?"

You say, a little quietly, that you want to build websites.

"Wrong answer," he says. "Wanting to build something and wanting the finished thing are not the same. Take adobo. Everyone loves a plate of it. You pick chicken or pork, just one. You fry it in a bit of oil with garlic and onion. Then you let it cook slowly in soy sauce, vinegar, and water, with bay leaves and black peppercorns. Some cooks add a little sugar to make it sweet. Some add red or green chili to make it spicy. Some add potatoes. Some add all three. Everyone wants to eat it. Not everyone wants to stand at a hot stove for forty minutes getting the vinegar and soy sauce just right."

He tosses you an apron. It's a little too big.

"Code works the same way," he says. "A dish is built from ingredients and techniques. A program is built from the basics, things like variables, conditions, loops, and functions. Learn them well, and one day you'll write your own recipes. Skip them, and every dish is a guess."

"In this kitchen, you're the chef of your own work. My job is to hand you the ingredients and help you cook your way through real problems. So let's start with the one question you should be able to answer before you write a single line. What, exactly, is this PHP thing?"

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

First, you need a place to write code. This book uses **VS Code** (Visual Studio Code). It's a free code editor for Windows, macOS, and Linux, and it's one of the most popular editors for PHP. You can download it from code.visualstudio.com. Other editors work too, like PhpStorm or Sublime Text. But every example in this book is shown in VS Code.

Open VS Code, create a new file named `hello.php`, and type exactly this:

```php
<?php

echo "Welcome, Cook. The kitchen is open.";
```

Two things are happening here, and both matter more than they look:

1. **`<?php`** is the opening tag. It's how you tell the server, "everything from here is PHP, not plain text." Without it, the server would just serve your code as-is, the way it would serve a `.txt` file. No cooking happens.
2. **`echo`** hands something to the browser to display. We'll spend a full chapter on `echo` later. For now, just know it's the line that says "plate this and send it out."

Notice there's no closing `?>` tag at the end of the file. That's not a mistake. Good PHP developers leave it out, and it's easier to learn the habit now than to fix it later.

Here's why. When a file has *only* PHP in it, anything after `?>` gets sent to the browser too. Even an extra space or an empty line you didn't notice. It's like a small crumb left on a clean plate. You didn't mean to put it there, but the customer still gets it. Leave out the `?>`, and there's nothing extra to send.

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
- This book uses VS Code as its code editor. Other editors, like PhpStorm or Sublime Text, work too.
- A PHP file needs the `<?php` opening tag, is typically run without a closing `?>` tag, and must be requested through a server that can execute PHP, not opened directly as a file.
- PHP remains one of the most widely used server-side languages on the web, powering huge platforms and popular tools like WordPress, Laravel, and Symfony.

Next chapter: setting up your own practice kitchen, so `hello.php` finally gets to run.
