# Chapter 7: PHP Data Types

### Kinds of Ingredients

---

## Back in the Kitchen

Flour and water are both ingredients, but you'd never treat them the same way. One you measure by weight, the other by volume. One you can knead, the other you can't. Knowing what kind of ingredient you're holding changes what you're allowed to do with it. The same is true for the values a variable can hold.

## The Concept

PHP recognizes several core data types. The ones you'll use constantly, starting now, are:

- **string**: text, wrapped in quotes. `"Adobo"`, `'Sinigang'`.
- **int** (integer): a whole number, positive or negative, no decimal point. `4`, `-12`, `0`.
- **float** (also called double): a number with a decimal point. `19.99`, `-0.5`.
- **bool** (boolean): exactly one of two values, `true` or `false`. Used for yes-or-no, on-or-off decisions.
- **array**: a collection of multiple values stored in one variable. Its own full chapter is coming soon.

Two more you'll meet less often at first, but should recognize:

- **null**: a special value meaning "no value at all." Not zero, not an empty string. Genuinely nothing.
- **object**: an instance of a class, the foundation of object-oriented PHP, a more advanced topic you'll meet after this book.

PHP is a **loosely typed** language. You don't have to declare, up front, "this variable will only ever hold a string." A variable's type is decided automatically, based on whatever value you put into it, and it can change if you put something else in later. This is convenient for quick scripts, and it's exactly why the "measure, don't eyeball it" habit this book teaches (type-safe function signatures, `declare(strict_types=1)`, and so on) matters more, not less, as your code grows. Loose typing gives you freedom. Discipline is what keeps that freedom from turning into confusion.

## In the Code Kitchen

Create a new file named `data-types.php` in your `kitchen` folder, and open it at `http://kitchen.test/data-types.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

You can check any variable's current type with `gettype()`, and inspect its full value and type together with `var_dump()`:

```php
<?php

$dishName = "Adobo";
$servings = 4;
$price = 149.50;
$isAvailable = true;

echo gettype($dishName);    // string
echo "<br>";
echo gettype($servings);    // integer
echo "<br>";
echo gettype($price);       // double
echo "<br>";
echo gettype($isAvailable); // boolean
```

`var_dump()` is even more useful while learning, since it shows both the type and the value at once:

```php
<?php

$price = 149.50;
var_dump($price); // float(149.5)
```

You can check for a specific type using functions like `is_string()`, `is_int()`, `is_float()`, `is_bool()`, and `is_array()`, each returning `true` or `false`:

```php
<?php

$servings = 4;

if (is_int($servings)) {
    echo "Yes, this is a whole number.";
}
```

## Kitchen Notes (Best Practices)

- **Use `var_dump()` while debugging, not `echo`, when you're unsure what a variable actually contains.** `echo` shows you the value but hides the type, and the type is often exactly the thing causing confusion.
- **Don't rely on PHP silently converting types for you in important logic.** It's tempting to compare a string and a number and let PHP figure it out, but that's exactly the kind of habit that causes subtle bugs. The Casting chapter covers this directly.
- **Match your variable names to what they hold.** A variable named `$count` should hold an integer, not sometimes a string like `"4 items"`. Consistency here prevents entire categories of bugs before they happen.

## Yoras' Mistake

Yoras writes this and is confused why it behaves like a "yes" instead of a "no":

```php
<?php

$isOpen = "false";
if ($isOpen) {
    echo "The kitchen is open.";
}
```

This prints "The kitchen is open," even though it looks like it says the opposite. The problem: `"false"` here is a **string**, not the boolean `false`. In PHP, any non-empty string, including the word `"false"`, is treated as truthy in a condition. Only the actual boolean `false` (no quotes), the number `0`, an empty string `""`, `null`, and a few other specific "empty" values are treated as falsy.

**Lesson:** boolean values are written without quotes, `true` and `false`, not `"true"` and `"false"`. A string that merely *looks* like a boolean is still just text to PHP.

## Take-Home Practice

1. Create one variable of each core type covered in this chapter (string, int, float, bool), and print each one's type using `gettype()`.
2. Use `var_dump()` on a float and observe exactly how PHP displays it.
3. Predict, then test, whether `if ("0")` and `if ("false")` behave the same way in PHP. (They don't. Find out why.)

## Recap

- PHP's core data types include string, int, float, bool, array, object, and null.
- PHP is loosely typed: a variable's type is inferred from its value and can change.
- `gettype()` reports a variable's current type. `var_dump()` reports both type and value.
- A string that looks like a boolean, such as `"false"`, is still just a truthy string in a condition, since only the real boolean `false` and a small set of other falsy values behave as false.

Next chapter: strings, the most commonly used data type, get a full chapter of their own.
