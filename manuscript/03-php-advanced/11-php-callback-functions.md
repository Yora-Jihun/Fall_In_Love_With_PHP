# Chapter 37: PHP Callback Functions

### "When You Finish That, Do This Next"

---

## Back in the Kitchen

Chef Jirrum hands a tray to another cook and says, "when you finish plating this, garnish it with the herbs on the counter." He isn't garnishing it himself, right now. He's handing off a specific instruction, to be carried out later, by whoever ends up holding the tray. In PHP, a function can be handed off exactly the same way, as a value, to be called later by something else.

## The Concept

A **callback** is a function passed into another function, to be called at some point during that function's own work. This is possible because PHP treats functions as values that can be stored, passed around, and called indirectly, not just written and called directly by name.

You've already been using this idea without the formal name. Back in the Arrays chapter, `array_map()` and `array_filter()` both accepted a small function as one of their arguments. This chapter looks at that pattern properly, along with the different ways PHP lets you write a callback:

- **A named function**, passed by writing its name as a string, or in modern PHP, using the function's name directly (its "first-class callable" form).
- **An anonymous function**, also called a closure, written inline where it's needed, with `function(...) { ... }`.
- **An arrow function**, the compact `fn(...) => ...` syntax from Chapter 18, ideal for a short, single-expression callback.

## In the Code Kitchen

**Passing a named function**

```php
<?php

function isSpicy(string $dish): bool {
    return str_contains(strtolower($dish), "sisig") || str_contains(strtolower($dish), "bicol");
}

$menu = ["Adobo", "Bicol Express", "Sinigang", "Sisig"];

$spicyDishes = array_filter($menu, isSpicy(...)); // first-class callable syntax
print_r($spicyDishes);
```

**Using an anonymous function (closure), including `use` to capture an outside variable**

```php
<?php

$taxRate = 0.12;

$prices = [100, 200, 300];

$withTax = array_map(function ($price) use ($taxRate) {
    return $price * (1 + $taxRate);
}, $prices);

print_r($withTax);
```

The `use ($taxRate)` part matters. Without it, the anonymous function has no access at all to `$taxRate` from outside itself, following the same scoping rule from Chapter 18: a function normally can't see variables from the code around it, unless they're explicitly handed in. `use` is how a closure explicitly captures specific outside variables.

**The same thing with an arrow function**, which automatically captures outside variables, without needing `use`

```php
<?php

$taxRate = 0.12;
$prices = [100, 200, 300];

$withTax = array_map(fn($price) => $price * (1 + $taxRate), $prices);
print_r($withTax);
```

**A custom sort, using `usort()` with a callback that defines the comparison**

```php
<?php

$menu = [
    ["name" => "Adobo", "price" => 150],
    ["name" => "Lumpia", "price" => 90],
    ["name" => "Sinigang", "price" => 180],
];

usort($menu, fn($a, $b) => $a["price"] <=> $b["price"]);

foreach ($menu as $dish) {
    echo $dish["name"] . ": " . $dish["price"] . "<br>";
}
```

That `<=>` is the "spaceship operator" from Chapter 14's operator overview, returning `-1`, `0`, or `1` depending on whether the left side is less than, equal to, or greater than the right side, exactly the shape `usort()` expects from its comparison callback.

## Kitchen Notes (Best Practices)

- **Prefer arrow functions for short, single-expression callbacks.** They're compact and automatically capture outside variables, which covers the majority of everyday cases like the examples in this chapter.
- **Reach for a full anonymous function with `use`, or a named function, once the callback's logic needs more than one line**, or when reusing the exact same logic in more than one place makes a named function clearer.
- **Type-hint a callback parameter as `callable` when you write your own function that accepts one**, so it's clear from the function's own signature that a function is expected as an argument, not just any ordinary value.

## Yoras' Mistake

Yoras writes a closure meant to apply a discount, but forgets `use`:

```php
<?php

$discountRate = 0.10;

$applyDiscount = function ($price) {
    return $price - ($price * $discountRate); // $discountRate is not visible here
};

echo $applyDiscount(100);
```

This produces an error, since `$discountRate` doesn't exist inside the closure at all. A closure, unlike an arrow function, does not automatically see variables from the surrounding code. It only sees what's explicitly passed to it as a parameter, or explicitly captured with `use`.

**Lesson:** an anonymous function needs `use ($variable)` to reach outside its own body for a variable from the surrounding code. Arrow functions handle this automatically, which is exactly why they're the more convenient default for short callbacks.

## Take-Home Practice

1. Use `array_filter()` with an arrow function to select only dishes priced under 150 from a list.
2. Write an anonymous function that adds a fixed delivery fee to a price, capturing the fee amount with `use`, then apply it with `array_map()`.
3. Use `usort()` to sort a list of dish names alphabetically, using the spaceship operator in your comparison callback.

## Recap

- A callback is a function passed into another function, to be called later, made possible because PHP treats functions as values.
- Named functions, anonymous functions (closures), and arrow functions are the three common ways to write one.
- A closure needs `use ($variable)` to access an outside variable. An arrow function captures outside variables automatically.
- `usort()` and similar functions rely on a callback that returns a negative number, zero, or a positive number to indicate ordering, a job the spaceship operator (`<=>`) is built for.

Next chapter: JSON, a standardized format any kitchen, not just this one, can read.
