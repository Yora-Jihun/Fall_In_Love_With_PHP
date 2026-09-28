# Chapter 21: PHP Regex

### The Quality Inspector

---

## Back in the Kitchen

Before a shipment of rice goes into the pantry, someone checks it. Right grain size, no visible spoilage, matches the standard the kitchen expects. Regular expressions, almost always called regex, do exactly this job for text. They check whether a piece of text matches an exact pattern you define, down to the smallest detail.

## The Concept

A **regular expression** is a small, specialized pattern language for describing the shape of text. It looks unfamiliar at first, more like a secret code than a sentence, but a handful of building blocks cover the vast majority of everyday use:

- `/pattern/` : the pattern is wrapped in delimiters, most commonly forward slashes.
- `^` : anchors the match to the start of the string.
- `$` : anchors the match to the end of the string.
- `.` : matches any single character.
- `\d` : matches any single digit.
- `\w` : matches any single "word" character (a letter, digit, or underscore).
- `+` : means "one or more" of whatever came before it.
- `*` : means "zero or more" of whatever came before it.
- `{n}` : means "exactly n" of whatever came before it.
- `[abc]` : matches any one of the characters listed inside the brackets.

PHP's main regex functions are `preg_match()` (checks whether a pattern matches, and can capture the matched portion), `preg_match_all()` (finds every match in a string, not just the first), `preg_replace()` (finds matches and replaces them), and `preg_split()` (splits a string wherever a pattern matches).

## In the Code Kitchen

Create a new file named `regex.php` in your `kitchen` folder, and open it at `http://kitchen.test/regex.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

**Checking a simple pattern**

```php
<?php

$code = "ORD-1234";

if (preg_match("/^ORD-\d{4}$/", $code)) {
    echo "Valid order code format.";
} else {
    echo "Invalid format.";
}
```

Reading that pattern piece by piece: `^ORD-` means the string must start with exactly "ORD-", `\d{4}` means exactly four digits must follow, and `$` means nothing else is allowed after those digits.

**Capturing part of a match**

```php
<?php

$order = "Quantity: 5 servings";

if (preg_match("/Quantity: (\d+)/", $order, $matches)) {
    echo $matches[1]; // 5, the captured digits from inside the parentheses
}
```

Parentheses inside a pattern create a "capture group," pulling out just the part you actually care about, stored in `$matches[1]` (with `$matches[0]` always holding the entire matched text).

**Replacing text that matches a pattern**

```php
<?php

$menu = "Adobo costs 150. Sinigang costs 180.";

$updated = preg_replace("/\d+/", "XXX", $menu);
echo $updated; // Adobo costs XXX. Sinigang costs XXX.
```

**A realistic, common use: validating a simple username**

```php
<?php

$username = "cook_627";

if (preg_match("/^[a-zA-Z0-9_]{3,20}$/", $username)) {
    echo "Valid username.";
} else {
    echo "Username must be 3-20 characters: letters, numbers, or underscores only.";
}
```

## Kitchen Notes (Best Practices)

- **Reach for a purpose-built function first, before writing a regex.** For checking a valid email format specifically, PHP's own `filter_var()` (covered fully in the Filters chapter) is generally the better, more maintainable choice. Save regex for patterns that genuinely need custom shape-matching.
- **Keep patterns as simple as the job actually requires.** A regex that's hard to read six months from now is a liability, not a convenience. If a pattern is getting complex, add a comment explaining what it's meant to catch.
- **Test a new regex against both valid and clearly invalid examples** before trusting it in real code, since a pattern that's slightly too loose or too strict is an easy, common mistake.

## Yoras' Mistake

Yoras writes a pattern meant to validate a four-digit PIN, but forgets the anchors:

```php
<?php

$pin = "12345"; // five digits, should be invalid

if (preg_match("/\d{4}/", $pin)) {
    echo "Valid PIN."; // incorrectly prints this
}
```

This incorrectly accepts a five-digit input. Without `^` and `$` anchoring the pattern to the start and end of the string, `\d{4}` is satisfied by finding *any* four consecutive digits *anywhere* inside the string, including as part of a longer, five-digit number.

**Lesson:** when a pattern needs to match the *entire* string, not just some part of it, anchor it with `^` at the start and `$` at the end:

```php
<?php

$pin = "12345";

if (preg_match("/^\d{4}$/", $pin)) {
    echo "Valid PIN.";
} else {
    echo "PIN must be exactly 4 digits.";
}
```

## Take-Home Practice

1. Write a pattern that validates a Philippine-style mobile number in the format `09XXXXXXXXX` (11 digits, starting with `09`).
2. Use `preg_match()` with a capture group to pull just the numeric price out of a string like `"Price: 150 pesos"`.
3. Reproduce Yoras' unanchored PIN mistake, confirm the incorrect behavior, then fix it with proper anchors.

## Recap

- Regex describes the shape of text using a compact pattern language: anchors, character classes, and repetition symbols.
- `preg_match()` checks for a match and can capture parts of it. `preg_match_all()`, `preg_replace()`, and `preg_split()` cover finding, replacing, and splitting.
- `^` and `$` anchor a pattern to the start and end of a string. Leaving them out lets a pattern match anywhere inside the string, often unintentionally.
- For common, well-defined formats like email addresses, prefer PHP's built-in validation functions over writing a custom regex.

This closes out **Part 1: The Foundation**. Next up: **Part 2, PHP Forms**, where the kitchen finally starts taking real orders from real customers.
