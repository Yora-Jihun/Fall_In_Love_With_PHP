# Chapter 3: PHP Syntax

### The Rules of the Kitchen

---

## Back in the Kitchen

Every kitchen has house rules, even if nobody wrote them down. Wash your hands before touching food. Label what's in the fridge. Clean your station when you're done. Break one of these rules and nothing explodes, but the next cook who uses your station will have a bad time.

PHP has house rules too. They're small, but skipping them is the single biggest source of beginner headaches.

## The Concept

PHP code is written between an opening tag, `<?php`, and, when needed, a closing tag, `?>`. Everything between those tags is treated as PHP instructions. Everything outside them is treated as plain text or HTML, and sent to the browser exactly as written.

Inside those tags, a few rules apply everywhere:

- **Every statement ends with a semicolon** (`;`). A statement is one complete instruction, the way one line on a recipe card is one complete step. Forgetting the semicolon is the single most common syntax error in this entire language, for beginners and veterans alike.
- **Code blocks are wrapped in curly braces** (`{ }`). You'll see these constantly, in `if` statements, loops, and functions, starting in the next few chapters.
- **Whitespace mostly doesn't matter.** Extra spaces, blank lines, and indentation don't change what the code does. They exist entirely for humans to read the recipe more easily. Use them generously.
- **Variable names are case-sensitive.** `$total` and `$Total` are two different containers. Function and keyword names are not case-sensitive, so `echo`, `ECHO`, and `Echo` all work the same, though writing them in lowercase is the standard, expected style.
- **PHP can be mixed directly into HTML.** You can drop in and out of PHP mode as many times as a page needs, which is genuinely useful for older-style templates, though this book generally keeps PHP and HTML cleanly separated once we reach the Forms section.

## In the Code Kitchen

Create a new file named `syntax.php` in your `kitchen` folder, and open it at `http://kitchen.test/syntax.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

Here's PHP mixed into HTML, which is legal and common:

```php
<!DOCTYPE html>
<html>
<body>

<h1>Today's Menu</h1>

<?php
echo "Chicken Adobo is the special today.";
?>

</body>
</html>
```

Notice the closing `?>` is used here, because PHP is only a small part of a larger HTML file. This is the one common, correct exception to the "no closing tag" habit from Chapter 1: when a file mixes PHP with other content, the closing tag is expected wherever a PHP block ends.

Compare a correct statement to a broken one:

```php
<?php
$dish = "sinigang";   // correct: ends with a semicolon
echo $dish;
```

```php
<?php
$dish = "sinigang"    // missing semicolon
echo $dish;
```

The second version fails to run at all. PHP doesn't guess where one instruction ends and the next begins. That's the semicolon's entire job.

**Turning on error display**

When you run the broken version, you should see an error message on the page that points to the line that broke. If you only see a blank white page, error display is turned off. It's controlled by a setting called `display_errors`, inside PHP's settings file, `php.ini`. Here's how to find it and turn it on.

1. **Find your `php.ini` file.** In your `kitchen` folder, create a file named `info.php` with just this line in it:

    ```php
    <?php phpinfo();
    ```

    Save it and open `http://kitchen.test/info.php`. You'll see a long page of PHP details. Near the top, look for the row called **Loaded Configuration File**. That's the full path to your `php.ini`. With Herd, it's usually somewhere like this:

    - Windows: `C:\Users\<your-name>\.config\herd\bin\php84\php.ini`
    - macOS: `~/Library/Application Support/Herd/config/php/84/php.ini`

    The number in the path matches your PHP version, so `84` means PHP 8.4. Always trust the path on your own `info.php` page over these examples.

    Shortcut: Herd also has a `herd ini` terminal command that gives you quick access to the same file.

2. **Open `php.ini` in VS Code and find the setting.** Press Ctrl+F (Cmd+F on a Mac) and search for `display_errors`. You may find it more than once. Lines that start with a semicolon (`;`) are only comments, so skip those. Find the line that doesn't start with `;` and make sure it says:

    ```ini
    display_errors = On
    ```

    If it already says `On`, there's nothing to change.

3. **Save the file and restart Herd's services.** The web server only reads `php.ini` when it starts. Click the Herd icon (in the system tray on Windows, or the menu bar on macOS), choose **Stop all**, then **Start all**. You can also run `herd restart` in a terminal.

4. **Check that it worked.** Reload `info.php` and press Ctrl+F (Cmd+F on a Mac) to search the page for `display_errors`. It should now show `On`. Then run the broken semicolon example again, and you should see the error message.

5. **Delete `info.php` when you're done.** It shows a lot of details about your setup. That's fine on your own computer, but it's a habit worth building now, since a file like this should never be left on a real website.

## Kitchen Notes (Best Practices)

- **Turn on error display while you're learning.** A local PHP setup can be configured to show errors directly on the page, which turns a blank white screen into a useful message pointing at the exact line that broke. This is controlled by a setting called `display_errors` in a file called `php.ini`, and the steps above show how to turn it on.
- **Read error messages from the bottom up when there are several.** The first error is often the real one. The rest can just be side effects of that first mistake.
- **Keep indentation consistent.** It costs nothing, and it's the difference between a recipe you can read at a glance and one you have to decode.

## Yoras' Mistake

Yoras writes an entire block of code, then spends ten minutes staring at a blank white page with no error message at all. He assumes the server is broken.

The real problem is his local setup has error display turned off, which is actually the default, safer setting for a live, public website. On a real production server, showing raw error details to visitors is a security risk, since errors can leak information about how the code works. But on your own practice machine, hiding errors just means you're debugging blind.

**Lesson:** for local development only, turn on error display so PHP tells you exactly what went wrong and on which line.

## Take-Home Practice

1. Write a short PHP file that intentionally forgets a semicolon. Run it, read the error message it produces, then fix it.
2. Write one PHP file that mixes plain HTML with a single PHP block in the middle, similar to the menu example above.
3. Use `info.php` to find the `php.ini` file your Herd PHP version uses, and check that `display_errors` is set to `On`. Then delete `info.php`.

## Recap

- PHP code lives between `<?php` and, when mixing with HTML, `?>`.
- Every statement ends in a semicolon.
- Code blocks use curly braces.
- Whitespace is for readability only. It doesn't change behavior.
- Variable names are case-sensitive. Function and keyword names are not, but lowercase is the convention.
- Turning on error display locally turns invisible mistakes into readable ones.

Next chapter: comments, or how to leave yourself (and every future cook who reads your recipe) a note.
