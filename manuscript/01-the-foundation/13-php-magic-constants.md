# Chapter 13: PHP Magic Constants

### The Kitchen's Own Handwriting

---

## Back in the Kitchen

Some labels in a kitchen aren't written by the cook. They're stamped automatically: a printed timestamp on a receipt, a station number burned into a tray, a barcode nobody typed by hand. PHP has a small set of constants exactly like this. You never define them yourself. PHP fills them in automatically, based on where they appear in your code.

## The Concept

These are called **magic constants**, and each one starts and ends with two underscores. Unlike the constants from the last chapter, their value isn't set by you, and it can be different depending on exactly where in your code you use them. The most useful ones to know starting out are:

- `__LINE__`: the current line number in the file.
- `__FILE__`: the full path to the current file.
- `__DIR__`: the full path to the folder containing the current file.
- `__FUNCTION__`: the name of the current function, used only inside a function.
- `__CLASS__`: the name of the current class, used only inside a class (a more advanced way of organizing code).

They're most often used for debugging and logging, situations where knowing exactly where a piece of code ran from is genuinely useful information.

## In the Code Kitchen

Create a new file named `magic-constants.php` in your `kitchen` folder, and open it at `http://kitchen.test/magic-constants.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

```php
<?php

echo "This is line: " . __LINE__;
echo "<br>";
echo "This file lives at: " . __FILE__;
echo "<br>";
echo "This folder is: " . __DIR__;
```

Inside a function, `__FUNCTION__` reports that function's own name, which is handy for quick debug messages without hardcoding the function's name as a string, something that would silently go stale if the function were ever renamed. (Functions get their own chapter later, in Chapter 18. For now, just know that a function is a named set of steps you can run by calling its name.)

```php
<?php

function calculateTotal() {
    echo "Running: " . __FUNCTION__;
}

calculateTotal(); // Running: calculateTotal
```

`__DIR__` is especially useful for reliably including other files, a topic covered fully in the Include chapter, since it always points to the current file's own folder, no matter what folder the script was originally run from:

```php
<?php

// Reliably points to a file in the same folder as this one,
// regardless of where the script was executed from.
$configPath = __DIR__ . "/config.php";
```

## Kitchen Notes (Best Practices)

- **Prefer `__DIR__` over typing out a relative path like `"../config.php"`** when including other files. Relative paths depend on where the script happened to be run from, which can change, while `__DIR__` never does.
- **Use `__FUNCTION__` and `__CLASS__` in debug or logging messages** instead of hardcoding the name as plain text, so the message stays accurate even if the function or class gets renamed later.
- **Don't overuse magic constants in regular business logic.** They're a debugging and file-path tool, not something that should shape how your application actually behaves.

## Yoras' Mistake

Yoras keeps his helper code in `includes/helpers.php`, which loads the kitchen's settings file like this:

```php
<?php

// includes/helpers.php
require "../config.php";
```

When he opens `helpers.php` directly, it works. But when his `index.php` page includes `helpers.php`, it suddenly fails with an error saying `config.php` can't be found.

The problem is how PHP reads a relative path like `"../config.php"`. It doesn't start from the file where that line is written. It starts from the folder of the main page that was opened, which here is `index.php`. From there, `..` goes up one level too many, and PHP ends up looking for `config.php` outside the project.

**Lesson:** anchor include and require paths to `__DIR__` instead of a relative path. `__DIR__` is always the folder of the file the line is written in, so the path stays correct no matter which page includes it:

```php
<?php

// includes/helpers.php
require __DIR__ . "/../config.php";
```

## Take-Home Practice

1. Print `__LINE__`, `__FILE__`, and `__DIR__` from a file of your own, and confirm the values make sense.
2. Write a small function that echoes its own name using `__FUNCTION__`, then call it.
3. Rewrite a relative include path (imagine one like `"../settings.php"`) using `__DIR__` instead.

## Recap

- Magic constants are built-in constants PHP fills in automatically, always written with double underscores on both sides.
- `__LINE__`, `__FILE__`, and `__DIR__` report information about the current location in your code.
- `__FUNCTION__` and `__CLASS__` report the name of the current function or class.
- `__DIR__` is the reliable way to build file paths that don't break when the project's folder structure changes.

Next chapter: operators, the actions a kitchen uses to combine, compare, and adjust.
