# Chapter 16: PHP Switch

### One Ingredient, Many Possible Dishes

---

## Back in the Kitchen

A long chain of `elseif` statements, all checking the exact same variable against different possible values, starts to look messy fast. PHP offers a cleaner shape for exactly that situation: `switch`.

## The Concept

A `switch` statement checks one value against a list of possible matches, called `case`s, and runs the code under whichever `case` matches. An optional `default` case runs if nothing else matched.

```php
switch (value) {
    case option1:
        // runs if value matches option1
        break;
    case option2:
        // runs if value matches option2
        break;
    default:
        // runs if nothing else matched
}
```

The `break` at the end of each case matters more than it looks. Without it, PHP keeps running the code in the *next* case too, a behavior called "fall-through." Sometimes fall-through is intentional and useful. Far more often, forgetting `break` is an accident that produces confusing results.

PHP also has a more modern alternative, the `match` expression, introduced in PHP 8.0. It fixes both of `switch`'s sharpest edges: it never falls through, and it compares strictly (like `===`) rather than loosely, and it can hand back a value directly, rather than only running code as a side effect.

## In the Code Kitchen

**Classic `switch`**

```php
<?php

$day = "Friday";

switch ($day) {
    case "Monday":
        echo "Monggo beans today.";
        break;
    case "Friday":
        echo "Fish is on the menu.";
        break;
    default:
        echo "Check today's board for the special.";
}
```

**Fall-through, on purpose**

```php
<?php

$day = "Saturday";

switch ($day) {
    case "Saturday":
    case "Sunday":
        echo "Weekend hours: open until midnight.";
        break;
    default:
        echo "Weekday hours: open until 10 PM.";
}
```

Here, `case "Saturday"` has no `break` of its own, so it deliberately falls through into `case "Sunday"`'s code. Both days share the same result, written once.

**The modern `match` expression**

```php
<?php

$day = "Friday";

$menuNote = match ($day) {
    "Monday" => "Monggo beans today.",
    "Friday" => "Fish is on the menu.",
    "Saturday", "Sunday" => "Weekend hours: open until midnight.",
    default => "Check today's board for the special.",
};

echo $menuNote;
```

Notice `match` uses commas to group multiple values under one result (`"Saturday", "Sunday"`), rather than relying on fall-through, and it directly produces a value you can store in a variable, rather than only running `echo` as a side effect inside each branch.

## Kitchen Notes (Best Practices)

- **Prefer `match` over `switch` in modern PHP**, whenever you're simply mapping one value to a corresponding result. It's shorter, it compares strictly by default (avoiding the `==` pitfalls from Chapter 14), and it can't accidentally fall through.
- **If you do use `switch`, never forget the `break`** at the end of each case, unless fall-through is exactly what you intend, and in that case, add a short comment saying so, since it looks like a mistake otherwise.
- **Always include a `default` case (or `default =>` in `match`)**, so an unexpected value has a defined, predictable outcome instead of silently doing nothing.

## Yoras' Mistake

Yoras writes a `switch` to categorize a dish's spice level, and forgets a `break`:

```php
<?php

$spiceLevel = "mild";

switch ($spiceLevel) {
    case "mild":
        echo "Kid-friendly. ";
    case "medium":
        echo "A little kick. ";
        break;
    case "spicy":
        echo "Not for the faint of heart.";
        break;
}
```

With `$spiceLevel` set to `"mild"`, this prints both "Kid-friendly." and "A little kick.", because execution fell straight through from the first case into the second, since there was no `break` stopping it.

**Lesson:** every `case` needs a `break`, unless you specifically want fall-through, and even then, it's worth adding a comment to make that intention obvious. This exact class of mistake is a large part of why `match` has become the preferred modern choice.

## Take-Home Practice

1. Write a `switch` statement that prints a different greeting depending on the time of day (morning, afternoon, evening), including a `default` case.
2. Rewrite the same logic using `match` instead, and compare how the two versions read.
3. Deliberately remove a `break` from a working `switch` statement, observe the fall-through behavior, then restore it.

## Recap

- `switch` compares one value against multiple `case` options, and needs `break` at the end of each case to avoid unintended fall-through.
- `match`, introduced in PHP 8.0, is the modern alternative: no fall-through, strict comparison by default, and it produces a value directly.
- Prefer `match` for simple value-to-result mapping in modern PHP code.
- Always include a `default` case so unexpected values have a defined outcome.

Next chapter: loops, or how a kitchen repeats a motion until the job is done.
