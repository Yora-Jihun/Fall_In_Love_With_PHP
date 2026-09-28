# Chapter 12: PHP Constants

### The One Measurement That Never Changes

---

## Back in the Kitchen

Aling Nena has one rule she has never broken in twenty years: her adobo always uses a 2-to-1 ratio of soy sauce to vinegar. Not "usually." Not "roughly." Always. Change that ratio and, in her words, "hindi na 'yan adobo," it isn't adobo anymore. Some measurements in a recipe are variables. This one is a constant.

## The Concept

A **constant** is a named value that, once set, cannot be changed for the rest of the script. Where a variable is a labeled container you can refill, a constant is a label stamped permanently onto a fixed value.

PHP gives you two ways to define one:

- `define('NAME', value);` is the older, function-based way. It can be called conditionally, inside an `if` block for example, and is evaluated while the script runs.
- `const NAME = value;` is the modern, preferred syntax for most everyday use. It's evaluated earlier, before the script starts running, which makes it slightly faster and more predictable, but it can only be used at the top level of a file or inside a class, never conditionally inside an `if` or a function.

By convention, constant names are written in uppercase, with underscores between words: `TAX_RATE`, `MAX_SERVINGS`, `RESTAURANT_NAME`. This isn't enforced by PHP, but it's such a strong, universal convention that breaking it will confuse every other PHP developer who reads your code.

Constants don't use the `$` prefix that variables use, and once defined, a constant is available anywhere in the script that runs after it, without needing to be passed around like a variable would.

## In the Code Kitchen

Create a new file named `constants.php` in your `kitchen` folder, and open it at `http://kitchen.test/constants.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

```php
<?php

const TAX_RATE = 0.12;
const RESTAURANT_NAME = "Chef Jirrum's Kitchen";

echo RESTAURANT_NAME;
echo "<br>";

$subtotal = 500;
$tax = $subtotal * TAX_RATE;
echo $tax; // 60
```

Using `define()` looks like this, and is still common in real-world PHP code, especially in configuration files:

```php
<?php

define('MAX_SERVINGS', 8);
echo MAX_SERVINGS;
```

Trying to change a constant after it's defined produces an error, which is exactly the point. It's a promise to the rest of the codebase that this value will not move:

```php
<?php

const TAX_RATE = 0.12;
TAX_RATE = 0.15; // Parse error: PHP refuses to run this file at all
```

## Kitchen Notes (Best Practices)

- **Reach for `const` by default**, and only use `define()` when you specifically need conditional definition, which is rare in everyday beginner code.
- **Use constants for values that describe a fixed rule of the business**, like a tax rate, a maximum limit, or a fixed configuration value, rather than for data that naturally changes while the script runs.
- **Always write constant names in uppercase with underscores.** A lowercase constant name will still technically work, but it will look like a bug to every experienced PHP developer who reads it, since it breaks a nearly universal convention.

## Yoras' Mistake

Yoras defines a constant for the restaurant's opening hour, then later tries to "update" it for a holiday schedule:

```php
<?php

const OPENING_HOUR = 8;

// later in the same script, trying to change it for a holiday
OPENING_HOUR = 10;
```

PHP refuses to run the script at all. It stops with a parse error (an error about code that isn't valid PHP), because a constant is exactly that: constant. Yoras actually wanted a value that changes under certain conditions, which means he wanted a variable, not a constant, or a conditional check that picks a different value depending on the day.

**Lesson:** if a value needs to change during the life of the script, even occasionally, it isn't a constant. Use a variable, and add whatever conditional logic decides which value applies.

## Take-Home Practice

1. Define a constant for your kitchen's tax rate using `const`, and use it to calculate the tax on three different subtotal amounts.
2. Define a second constant using `define()` instead, and confirm both styles work the same way when you read them back.
3. Try to reassign a constant after defining it, on purpose, and read the error PHP gives you.

## Recap

- A constant holds a value that cannot change once it's set.
- `const NAME = value;` is the modern, preferred syntax for most cases. `define('NAME', value);` is older but still valid, and useful when a constant needs to be defined conditionally.
- Constant names are written in uppercase with underscores, by strong convention.
- If a value needs to change while the script runs, it belongs in a variable, not a constant.

Next chapter: magic constants, a special set of built-in values PHP fills in automatically.
