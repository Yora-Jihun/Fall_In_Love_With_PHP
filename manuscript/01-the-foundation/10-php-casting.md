# Chapter 10: PHP Casting

### Repackaging an Ingredient

---

## Back in the Kitchen

Aling Nena has been cooking for twenty years, and she has a habit: she never checks what container something is already in. Rice goes in whatever bowl is closest, sauce goes in whatever cup is nearby, and somehow, most of the time, it works out.

"Most of the time" is doing a lot of work in that sentence.

## The Concept

**Casting** means deliberately converting a value from one type into another, on purpose, so you know exactly what you're working with. PHP does some of this automatically behind the scenes, called **type juggling**, but relying on that silently is exactly the kind of habit that eventually causes a confusing bug. Casting explicitly is the disciplined version of the same idea: "measure, don't eyeball it."

To cast a value, you write the target type in parentheses directly before it:

- `(int)` converts to an integer.
- `(float)` converts to a float.
- `(string)` converts to a string.
- `(bool)` converts to a boolean.
- `(array)` converts to an array.

PHP also does this automatically in many situations. If you write `"5" + 3`, PHP converts the string `"5"` into the number `5` before adding, giving you `8`. This automatic behavior is convenient, but it's also exactly why explicit casting matters: when you cast on purpose, anyone reading your code, including future you, knows precisely what type is intended at that point, instead of having to trust PHP's automatic guesswork.

## In the Code Kitchen

```php
<?php

$quantityInput = "4"; // this arrived as a string, perhaps from a form
$quantity = (int) $quantityInput;

var_dump($quantityInput); // string(1) "4"
var_dump($quantity);      // int(4)
```

Casting to a string works the other direction just as easily:

```php
<?php

$price = 149.5;
$priceAsText = (string) $price;

var_dump($priceAsText); // string(5) "149.5"
```

Casting to a boolean follows PHP's "truthy and falsy" rules, the same ones from Chapter 7:

```php
<?php

var_dump((bool) "");     // false, an empty string
var_dump((bool) "0");    // false, the string "0" specifically
var_dump((bool) "0.0");  // true, this string is not falsy, unlike "0"
var_dump((bool) 0);      // false
var_dump((bool) 1);      // true
var_dump((bool) "hello"); // true, any other non-empty string
```

That third example is worth remembering. `"0"` is one of the few strings PHP treats as falsy, but `"0.0"` is not on that short list. It's a small, sharp edge in the language, and knowing about it now saves confusion later.

An alternative to casting is `settype()`, which changes a variable's type in place, rather than producing a new value:

```php
<?php

$count = "10";
settype($count, "integer");

var_dump($count); // int(10)
```

## Kitchen Notes (Best Practices)

- **Cast explicitly whenever a value's type genuinely matters**, especially right after receiving input from a form, a file, or anywhere outside your own code. Forms are covered soon, and this habit starts paying off immediately once you get there.
- **Prefer casting (`(int) $value`) over `settype()` for most everyday use.** Casting produces a new value without changing the original variable's identity, which tends to read more clearly in typical code.
- **Learn PHP's specific falsy values by heart**: `false`, `0`, `0.0`, `""`, `"0"`, `null`, and an empty array. Everything else counts as truthy, including the string `"0.0"` and the string `" "` (a single space).

## Yoras' Mistake

Yoras collects a quantity from a form (covered properly later in this book), and writes:

```php
<?php

$quantity = "3"; // arrived as a string
$total = $quantity + $quantity;

echo $total; // 6, this actually works fine
```

That one works, thanks to automatic type juggling. But then he tries this:

```php
<?php

$quantity = "3 items";
$total = $quantity + 2;

echo $total; // 5, with a warning, not an error
```

PHP pulls the leading numeric portion, `3`, out of the string and ignores the rest, producing `5`, but also raises a warning about the non-numeric text it discarded. This "mostly works" quality is exactly the danger. It hides a data problem instead of surfacing it clearly.

**Lesson:** don't trust automatic type juggling with input you didn't fully control yourself. Validate with `is_numeric()` first, then cast explicitly with `(int)` or `(float)`, so bad data gets caught instead of silently mangled.

## Take-Home Practice

1. Take a string that looks like a number, `"25"`, cast it to an integer, and confirm the type with `var_dump()`.
2. Test the boolean cast of `"0"`, `"0.0"`, and `" "` (a single space), and confirm which ones are truthy.
3. Reproduce Yoras' `"3 items"` example, observe the warning, then fix it by validating with `is_numeric()` before doing any math.

## Recap

- Casting explicitly converts a value's type on purpose, using `(int)`, `(float)`, `(string)`, `(bool)`, or `(array)`.
- PHP also performs automatic type juggling, which is convenient but can hide data problems.
- `"0"` is falsy. `"0.0"` and `" "` are truthy. This distinction is worth memorizing.
- Validate with `is_numeric()` before casting untrusted input to a number, rather than trusting automatic conversion alone.

Next chapter: math functions, the kitchen scale and measuring cups of PHP.
