# Chapter 11: PHP Math

### The Kitchen Scale and Measuring Cups

---

## Back in the Kitchen

Chapter 9 covered numbers themselves. This chapter is about the tools you use on them: the scale, the measuring cup, the calculator sitting on the counter. PHP ships with a large set of built-in math functions, and a handful of them will show up in almost every project you ever build.

## The Concept

PHP's math functions live in the global namespace, meaning you can call them directly, with no setup required: `round()`, `abs()`, `sqrt()`, `max()`, `min()`, and more. Most take one or more numbers and return a single number.

Beyond the basics already touched on in Chapter 9 (`round()`, `floor()`, `ceil()`, `abs()`), a few more come up often enough to introduce properly here:

- `max()` and `min()` find the largest or smallest value among the arguments you give them, or among the values in an array.
- `sqrt()` returns the square root of a number.
- `pow()` raises a number to a power.
- `pi()` returns the mathematical constant π, useful for anything involving circles.
- Random number generation, for anything from a random discount to shuffling a menu.

## In the Code Kitchen

```php
<?php

echo max(10, 25, 3);   // 25
echo "<br>";
echo min(10, 25, 3);   // 3
echo "<br>";
echo sqrt(81);         // 9
echo "<br>";
echo pow(2, 5);        // 32, 2 raised to the 5th power
```

`max()` and `min()` also accept a single array of values, which becomes useful once the Arrays chapter arrives:

```php
<?php

$prices = [150, 89, 220, 65];
echo max($prices); // 220
echo "<br>";
echo min($prices); // 65
```

For randomness, PHP offers a couple of options, and which one you reach for depends on what the randomness is for:

```php
<?php

echo rand(1, 10);         // a random whole number between 1 and 10
echo "<br>";
echo random_int(1, 10);   // also a random whole number between 1 and 10
```

Both `rand()` and `random_int()` give you a random integer in a range. The difference is about how unpredictable the result needs to be. `rand()` is fine for everyday, low-stakes randomness, like picking which of today's specials to feature first on a page. `random_int()` is built for situations where the randomness has real security weight, like generating a one-time code or a password reset token, since it uses a source of randomness that's much harder to predict or guess.

## Kitchen Notes (Best Practices)

- **Use `random_int()`, not `rand()`, for anything security-sensitive**, such as tokens, codes, or anything an attacker might benefit from predicting. This is a small detail that matters a great deal the one time it matters at all.
- **Pass an array into `max()` or `min()` rather than writing out ten separate arguments by hand**, once you're working with a real collection of values.
- **Round money only at the point of display, not in the middle of a calculation**, to avoid compounding small rounding errors across multiple steps.

## Yoras' Mistake

Yoras builds a "random discount code" generator for a promotion and uses `rand()`:

```php
<?php

$discountCode = rand(1000, 9999);
echo $discountCode;
```

For a fun, low-stakes number shown once on a screen, this is genuinely fine. But when Aling Nena asks him to reuse the exact same function to generate secret password reset codes for customer accounts, that's a real problem. `rand()`'s randomness is predictable enough, under the right conditions, that it isn't considered secure for anything protecting an account.

**Lesson:** the moment randomness is protecting something (an account, a payment, a secret), switch to `random_int()`. It costs nothing extra to use and closes a real security gap.

## Take-Home Practice

1. Given a list of five prices, use `max()` and `min()` to find the highest and lowest.
2. Calculate the square root of 144 and the result of 3 raised to the power of 4.
3. Generate a random number between 1 and 100 using both `rand()` and `random_int()`, and write one sentence explaining when you'd choose each.

## Recap

- PHP's math functions, including `max()`, `min()`, `sqrt()`, `pow()`, and `pi()`, are available globally with no setup.
- `max()` and `min()` work on either a list of individual arguments or a single array.
- `rand()` is fine for everyday randomness. `random_int()` is the correct choice whenever the randomness protects something.
- Round money for display only, not mid-calculation, to avoid stacking small rounding errors.

Next chapter: constants, the one measurement in a recipe that's never allowed to change.
