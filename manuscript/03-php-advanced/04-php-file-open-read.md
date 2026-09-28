# Chapter 30: PHP File Open and Read

### Reading the Notebook

---

## Back in the Kitchen

The log file from the last chapter is only useful if someone can actually read it back later. This chapter focuses entirely on that half of the job: getting a file's contents into your script.

## The Concept

PHP gives you two main approaches, and which one you reach for depends mostly on the file's size and what you're trying to do with it:

- **`file_get_contents($path)`** reads an entire file into a single string, in one line of code. This is the simplest option, and the right default choice for most everyday files, like a config file, a saved menu, or a reasonably sized log.
- **Reading line by line with `fopen()` and `fgets()`** processes a file one line at a time, without ever loading the whole thing into memory at once. This matters for genuinely large files, where loading everything at once could use more memory than is reasonable.

## In the Code Kitchen

Create a new file named `read-file.php` in your `kitchen` folder, and open it at `http://kitchen.test/read-file.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

You'll also need something to read. In the same folder, create a plain text file named `menu.txt` with a few lines, like `Adobo - 150` and `Sinigang - 180`. The line-by-line example reads `order-log.txt`, which you created in the last chapter.

**The simple, common case**

```php
<?php

$content = file_get_contents(__DIR__ . "/menu.txt");
echo nl2br(htmlspecialchars($content));
```

`nl2br()` converts plain line breaks in the text into HTML `<br>` tags, so they actually show up as line breaks in the browser, exactly the same issue Chapter 6 first pointed out about blank lines being invisible to HTML. Note the order here: escape first with `htmlspecialchars()`, since the file's content should still be treated as untrusted if there's any chance it came from outside your own code, and only then convert line breaks for display.

**Reading line by line**

```php
<?php

$handle = fopen(__DIR__ . "/order-log.txt", "r");

if ($handle) {
    while (($line = fgets($handle)) !== false) {
        echo htmlspecialchars($line) . "<br>";
    }
    fclose($handle);
}
```

That `!== false` comparison matters. `fgets()` returns `false` specifically when it reaches the end of the file, and using `!==` (strict comparison, from Chapter 14) avoids a subtle trap. If the last line of the file is just the character `0`, with no line break after it, a loose check treats that `"0"` as falsy, the same edge case from Chapter 7, and mistakes it for the end of the file.

**Checking if a file exists before reading it**, tying back to the last chapter:

```php
<?php

$path = __DIR__ . "/menu.txt";

if (file_exists($path)) {
    echo file_get_contents($path);
} else {
    echo "Menu file not found.";
}
```

## Kitchen Notes (Best Practices)

- **Reach for `file_get_contents()` by default.** It's shorter, harder to get wrong, and perfectly adequate for the vast majority of files a typical application deals with.
- **Only switch to line-by-line reading with `fgets()` when a file is genuinely large enough that loading it all at once would be wasteful or risky.** Don't add this complexity before you actually need it.
- **Escape file content with `htmlspecialchars()` before displaying it**, exactly as with any other untrusted source, unless you wrote and fully control every byte of that file yourself and are certain it will never contain anything unexpected.

## Yoras' Mistake

Yoras reads a log file line by line, but checks for the end of the file incorrectly:

```php
<?php

$handle = fopen(__DIR__ . "/order-log.txt", "r");

while ($line = fgets($handle)) {
    echo $line . "<br>";
}

fclose($handle);
```

This looks reasonable, and it works for most files. But if the last line is just `0`, with no line break after it, `fgets()` returns the string `"0"`. That's falsy, so the loop stops and skips it, treating a real line of data as if it meant "end of file."

**Lesson:** always compare `fgets()`'s result against `false` explicitly, using `!== false`, rather than relying on the loosely truthy or falsy value of the line itself. This is a small, specific detail, but it's exactly the kind of edge case a careless comparison misses.

## Take-Home Practice

1. Create a small text file with three lines of dish names, and read the whole thing at once with `file_get_contents()`.
2. Read the same file line by line using `fopen()` and `fgets()`, printing each line separately.
3. Make the last line of the file just `0`, with no line break after it. Run Yoras' loop and the correct `!== false` loop, and compare which one prints that last line.

## Recap

- `file_get_contents()` reads an entire file into a string in one call, and is the right default for most files.
- Line-by-line reading with `fopen()` and `fgets()` is for genuinely large files where loading everything at once isn't practical.
- Always compare `fgets()`'s result with `!== false`, to correctly detect the actual end of the file.
- File content should be escaped with `htmlspecialchars()` before being displayed, the same as any other untrusted source.

Next chapter: creating and writing files, the other half of the notebook.
