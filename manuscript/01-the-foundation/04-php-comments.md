# Chapter 4: PHP Comments

### Notes Taped to the Recipe Card

---

## Back in the Kitchen

Every good kitchen has recipe cards with handwritten notes in the margins. "Add less salt if using salted butter." "This step burns fast, watch it closely." Nobody reads that note out loud while cooking. It's there for whoever picks up the card next, including the same cook, six months later, who has completely forgotten why the recipe says what it says.

Code needs the same kind of margin note. In PHP, that's a comment.

## The Concept

A comment is a piece of text in your code that PHP completely ignores when it runs. It's there only for humans. PHP gives you three ways to write one:

- `//` starts a single-line comment. Everything after it, to the end of that line, is ignored.
- `#` also starts a single-line comment. It works identically to `//`, though `//` is far more common in practice and is what this book uses.
- `/*` and `*/` wrap a comment that can span multiple lines.

Comments are not for explaining what obvious code does. A comment like `// add one to total` above a line that says `$total = $total + 1;` teaches the reader nothing they couldn't already see. A useful comment explains something the code itself can't: why a value is what it is, why a workaround exists, or a warning about something non-obvious that will bite the next cook.

## In the Code Kitchen

Create a new file named `comments.php` in your `kitchen` folder, and open it at `http://kitchen.test/comments.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

```php
<?php

// This is the daily special. Update it each morning before opening.
$special = "Chicken Adobo";

echo $special; # This line works the same as above, using the # style instead.

/*
   The block below used to include a Tuesday-only combo deal.
   It was removed after the promo ended, but keeping the note
   here in case Chef Jirrum brings it back next quarter.
*/
```

Comments are also handy for temporarily turning off a line of code without deleting it, useful while you're testing something:

```php
<?php

$price = 150;
// $price = $price * 1.1; // tax calculation, disabled for now
echo $price;
```

## Kitchen Notes (Best Practices)

- **Write comments that explain *why*, not *what*.** The code already says what it does. A comment earns its place by explaining a reason, a constraint, or a warning that isn't visible just by reading the line.
- **Don't leave large blocks of old, commented-out code sitting around forever.** A recipe notebook full of crossed-out, half-legible old attempts is harder to read, not easier. If it's truly gone, delete it. Version control (a tool like Git, covered outside this book) remembers old code for you.
- **Update or delete comments when the code around them changes.** A comment that no longer matches what the code actually does is worse than no comment at all, since it actively misleads the next reader.

## Yoras' Mistake

Yoras writes a multi-line comment, but forgets the closing `*/`:

```php
<?php

/*
This explains the discount logic below.

$price = 100;
echo $price;
```

Every line after the opening `/*` silently disappears into the comment, including the actual code, because PHP is still waiting for `*/` to show up. Nothing runs, since as far as PHP is concerned, there's no code there at all to run. At most, PHP shows a small warning about an "unterminated comment," which is easy to miss.

**Lesson:** always close a multi-line comment. If a chunk of code seems to have vanished for no reason, check for an unclosed `/*` above it.

## Take-Home Practice

1. Take any PHP file you've written so far and add one genuinely useful comment to it, one that explains a *why*, not a *what*.
2. Practice commenting out a single line of working code using `//`, run the file, then uncomment it again.
3. Write a multi-line comment on purpose, then intentionally forget the closing `*/`, and observe what breaks.

## Recap

- `//` and `#` both start a single-line comment. This book uses `//`.
- `/* ... */` wraps a comment across multiple lines, and it must be closed.
- Good comments explain *why*, not *what*, since the code already shows *what*.
- An unclosed `/*` silently swallows every line of real code that follows it.

Next chapter: variables, the labeled containers every recipe depends on.
