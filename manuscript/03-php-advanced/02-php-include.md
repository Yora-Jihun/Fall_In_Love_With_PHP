# Chapter 28: PHP Include

### Borrowing a Recipe Card

---

## Back in the Kitchen

The menu header, the footer with the restaurant's contact details, the navigation bar linking every page together. Copying that same block of HTML and PHP into every single page of a website is exactly the kind of repetition Chapter 18 warned about with functions. `include` and `require` solve the same problem for entire files.

## The Concept

Four keywords let one PHP file pull in the contents of another:

- **`include`**: inserts and runs the target file. If the file is missing, PHP raises a warning and *keeps running* the rest of the script.
- **`require`**: does the same thing, but if the file is missing, PHP raises a fatal error and *stops the script immediately*.
- **`include_once`** and **`require_once`**: behave identically to their counterparts, but PHP keeps track of which files have already been included, and silently skips including the same file twice.

The choice between `include` and `require` is really a question: **is the rest of the page still useful without this file?** A missing decorative promo banner is annoying, but the page can still function. A missing file containing your core configuration or database connection settings means nothing else should even attempt to run.

## In the Code Kitchen

This chapter uses more than one file, so create each one in your `kitchen` folder as you go. Save every file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page. An unsaved `header.php` is a header the other page can't see.

A shared header file, `header.php`:

```php
<?php
// header.php
?>
<header>
    <h1>Chef Jirrum's Kitchen</h1>
    <nav>
        <a href="/">Home</a> | <a href="/menu.php">Menu</a> | <a href="/contact.php">Contact</a>
    </nav>
</header>
```

Using it from another page, `menu.php`, anchored with `__DIR__` from Chapter 13 so the path stays correct no matter where the script runs from:

```php
<?php
require __DIR__ . "/header.php";
?>

<main>
    <p>Welcome to today's menu.</p>
</main>
```

Open `http://kitchen.test/menu.php`. The header from `header.php` shows up at the top, even though `menu.php` never wrote it out itself.

`include_once` and `require_once` matter most when a file might get pulled in from multiple places in one request. A shared file defining functions or constants is a common example. Including it twice would attempt to redefine those functions, causing a fatal error:

```php
<?php

require_once __DIR__ . "/functions.php"; // safe, even if another file already included it
```

To try this line, you need a `functions.php` file in the same folder. The Take-Home Practice below walks you through making one.

## Kitchen Notes (Best Practices)

- **Use `require` or `require_once` for anything essential**, like configuration, core function libraries, or database setup, since the rest of the page genuinely cannot work correctly without them.
- **Use `include` only for genuinely optional content**, where the page can reasonably continue if the file happens to be missing.
- **Default to the `_once` variants for anything defining functions, classes, or constants**, since including the same definitions twice causes a fatal "already declared" error.
- **Always build the path with `__DIR__`**, as shown above, rather than a relative path that depends on where the script happened to be run from.

## Yoras' Mistake

Yoras includes his database connection file using plain `include`:

```php
<?php

include __DIR__ . "/database-connection.php";

$results = $connection->query("SELECT * FROM menu");
```

One day, the file gets accidentally renamed during a cleanup, and `include` fails to find it. PHP raises a warning, and, critically, *keeps going*, trying to use `$connection` on the very next line, even though it was never actually set. This produces a second, more confusing fatal error, several lines away from the real problem.

**Lesson:** for anything the rest of the script truly depends on, use `require`, not `include`. A hard, immediate failure at the actual point of the problem is far easier to diagnose than a warning followed by a confusing, unrelated crash further down the page.

## Take-Home Practice

1. Create a `footer.php` file with a simple closing HTML block, and `include` it from two different pages.
2. Create a `functions.php` file defining one small function, and `require_once` it from a page that calls that function.
3. Deliberately misspell a filename in a `require` statement, run the script, and read the fatal error PHP produces.

## Recap

- `include` warns and continues if the target file is missing. `require` fails immediately and stops the script.
- `include_once` and `require_once` prevent the same file from being included, and its contents re-declared, more than once.
- Use `require` (or `require_once`) for anything the script genuinely can't function without.
- Anchor include and require paths with `__DIR__` so they don't break when the folder structure or execution context changes.

Next chapter: file handling, or writing to and reading from the kitchen's own recipe notebook.
