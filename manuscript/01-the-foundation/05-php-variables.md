# Chapter 5: PHP Variables

### Labeled Containers

---

## Back in the Kitchen

Chef Jirrum points at a row of small containers on the prep shelf, each one labeled in marker: GARLIC, VINEGAR, BAY LEAF, SOY SAUCE.

"You don't cook straight from a five-kilo sack every time," he says. "You portion things out into a labeled container, so you can grab exactly what you need, when you need it, without hunting through the whole pantry. That's what a variable is."

## The Concept

A **variable** is a named container that holds a single value, which can change over time (hence "variable"). In PHP, every variable name starts with a dollar sign, followed by the name itself: `$price`, `$customerName`, `$isOpen`.

A few rules govern what a variable name is allowed to look like:

- It must start with a letter or an underscore, never a number. `$1total` is invalid; `$total1` is fine.
- After that first character, it can contain letters, numbers, and underscores.
- It's case-sensitive. `$total` and `$Total` are two separate, unrelated containers.
- PHP is a loosely typed language, meaning a variable isn't locked into holding only one kind of value forever. `$x` can hold a number today and a piece of text tomorrow. (Chapter 7 covers the actual data types a variable can hold.)

You put a value into a container using the assignment operator, `=`. This isn't a mathematical equals sign asking "are these the same?" It's an instruction: "put the value on the right into the container on the left."

## In the Code Kitchen

```php
<?php

$dishName = "Sinigang na Baboy";
$servings = 4;
$isSpicy = false;

echo $dishName;
```

Once a variable holds a value, you can use it anywhere you'd otherwise write that value directly, and you can change what it holds at any point:

```php
<?php

$total = 100;
echo $total; // 100

$total = $total + 20;
echo $total; // 120
```

That second line is worth slowing down on. PHP first looks at the right side, `$total + 20`, calculates it using the *current* value of `$total` (100), gets 120, and only then stores that result back into `$total`. The container gets relabeled with a new value. Nothing about this is mysterious once you remember `=` always means "store this," read right to left in terms of what happens first.

You can also build a new variable out of others:

```php
<?php

$firstName = "Jirrum";
$lastName = "Edica";
$fullName = $firstName . " " . $lastName;

echo $fullName; // Jirrum Edica
```

That `.` is the string concatenation operator, joining pieces of text together. It gets its own detailed look in the Strings chapter.

## Kitchen Notes (Best Practices)

- **Name variables so they explain themselves.** `$d` tells the next reader nothing. `$dishName` tells them everything, at a glance, without needing a comment.
- **Use camelCase for variable names** (`$customerName`, not `$customer_name` or `$CustomerName`). This isn't a PHP requirement, just a very common convention, and this book uses it consistently so the code reads predictably.
- **Give a variable a value before you use it.** Reading a variable that was never set produces a warning and treats the value as empty, which usually isn't what you meant, and is a common source of quiet, confusing bugs.

## Yoras' Mistake

Yoras writes this, expecting it to print `true`:

```php
<?php

$isReady = false;
if ($isReady = true) {
    echo "Yes, ready!";
}
```

It prints "Yes, ready!" every single time, no matter what `$isReady` was set to before. Yoras used a single `=`, which *assigns* `true` into `$isReady` right there inside the `if` condition, rather than checking whether it's already true. The assignment itself is treated as "successful," so the condition is always true.

**Lesson:** a single `=` assigns a value. Comparing two values for equality needs a double `==` or, better, a triple `===`, both covered in the Operators chapter. Mixing these up is one of the oldest, most common mistakes in the entire language.

## Take-Home Practice

1. Create three variables describing a dish: its name, its price, and whether it's currently available. Print all three.
2. Take a variable holding a number, add 10 to it, and store the result back into the same variable, then print it.
3. Predict, on paper, what the following prints, then run it to check yourself:
   ```php
   $a = 5;
   $b = $a;
   $a = 10;
   echo $b;
   ```

## Recap

- A variable is a named container for a value, written with a leading `$`.
- Variable names are case-sensitive and must start with a letter or underscore.
- `=` assigns a value. It does not check for equality.
- PHP is loosely typed: a variable can hold different kinds of values over its lifetime.
- Descriptive variable names are one of the cheapest ways to make code easier to read.

Next chapter: `echo` and `print`, or how you actually get a dish out to the table.
