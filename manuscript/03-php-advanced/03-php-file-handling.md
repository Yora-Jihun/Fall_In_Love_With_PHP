# Chapter 29: PHP File Handling

### The Recipe Notebook

---

## Back in the Kitchen

Everything so far has lived and died within a single page load. The moment the script finishes, every variable disappears. A real kitchen needs a notebook that survives after the cook goes home: today's sales log, a list of pending orders, a saved copy of the menu. That's what working with files on disk gives you.

## The Concept

PHP can read from and write to files stored on the server's disk, using a small family of functions built around a shared idea: **open the file, do something with it, then close it.**

- **`fopen($path, $mode)`** opens a file and returns a "handle," a reference PHP uses for all further operations on that file. The `$mode` tells PHP what you intend to do: `"r"` for reading, `"w"` for writing (erasing existing content first), `"a"` for appending (adding to the end without erasing), among others.
- **`fclose($handle)`** closes the file, releasing it back to the system. Skipping this is a genuinely common mistake with real consequences, covered below.
- **`file_exists($path)`** checks whether a file exists at all, before you try to do anything with it.
- **`is_readable($path)`** and **`is_writable($path)`** check whether your script actually has permission to read or write that specific file.

PHP also offers a simpler pair of functions for the extremely common case of handling a whole file at once, rather than manually opening, reading piece by piece, and closing: `file_get_contents()` and `file_put_contents()`. These get their own full treatment in the next two chapters, but it's worth knowing now that they exist, since they cover a large share of everyday file work with far less code than the `fopen()` family.

## In the Code Kitchen

Create a new file named `file-handling.php` in your `kitchen` folder, and open it at `http://kitchen.test/file-handling.php`. Type each example below into that file, one at a time, and save it (Ctrl+S, or Cmd+S on a Mac) before you refresh the page. The examples work with a text file named `order-log.txt` in the same folder. You don't need to make it yourself. The second example creates it the first time it runs.

```php
<?php

$logFile = __DIR__ . "/order-log.txt";

if (file_exists($logFile)) {
    echo "The log file exists.";
} else {
    echo "No log file yet.";
}

if (is_writable(__DIR__)) {
    echo "This folder can be written to.";
}
```

Here's the full open, use, close pattern, using `fopen()` directly:

```php
<?php

$handle = fopen(__DIR__ . "/order-log.txt", "a"); // "a" = append mode

if ($handle) {
    fwrite($handle, "Order placed at " . date("Y-m-d H:i:s") . "\n");
    fclose($handle);
} else {
    echo "Could not open the log file.";
}
```

Notice the `if ($handle)` check. `fopen()` returns `false` if it fails, perhaps because the folder doesn't have write permission, or the disk is full, or the path is wrong. Assuming it always succeeds is exactly the kind of untrusted assumption this book has warned against since the very first chapter about superglobals, applied here to the filesystem instead of user input.

## Kitchen Notes (Best Practices)

- **Always close a file handle when you're done with it.** Leaving files open unnecessarily can lock resources, and on a busy server handling many requests, this adds up into real, hard-to-diagnose problems.
- **Always check whether `fopen()` actually succeeded before trying to use its result.** A failed `fopen()` doesn't throw an error by default. It quietly returns `false`, and using `false` as if it were a valid file handle causes a separate, more confusing failure.
- **Never build a file path directly from user input without validating it first.** A path like `__DIR__ . "/" . $_GET["file"]` could be manipulated by a visitor to reach files far outside the folder you intended, a real and well-known vulnerability called path traversal. This becomes especially important once uploads are involved, in a couple of chapters.

## Yoras' Mistake

Yoras writes to a log file without checking whether `fopen()` succeeded:

```php
<?php

$handle = fopen(__DIR__ . "/logs/order-log.txt", "a"); // "logs" folder doesn't exist yet
fwrite($handle, "New order.\n"); // fails silently, with a warning
fclose($handle);
```

The `logs` folder was never created, so `fopen()` fails and returns `false`. `fwrite($handle, ...)` then tries to write using `false` as if it were a real file handle, which produces its own separate warning, and no log entry is ever actually written. Nothing crashes outright, but nothing works either, and the failure is easy to miss entirely if warnings aren't being displayed.

**Lesson:** always check `fopen()`'s return value before using it, and make sure any folder your file lives in actually exists first, either by creating it ahead of time or checking for it with `is_dir()` and creating it with `mkdir()` if needed.

## Take-Home Practice

1. Check whether a file called `notes.txt` exists in your current folder using `file_exists()`, printing a different message depending on the result.
2. Open a file in append mode, write one line of text to it, and close it properly.
3. Deliberately try to open a file inside a folder that doesn't exist, and observe what `fopen()` returns.

## Recap

- Working with files follows a consistent pattern: open, do something, close.
- `fopen()` returns a file handle, or `false` on failure, which should always be checked.
- `file_exists()`, `is_readable()`, and `is_writable()` let you check before you act, rather than assuming.
- Never build a file path directly from unvalidated user input, to avoid the path traversal vulnerability.

Next chapter: a closer look at actually opening and reading a file's contents.
