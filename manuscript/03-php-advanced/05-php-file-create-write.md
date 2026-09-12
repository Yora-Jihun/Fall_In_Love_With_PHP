# Chapter 31: PHP File Create and Write

### Writing in the Notebook

---

## Back in the Kitchen

Reading the notebook is only half the job. Someone has to actually write in it first: today's sales total, a new log entry, an updated version of the menu. This chapter covers creating and writing files, the counterpart to the last chapter's reading.

## The Concept

Just like reading, PHP gives you a simple, one-line option and a more manual, flexible option:

- **`file_put_contents($path, $data)`** writes a string to a file in a single call. If the file doesn't exist yet, it's created. If it does exist, its previous content is completely replaced, unless you pass the `FILE_APPEND` flag, in which case the new data is added to the end instead.
- **`fopen()` with mode `"w"` or `"a"`, followed by `fwrite()`**, gives you more control, useful when you're writing in multiple steps rather than all at once.

The mode you choose with `fopen()` matters a great deal:

- `"w"` opens for writing, and immediately erases the file's existing content, even before you write anything new.
- `"a"` opens for appending, preserving existing content and adding new content to the end.
- `"x"` creates a new file for writing, but fails if the file already exists, useful when you specifically want to avoid overwriting something.

## In the Code Kitchen

**The simple, common case**

```php
<?php

$logLine = "Order placed at " . date("Y-m-d H:i:s") . "\n";

file_put_contents(__DIR__ . "/order-log.txt", $logLine, FILE_APPEND);
```

Without `FILE_APPEND`, that same call would erase the entire log file and replace it with just this one line, which is almost never what you want for a running log.

**Manual writing with `fopen()`**

```php
<?php

$handle = fopen(__DIR__ . "/order-log.txt", "a");

if ($handle) {
    fwrite($handle, "Order placed at " . date("Y-m-d H:i:s") . "\n");
    fclose($handle);
} else {
    echo "Could not write to the log file.";
}
```

**Overwriting a file completely**, useful for something like regenerating a saved menu from scratch:

```php
<?php

$menuContent = "Adobo - 150\nSinigang - 180\nLumpia - 90\n";

file_put_contents(__DIR__ . "/menu.txt", $menuContent); // no FILE_APPEND, so this replaces everything
```

## Kitchen Notes (Best Practices)

- **Be deliberate about append versus overwrite.** A missing `FILE_APPEND` flag on a log file is a genuinely common, easy mistake that quietly destroys existing data the moment it happens.
- **Check `file_put_contents()`'s return value.** It returns the number of bytes written on success, or `false` on failure, and that failure should never be silently ignored, especially for anything important like an order log.
- **Never write a file path built directly from unvalidated user input.** The path traversal warning from the File Handling chapter applies with even more force here, since writing lets an attacker not just read unintended files, but potentially create or overwrite them.
- **Keep sensitive files, like logs containing personal information, outside the folder your web server actually serves publicly.** A log file sitting inside a publicly accessible folder can potentially be viewed directly by anyone who guesses or finds its URL.

## Yoras' Mistake

Yoras wants to add a new line to the daily log every time an order comes in, and writes:

```php
<?php

$logLine = "Order placed at " . date("Y-m-d H:i:s") . "\n";
file_put_contents(__DIR__ . "/order-log.txt", $logLine);
```

Every single order overwrites the entire log file with just that one line, since `FILE_APPEND` was never included. By the end of the day, the log only ever shows the single most recent order, and every earlier one has been silently erased.

**Lesson:** always include the `FILE_APPEND` flag when the intent is to add to an existing file rather than replace it, and think carefully, every single time you write a file, about which of those two behaviors you actually want.

## Take-Home Practice

1. Write a function that appends a timestamped message to a log file, using `file_put_contents()` with `FILE_APPEND`.
2. Call that function three times in a row, and confirm all three lines are preserved in the file afterward.
3. Deliberately leave out `FILE_APPEND` once, and observe that the earlier lines disappear.

## Recap

- `file_put_contents()` writes a string to a file in one call, creating it if needed, and replacing existing content unless `FILE_APPEND` is used.
- `fopen()` mode `"w"` erases existing content immediately. Mode `"a"` preserves it and appends. Mode `"x"` fails if the file already exists.
- Always check whether a write operation actually succeeded, rather than assuming it did.
- Never build a file path for writing directly from unvalidated user input, and keep sensitive files outside your publicly served folder.

Next chapter: file uploads, or what happens when a customer hands you a file directly.
