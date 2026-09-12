# Chapter 14: PHP Operators

### Kitchen Actions

---

## Back in the Kitchen

Combining, comparing, and adjusting. Every action in a kitchen falls into one of these three categories, and so does nearly every operator in PHP.

## The Concept

**Arithmetic operators** handle basic math: `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `%` (modulo, meaning "the remainder after dividing"), and `**` (exponent, meaning "raised to the power of").

**Assignment operators** store a value into a variable. Plain `=` is the basic one. PHP also offers shortcuts that combine an operation with assignment: `+=`, `-=`, `*=`, `/=`. Writing `$total += 10;` is shorthand for `$total = $total + 10;`.

**Comparison operators** ask a true-or-false question about two values: `==`, `!=`, `<`, `>`, `<=`, `>=`. There's also `===` and `!==`, which check both value *and* type together, not just value.

**Logical operators** combine multiple true-or-false conditions: `&&` (and), `||` (or), `!` (not).

**Increment and decrement operators**, `++` and `--`, add or subtract exactly one from a variable.

## In the Code Kitchen

**Arithmetic and assignment shortcuts**

```php
<?php

$total = 100;
$total += 20; // same as $total = $total + 20
echo $total;  // 120

$remaining = 10 % 3; // 1, the remainder after 10 divided by 3
echo $remaining;
```

**Comparison: `==` versus `===`**

This is the single most important distinction in this whole chapter:

```php
<?php

var_dump(5 == "5");  // true, values match after PHP converts types
var_dump(5 === "5"); // false, same value, but different types (int vs string)
```

`==` is called "loose comparison." It converts types as needed before comparing. `===` is "strict comparison." It only returns true if both the value and the type match exactly. In modern PHP, the strong, near-universal recommendation is: **default to `===` and `!==`**, and only reach for `==` when you have a specific, deliberate reason to allow type conversion.

**Logical operators**

```php
<?php

$isOpen = true;
$hasStock = false;

if ($isOpen && $hasStock) {
    echo "We can serve this dish.";
} else {
    echo "Sorry, not available right now.";
}
```

**The null coalescing operator**

One more operator worth knowing early, `??`, checks whether a value is `null` (or simply doesn't exist yet) and provides a fallback if so. This comes up constantly once you're working with form data or array values that might not be set:

```php
<?php

$discount = null;
$finalDiscount = $discount ?? 0; // uses 0, since $discount is null

echo $finalDiscount; // 0
```

## Kitchen Notes (Best Practices)

- **Default to `===` and `!==` for comparisons.** `==` has caused enough real, hard-to-spot bugs across the history of PHP that treating strict comparison as the default, safe habit is widely considered good practice today.
- **Use `??` instead of a longer `isset()` check** when you just need a fallback value for something that might be `null` or missing. It reads cleanly and does exactly one job.
- **Don't chain too many logical operators into one unreadable line.** If a condition needs three or four `&&` and `||` combined, consider breaking it into a named variable or two first, so the logic is easier to follow at a glance.

## Yoras' Mistake

Yoras builds a discount checker for a promo code:

```php
<?php

$enteredCode = "0";
if ($enteredCode == false) {
    echo "No code entered.";
} else {
    echo "Code accepted: $enteredCode";
}
```

He enters the code `"0"`, a perfectly real, valid promo code, and gets "No code entered," even though a code clearly was entered. The string `"0"` is one of PHP's falsy values, discussed back in Chapter 7, so `"0" == false` evaluates to `true`.

**Lesson:** don't use a general truthy or falsy check to test something specific, like "was a value entered at all." Use a purpose-built check instead, such as `$enteredCode === ""` to test for an empty string specifically, or `isset($enteredCode)` to test whether a variable exists at all.

## Take-Home Practice

1. Write three comparisons using `==` and their `===` equivalents, using values where the results differ (a number and a matching numeric string is a good place to start).
2. Combine `&&` and `||` in a single condition that decides whether a dish should be shown as "available today."
3. Use `??` to provide a default serving size when a variable might be `null`.

## Recap

- Arithmetic operators handle math; assignment operators (including shortcuts like `+=`) store values.
- `==` compares loosely, converting types as needed. `===` compares strictly, checking both value and type.
- Default to `===` and `!==` unless there's a specific, deliberate reason to allow loose comparison.
- `&&`, `||`, and `!` combine conditions. `??` provides a fallback for a `null` or missing value.

Next chapter: `if`, `else`, and `elseif`, or how a kitchen decides what to do next.
