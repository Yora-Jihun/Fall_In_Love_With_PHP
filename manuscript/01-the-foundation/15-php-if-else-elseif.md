# Chapter 15: PHP If, Else, and Elseif

### Tasting the Dish

---

## Back in the Kitchen

A good cook tastes constantly. Too sour, add a little sugar. Too bland, add salt. Just right, plate it and serve. Every one of those decisions follows the same shape: check something, then act differently depending on what you find. That shape has a name in PHP: the `if` statement.

## The Concept

An `if` statement runs a block of code only when a given condition is `true`. You can extend it with `else`, which runs when the condition is `false`, and `elseif`, which lets you check additional conditions in sequence if the first one didn't match.

```php
if (condition) {
    // runs if condition is true
} elseif (anotherCondition) {
    // runs if the first condition was false, but this one is true
} else {
    // runs if none of the above conditions were true
}
```

PHP checks conditions from top to bottom, and stops at the first one that matches. If none match, and there's an `else`, that final block runs. `elseif` and `else` are both optional. A plain `if` with nothing else is completely valid on its own.

## In the Code Kitchen

Create a new file named `if-else.php` in your `kitchen` folder, and open it at `http://kitchen.test/if-else.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

```php
<?php

$servings = 2;

if ($servings <= 0) {
    echo "Invalid order.";
} elseif ($servings === 1) {
    echo "Solo meal, coming right up.";
} elseif ($servings <= 4) {
    echo "Good for sharing.";
} else {
    echo "That's a party order!";
}
```

With `$servings` set to `2`, PHP checks each condition in order: `$servings <= 0` is false, `$servings === 1` is false, `$servings <= 4` is true, so that block runs, and the rest are skipped entirely, even if they would also have matched.

You can nest `if` statements inside each other, though it's worth keeping this shallow for readability:

```php
<?php

$isOpen = true;
$hasIngredient = false;

if ($isOpen) {
    if ($hasIngredient) {
        echo "We can make that dish today.";
    } else {
        echo "Sorry, we're out of an ingredient for that today.";
    }
} else {
    echo "We're closed right now.";
}
```

That same logic often reads more cleanly by combining conditions with `&&`, from the last chapter, instead of nesting:

```php
<?php

if ($isOpen && $hasIngredient) {
    echo "We can make that dish today.";
}
```

## Kitchen Notes (Best Practices)

- **Keep conditions simple and readable.** If a single `if` line is getting hard to read at a glance, consider storing part of the logic in a well-named variable first, like `$canServeDish = $isOpen && $hasIngredient;`, then checking that variable in the `if`.
- **Avoid deeply nested `if` blocks** where possible. Three or four levels deep is genuinely hard for anyone, including you later, to follow. Combining conditions or restructuring the logic usually flattens this out.
- **Always use `===` inside conditions**, following the recommendation from the last chapter, unless there's a specific reason to allow loose comparison.

## Yoras' Mistake

Yoras writes this to check whether an order quantity is exactly one:

```php
<?php

$quantity = 1;

if ($quantity = 2) {
    echo "Ordering two.";
} else {
    echo "Ordering something else.";
}
```

This always prints "Ordering two," no matter what `$quantity` originally held. This is the single `=` mistake from Chapter 5, showing up again here. `$quantity = 2` *assigns* `2`, and an assignment is treated as successful (and therefore truthy), so the `if` block always runs.

**Lesson:** always double-check that a condition uses `==` or, better, `===`, never a single `=`. A good habit some developers use to catch this automatically: writing the constant or fixed value first, like `2 === $quantity`, which causes an immediate error if you accidentally type a single `=`, since you can't assign a value into a plain number.

## Take-Home Practice

1. Write an `if`/`elseif`/`else` chain that labels a dish's spice level as "mild," "medium," or "spicy" based on a numeric value.
2. Combine two conditions with `&&` to decide whether an order qualifies for free delivery (for example, order total above a minimum, and within a certain distance).
3. Deliberately write the single `=` mistake inside an `if`, observe the incorrect behavior, then fix it.

## Recap

- `if` runs a block only when its condition is `true`. `elseif` checks additional conditions if earlier ones failed. `else` catches everything else.
- PHP checks conditions top to bottom and stops at the first match.
- Combining conditions with `&&` or `||` is often clearer than deeply nested `if` blocks.
- A single `=` inside a condition assigns a value instead of comparing one, a classic and easy mistake to make.

Next chapter: `switch`, a cleaner way to check one value against many possibilities, and its modern alternative, `match`.
