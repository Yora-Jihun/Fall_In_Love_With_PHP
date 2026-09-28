# Chapter 17: PHP Loops

### Stirring Until It's Ready

---

## Back in the Kitchen

You don't stir a sauce once and call it done. You stir it continuously, checking it every so often, until it reaches the thickness you're after. That repeated motion, done until a condition is met, is exactly what a loop is.

## The Concept

PHP offers a few different loop styles, each suited to a slightly different situation:

- **`while`**: repeats a block of code as long as a condition stays `true`, checking the condition *before* each repetition.
- **`do-while`**: works like `while`, but checks the condition *after* each repetition, guaranteeing the code runs at least once, even if the condition turns out to be false immediately.
- **`for`**: repeats a block a specific, countable number of times, and is the standard choice when you already know how many repetitions you need.
- **`foreach`**: walks through every item in an array, one at a time, and is the loop you'll use most often once the Arrays chapter arrives.

Two keywords work inside any loop: `break` exits the loop immediately, and `continue` skips the rest of the current repetition and moves on to the next one.

## In the Code Kitchen

Create a new file named `loops.php` in your `kitchen` folder, and open it at `http://kitchen.test/loops.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

**`while`**

```php
<?php

$servingsLeft = 3;

while ($servingsLeft > 0) {
    echo "Plating one serving. Servings left: $servingsLeft<br>";
    $servingsLeft--;
}
```

**`for`**

```php
<?php

for ($i = 1; $i <= 3; $i++) {
    echo "Stirring the pot, stir number $i.<br>";
}
```

A `for` loop packs three parts into its parentheses: a starting point (`$i = 1`), a condition checked before each repetition (`$i <= 3`), and an action run after each repetition (`$i++`, increasing `$i` by one). This is the classic shape for "repeat exactly this many times."

**`foreach`**, previewing the Arrays chapter

```php
<?php

$menu = ["Adobo", "Sinigang", "Lumpia"];

foreach ($menu as $dish) {
    echo "Today's menu includes: $dish<br>";
}
```

`break` and `continue` in action:

```php
<?php

$orders = ["Adobo", "SOLD OUT", "Sinigang", "Lumpia"];

foreach ($orders as $order) {
    if ($order === "SOLD OUT") {
        continue; // skip this one, move to the next
    }
    echo "Preparing: $order<br>";
}
```

## Kitchen Notes (Best Practices)

- **Use `for` when you know the exact number of repetitions in advance**, and `while` when you're repeating until some condition changes, without necessarily knowing the count ahead of time.
- **Always make sure a `while` loop's condition can eventually become false.** A condition that never changes creates an infinite loop, one of the most common ways a beginner script freezes or crashes a page.
- **Reach for `foreach` whenever you're working through an array**, rather than a manual `for` loop with a counter. It's shorter, clearer, and removes an entire category of counting mistakes.

## Yoras' Mistake

Yoras writes a loop meant to count down servings, but forgets to change the variable inside the loop:

```php
<?php

$servingsLeft = 3;

while ($servingsLeft > 0) {
    echo "Still cooking...<br>";
    // forgot to decrease $servingsLeft here
}
```

This never stops. `$servingsLeft` stays at `3` forever, so the condition `$servingsLeft > 0` never becomes false, and the page hangs or crashes trying to run the loop endlessly.

**Lesson:** every `while` loop needs something inside it that actually moves the condition toward becoming false. Before running any loop, ask: "what, inside this loop, eventually makes the condition stop being true?" If you can't answer that, the loop isn't finished yet.

## Take-Home Practice

1. Write a `for` loop that prints "Preparing dish #1" through "Preparing dish #5."
2. Write a `while` loop that counts down from 5 to 1, printing each number.
3. Write a `foreach` loop over a small list of three dish names, using `continue` to skip one specific dish by name.

## Recap

- `while` checks its condition before each repetition. `do-while` checks after, guaranteeing at least one run.
- `for` is the standard choice for a known, fixed number of repetitions.
- `foreach` walks through every item in an array, and will be your most-used loop once arrays are introduced.
- `break` exits a loop early. `continue` skips to the next repetition.
- Every loop needs something inside it that can eventually make its condition false, or it never ends.

Next chapter: functions, or how a set of steps becomes a reusable recipe card.
