# Chapter 35: PHP Filters

### The Strainer

---

## Back in the Kitchen

A strainer does one job: it lets through what belongs, and catches what doesn't. Every ingredient that comes into the kitchen from outside, forms, cookies, uploaded files, deserves to pass through something like it before it's used. PHP's filter system is that strainer, and Chapter 25 already used one small piece of it, `FILTER_VALIDATE_EMAIL`, without naming the bigger system it belongs to.

## The Concept

PHP's filtering system is built around one central function, `filter_var()`, which takes a value and a filter, and does one of two kinds of jobs:

- **Validating filters** check whether a value matches a specific format, returning the value if it passes, or `false` if it doesn't. `FILTER_VALIDATE_EMAIL`, `FILTER_VALIDATE_URL`, `FILTER_VALIDATE_INT`, and `FILTER_VALIDATE_BOOLEAN` are common examples.
- **Sanitizing filters** don't check anything. They clean a value by removing or encoding characters that don't belong, always returning some usable result, never `false`. `FILTER_SANITIZE_FULL_SPECIAL_CHARS` and `FILTER_SANITIZE_NUMBER_INT` are common examples.

A companion function, `filter_input()`, combines reading a value directly from `$_GET`, `$_POST`, or `$_COOKIE` with applying a filter to it, in one step, which can be a cleaner habit than reading a superglobal directly and filtering it as a separate line.

## In the Code Kitchen

Create a new file named `filters.php` in your `kitchen` folder, and open it at `http://kitchen.test/filters.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

**Validating filters**

```php
<?php

var_dump(filter_var("42", FILTER_VALIDATE_INT));        // int(42)
var_dump(filter_var("not a number", FILTER_VALIDATE_INT)); // bool(false)

var_dump(filter_var("true", FILTER_VALIDATE_BOOLEAN));   // bool(true)
var_dump(filter_var("no", FILTER_VALIDATE_BOOLEAN));     // bool(false)
```

Notice `FILTER_VALIDATE_INT` is meaningfully stricter than the `is_numeric()` check used back in Chapter 10. `is_numeric()` happily accepts strings like `"5.5"` or `"1e3"`, since they're valid numbers. `FILTER_VALIDATE_INT` rejects both, because neither is a plain whole number.

**Sanitizing filters**

```php
<?php

$comment = "<script>alert('hi')</script> Great food!";
$clean = filter_var($comment, FILTER_SANITIZE_FULL_SPECIAL_CHARS);

echo $clean; // the dangerous tag is neutralized, safe to display
```

This is doing very similar work to `htmlspecialchars()`, and in practice, for output going into HTML, `htmlspecialchars()` remains the clearer, more direct tool. Sanitizing filters shine more for cleaning data on the way *in*, before it's stored or processed, rather than as the final step before display.

**`filter_input()`, reading directly from a superglobal**

```php
<?php

$servings = filter_input(INPUT_POST, "servings", FILTER_VALIDATE_INT);

if ($servings === false || $servings === null) {
    echo "Please enter a valid number of servings.";
} else {
    echo "Servings: " . $servings;
}
```

`filter_input()` returns `null`, not `false`, if the field wasn't submitted at all, distinct from `false` for a field that was submitted but failed validation. Checking both is worth the extra care here.

## Kitchen Notes (Best Practices)

- **Reach for `FILTER_VALIDATE_INT` instead of `is_numeric()` plus a manual cast** when you specifically need a whole number, since it's stricter and handles more edge cases correctly in one step.
- **Keep sanitizing and escaping conceptually separate**, even though they can look similar. Sanitize data on the way in, to clean it before storing or processing it. Escape data on the way out, with `htmlspecialchars()`, right before it's displayed. Doing one doesn't remove the need for the other.
- **Check for both `false` and `null` when using `filter_input()`**, since they mean different things: a value that failed validation, versus a value that was never sent at all.

## Yoras' Mistake

Yoras validates a quantity field using `is_numeric()` alone, trusting it fully:

```php
<?php

$quantity = $_POST["quantity"] ?? "";

if (is_numeric($quantity)) {
    $total = $quantity * 65.50; // seems safe enough
}
```

A visitor enters `"5.5"`, which passes `is_numeric()` easily, since it's a perfectly valid number, just not a valid *whole number* of servings. The order proceeds with a fractional quantity that makes no sense for the business.

**Lesson:** `is_numeric()` only confirms a value is *some kind* of number. If you specifically need an integer, use `FILTER_VALIDATE_INT`, which enforces that more precisely than a manual check would.

## Take-Home Practice

1. Use `filter_var()` with `FILTER_VALIDATE_INT` to validate a servings field, rejecting anything that isn't a whole number.
2. Use `filter_input()` to read and validate an `email` field directly from `$_POST`, distinguishing between "not submitted" and "submitted but invalid."
3. Explain, in your own words, the difference between a sanitizing filter and a validating filter.

## Recap

- `filter_var()` either validates a value's format (returning it, or `false`, if it fails) or sanitizes it (cleaning it, always returning something usable).
- `filter_input()` reads directly from `$_GET`, `$_POST`, or `$_COOKIE` and applies a filter in one step, returning `null` if the field was never sent.
- Sanitize data on the way in. Escape data (with `htmlspecialchars()`) on the way out. These are related but separate habits.
- `FILTER_VALIDATE_INT` is stricter than `is_numeric()` when you specifically need a whole number.

Next chapter: a deeper, more advanced look at combining filters across an entire form at once.
