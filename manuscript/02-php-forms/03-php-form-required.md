# Chapter 24: PHP Form Required Fields

### The Fields That Can't Be Left Blank

---

## Back in the Kitchen

Some parts of an order ticket are optional. "Any special requests?" can stay blank. Others cannot. A ticket with no dish name isn't an order at all, it's just a blank piece of paper. This chapter zooms in on that one specific, extremely common check: making sure a field wasn't left empty.

## The Concept

Chapter 23 introduced the overall shape of validation. This chapter focuses specifically on the pattern for a required field, since it's the single most common validation check you'll write, appearing in nearly every form you'll ever build.

The reliable version of this check has two parts, and skipping either one causes real bugs:

1. **`trim()` the value first**, so input that's only spaces doesn't slip past the check.
2. **Compare it to an empty string using `===`**, rather than using PHP's general "empty" checks alone, which can behave in surprising ways for values like `"0"`.

## In the Code Kitchen

```php
<?php

$errors = [];
$dishName = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $dishName = trim($_POST["dishName"] ?? "");

    if ($dishName === "") {
        $errors[] = "Dish name is required.";
    }
}
```

This same pattern extends cleanly to multiple required fields, checked one after another:

```php
<?php

$errors = [];
$customerName = "";
$dishName = "";
$servings = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $customerName = trim($_POST["customerName"] ?? "");
    $dishName = trim($_POST["dishName"] ?? "");
    $servings = trim($_POST["servings"] ?? "");

    if ($customerName === "") {
        $errors[] = "Please enter your name.";
    }

    if ($dishName === "") {
        $errors[] = "Please choose a dish.";
    }

    if ($servings === "") {
        $errors[] = "Please enter the number of servings.";
    }
}
```

Worth knowing: PHP's `empty()` function is often reached for here instead, but it treats several values as "empty" that might genuinely be valid input, most notably the string `"0"`. If a field could legitimately be the value `"0"` (a quantity, a discount amount, a table number), `empty()` will incorrectly flag it as missing:

```php
<?php

$discountCode = "0"; // a real, valid code

var_dump(empty($discountCode)); // bool(true), incorrectly treated as "empty"
var_dump($discountCode === ""); // bool(false), correctly recognized as present
```

This is the same falsy-string edge case first introduced in Chapter 7, showing up again here in a place where it can quietly break real functionality.

## Kitchen Notes (Best Practices)

- **Use `trim($value) === ""` to check for a genuinely empty required field**, rather than `empty($value)`, unless you've specifically confirmed the field could never legitimately be `"0"`.
- **Give each required field its own specific error message.** "Please fill out all fields" tells a visitor nothing about which field is the actual problem. "Please enter your name" tells them exactly what to fix.
- **Mark required fields clearly in the HTML too**, using the `required` attribute, purely as a helpful, immediate hint for the visitor. Remember, per the last chapter, this is a convenience only. The real check still has to happen in PHP.

## Yoras' Mistake

Yoras builds a form with a table number field, where `"0"` is a perfectly valid table number for counter seating, and checks it like this:

```php
<?php

$tableNumber = $_POST["tableNumber"] ?? "";

if (empty($tableNumber)) {
    $errors[] = "Please enter a table number.";
}
```

A customer at the counter, correctly entering `"0"`, gets told their required field is missing, even though they filled it out exactly as asked.

**Lesson:** whenever `"0"` could be a legitimate value for a field, check for emptiness with `trim($value) === ""`, not `empty($value)`, so a real, valid zero isn't mistaken for a missing field.

## Take-Home Practice

1. Write a required-field check for an `email` field, using the correct `trim()` and `=== ""` pattern.
2. Demonstrate, with a small test script, how `empty("0")` and `"0" === ""` disagree, and explain in your own words why that matters for form validation.
3. Add the HTML `required` attribute to a form field, then explain, in a comment, why the PHP-side check is still necessary even with it in place.

## Recap

- The reliable required-field check is: `trim($value) === ""`.
- `empty()` treats several genuinely valid values, most notably `"0"`, as empty, which can incorrectly reject valid input.
- Every required-field error message should name the specific field, not just say something generic went wrong.
- The HTML `required` attribute is a helpful hint for the visitor, never a replacement for a real server-side check.

Next chapter: validating specific formats, like a URL or an e-mail address.
