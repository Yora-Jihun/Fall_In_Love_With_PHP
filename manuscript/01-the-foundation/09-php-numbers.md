# Chapter 9: PHP Numbers

### Measurements That Matter

---

## Back in the Kitchen

A recipe that says "add some sugar" is a recipe waiting to go wrong. A recipe that says "add 2 tablespoons of sugar" is repeatable. Numbers are where a recipe, and a program, get precise.

## The Concept

PHP works with two numeric types day to day:

- **int**: a whole number, with no decimal point. `3`, `-40`, `0`.
- **float**: a number with a decimal point, used for anything that needs fractional precision. `3.5`, `-0.25`, `19.99`.

PHP decides which one you're using automatically, based on how you write the number. `10` is an int. `10.0` is a float, even though it represents the same mathematical value, because PHP looks at the literal form, not just the underlying value.

A detail worth knowing early: floats are stored using a format that can't represent every decimal value with perfect precision, a limitation shared by essentially every programming language, not something unique to PHP. This means a calculation like `0.1 + 0.2` can come out to something like `0.30000000000000004` instead of a clean `0.3`. This is rarely a problem for everyday use, but it matters the moment you're dealing with money. For currency, it's common practice to work in whole cents (or centavos) as integers internally, and only convert to a decimal display format at the very end.

## In the Code Kitchen

```php
<?php

$quantity = 4;        // int
$unitPrice = 65.50;   // float

$total = $quantity * $unitPrice;
echo $total; // 262
```

You can check whether a value is numeric, even if it's currently stored as a string, using `is_numeric()`:

```php
<?php

$input = "12";
var_dump(is_numeric($input)); // bool(true)

$input2 = "twelve";
var_dump(is_numeric($input2)); // bool(false)
```

For displaying numbers nicely, especially money, `number_format()` is the tool to reach for:

```php
<?php

$total = 24403.344433;
echo number_format($total, 2); // 24,403.34
```

Math often leaves you with long, messy decimals like this one. Nobody pays 24,403.344433 pesos. The second argument, `2`, tells `number_format()` to show only two decimal places, the cents. It also adds the comma for thousands, which plain math never gives you for free.

Note that `number_format()` rounds. It doesn't just cut off the extra digits. So `24403.346` would show as `24,403.35`, not `24,403.34`.

A few more genuinely useful functions:

```php
<?php

echo round(3.7);   // 4
echo "<br>";
echo floor(3.7);   // 3, always rounds down
echo "<br>";
echo ceil(3.2);    // 4, always rounds up
echo "<br>";
echo abs(-15);     // 15, the absolute value, always non-negative
```

## Kitchen Notes (Best Practices)

- **Never compare two floats directly for exact equality** (`$a == $b`), since tiny precision errors can make two numbers that "should" be equal come out slightly different. If you need to compare floats, check whether the difference between them is smaller than some tiny acceptable amount, rather than checking for perfect equality.
- **For money, favor integers (cents/centavos) internally, and format for display only at the end**, using `number_format()`. This avoids float precision issues entirely in the calculations that matter most.
- **Validate that a value is actually numeric before doing math on it**, especially once that value originates from user input, using `is_numeric()`.

## Yoras' Mistake

Yoras writes a price checker like this and can't understand why it fails:

```php
<?php

$total = 0.1 + 0.2;
if ($total == 0.3) {
    echo "Correct total.";
} else {
    echo "Something's off.";
}
```

It prints "Something's off," even though `0.1 + 0.2` looks like it obviously equals `0.3`. This is the float precision issue described above. The actual stored value is extremely close to `0.3`, but not exactly equal to it at the level of precision PHP checks.

**Lesson:** don't test floats for exact equality. If a comparison like this is ever truly necessary, check whether the difference between the two values is smaller than a very small threshold, instead of using `==` directly.

## Take-Home Practice

1. Calculate the total cost of 3 items priced at 45.75 each, then display it using `number_format()` with two decimal places.
2. Use `is_numeric()` to check three different values: an actual number, a numeric string like `"42"`, and a non-numeric string like `"forty-two"`.
3. Try `0.1 + 0.2 == 0.3` yourself and confirm what this chapter described.

## Recap

- PHP has two everyday numeric types: int and float.
- Floats can't represent every decimal value with perfect precision, which matters most for money.
- `number_format()` formats numbers for clean display, including thousands separators.
- `round()`, `floor()`, `ceil()`, and `abs()` cover common rounding and magnitude needs.
- Never compare floats for exact equality with `==`.

Next chapter: casting, or deliberately repackaging a value from one type into another.
