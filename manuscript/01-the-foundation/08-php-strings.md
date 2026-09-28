# Chapter 8: PHP Strings

### Working With Text

---

## Back in the Kitchen

Text is the flour of programming. It shows up in nearly every dish you'll ever cook: a dish name, a customer's order, an address, a message on the screen. Getting comfortable with strings pays off in almost every chapter that follows.

## The Concept

A **string** is a sequence of characters, wrapped in either single quotes (`'...'`) or double quotes (`"..."`). Chapter 6 already introduced the one major difference between them:

- **Double-quoted strings** support variable interpolation (`"Hello, $name"`) and recognize escape sequences like `\n` for a new line.
- **Single-quoted strings** treat almost everything literally. `$name` stays as literal text, and most escape sequences aren't processed.

Beyond that, PHP includes a large library of built-in functions for working with strings. You don't need to memorize all of them today. Getting familiar with a handful of the most common ones is enough to get real work done, and you can always look up the rest when you need them.

## In the Code Kitchen

Create a new file named `strings.php` in your `kitchen` folder, and open it at `http://kitchen.test/strings.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

**Combining strings**

```php
<?php

$first = "Adobong";
$second = "Manok";
$fullName = $first . " " . $second;

echo $fullName; // Adobong Manok
```

**Measuring and searching**

```php
<?php

$dish = "Chicken Adobo";

echo strlen($dish);          // 13, the number of characters
echo "<br>";
echo str_word_count($dish);  // 2, the number of words
echo "<br>";
echo strpos($dish, "Adobo"); // 8, the position where "Adobo" starts
```

`strpos()` counts from zero, the same way most counting works in programming. The very first character of a string is at position 0, not position 1.

**Changing case and replacing text**

```php
<?php

$dish = "chicken adobo";

echo strtoupper($dish);                    // CHICKEN ADOBO
echo "<br>";
echo ucwords($dish);                       // Chicken Adobo
echo "<br>";
echo str_replace("chicken", "pork", $dish); // pork adobo
```

**Trimming extra space**

```php
<?php

$input = "   Sinigang   ";
echo trim($input); // "Sinigang", with the surrounding spaces removed
```

`trim()` becomes especially important once you're working with real user input in the Forms section, since people reliably type extra spaces without noticing.

**Multi-line strings with heredoc**

For a longer block of text that mixes in variables, PHP offers heredoc syntax, which behaves like a double-quoted string that can span multiple lines cleanly:

```php
<?php

$dish = "Sinigang";
$price = 180;

$menuEntry = <<<TEXT
Today's Special: $dish
Price: $price pesos
TEXT;

echo $menuEntry;
```

## Kitchen Notes (Best Practices)

- **Use double quotes only when you actually need interpolation or escape sequences.** Otherwise, single quotes are a perfectly reasonable, common default. Neither choice is a security issue by itself. What matters is escaping output correctly, covered starting in the Forms section.
- **Never build HTML output by blindly concatenating raw user input into a string.** This chapter's examples use text we wrote ourselves. The moment a string comes from a customer, a form, or a file, it needs to be treated as untrusted and escaped with `htmlspecialchars()` before being echoed.
- **Reach for `trim()` early and often** whenever a string might have accidental leading or trailing spaces, especially anything a person typed by hand.

## Yoras' Mistake

Yoras wants to check if a customer's order includes the word "extra," and writes:

```php
<?php

$order = "extra rice please";
if ($order == "extra") {
    echo "Found it.";
}
```

Nothing prints. `==` checks whether two strings are *entirely* identical, not whether one contains the other. `"extra rice please"` and `"extra"` are different strings, full stop.

**Lesson:** to check whether one string contains another, use `str_contains()` (available in modern PHP), not `==`:

```php
<?php

$order = "extra rice please";
if (str_contains($order, "extra")) {
    echo "Found it.";
}
```

## Take-Home Practice

1. Take a dish name of your choosing, print its length, and print an uppercase version of it.
2. Use `str_replace()` to swap one ingredient in a sentence for another.
3. Write a string with extra spaces around it on purpose, then clean it with `trim()` and print both versions to compare.

## Recap

- Strings can be built with single or double quotes. Double quotes support interpolation and escape sequences.
- `strlen()`, `strpos()`, `str_word_count()`, `strtoupper()`, `ucwords()`, `str_replace()`, and `trim()` cover a large share of everyday string work.
- Heredoc syntax is useful for longer, multi-line text that still needs variable interpolation.
- `str_contains()` checks whether a string appears inside another string. `==` only checks for exact equality.

Next chapter: numbers, and the small but important details of how PHP handles them.
