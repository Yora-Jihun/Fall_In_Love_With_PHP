# Chapter 39: PHP Exceptions

### When Something in the Kitchen Goes Wrong

---

## Back in the Kitchen

Something burns. A dish gets dropped. An ingredient turns out to have gone bad right as you're about to use it. A real kitchen doesn't grind to a total halt over every mishap, but it also doesn't just pretend nothing happened and keep serving a ruined dish. It stops, deals with the specific problem, and either recovers or clearly tells someone that this particular dish can't go out. That's what exceptions are for.

## The Concept

An **exception** is PHP's structured way of signaling that something went wrong, at the exact moment it went wrong, and handing control to code specifically written to deal with that kind of problem.

- **`throw`** raises an exception, immediately stopping normal execution at that point.
- **`try`** wraps a block of code that might throw an exception.
- **`catch`** defines what to do if a specific type of exception was thrown inside the `try` block.
- **`finally`** defines code that runs no matter what happened, whether an exception was thrown or not, commonly used for cleanup, like closing a file handle from the File Handling chapter.

PHP's built-in `Exception` class covers most everyday needs, but you can also create your own custom exception types by extending it. This uses a feature of classes called inheritance. You don't need to understand classes yet to follow the example below. Just copy its shape.

## In the Code Kitchen

Create a new file named `exceptions.php` in your `kitchen` folder, and open it at `http://kitchen.test/exceptions.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

**Basic try, throw, catch**

```php
<?php

function calculateServingSize(int $totalRice, int $numberOfGuests): float {
    if ($numberOfGuests <= 0) {
        throw new Exception("Number of guests must be greater than zero.");
    }
    return $totalRice / $numberOfGuests;
}

try {
    $serving = calculateServingSize(1000, 0);
    echo $serving;
} catch (Exception $e) {
    echo "Could not calculate serving size: " . htmlspecialchars($e->getMessage());
}
```

Without the `try`/`catch`, that `throw` would crash the script entirely with an uncaught error. With it, the problem is handled gracefully, and the rest of the page can continue running normally.

**`finally`, guaranteed cleanup**

```php
<?php

$handle = fopen(__DIR__ . "/order-log.txt", "a");

try {
    if (!$handle) {
        throw new Exception("Could not open the log file.");
    }
    fwrite($handle, "Order logged.\n");
} catch (Exception $e) {
    echo "Logging failed: " . htmlspecialchars($e->getMessage());
} finally {
    if ($handle) {
        fclose($handle);
    }
}
```

The `finally` block runs whether the `try` succeeded or the `catch` caught a problem, making it the reliable place to put cleanup code, like closing a file, that absolutely must happen either way.

**A custom exception**, extending PHP's built-in one

```php
<?php

class OutOfStockException extends Exception {
}

function orderDish(string $dish, bool $inStock): string {
    if (!$inStock) {
        throw new OutOfStockException("$dish is currently out of stock.");
    }
    return "$dish confirmed.";
}

try {
    echo orderDish("Sisig", false);
} catch (OutOfStockException $e) {
    echo "Sorry: " . htmlspecialchars($e->getMessage());
}
```

Custom exception classes let you `catch` different kinds of problems differently, rather than lumping every possible failure into one generic `Exception`. A real application might catch `OutOfStockException` one way (suggest an alternative dish) and a different exception type another way entirely (log the error and show a generic apology).

## Kitchen Notes (Best Practices)

- **Throw an exception for a genuinely exceptional situation**, something that prevents the normal, expected flow of the code from continuing, not for routine, expected outcomes like "no search results found," which is usually better handled with a plain conditional check.
- **Catch the most specific exception type that makes sense**, rather than a broad, generic `Exception` everywhere, once your code defines its own exception types. This lets different problems be handled appropriately, instead of identically.
- **Never silently swallow an exception with an empty `catch` block.** At the very least, log what happened. A caught exception that vanishes without a trace is often harder to debug than if it had never been caught at all.
- **Use `finally` for cleanup that must always happen**, like closing a file or a resource, regardless of whether the operation succeeded.

## Yoras' Mistake

Yoras catches an exception, but does nothing meaningful with it. (This uses the `calculateServingSize()` function from the first example, so keep that function in the file if you try it.)

```php
<?php

try {
    $serving = calculateServingSize(1000, 0);
} catch (Exception $e) {
    // seems handled, right?
}

echo $serving; // Warning: $serving was never actually set
```

The exception is caught, so the script doesn't crash outright, but nothing about the underlying problem was actually addressed. `$serving` was never assigned, since the function threw before it could return a value, and the very next line tries to use a variable that doesn't exist.

**Lesson:** catching an exception is only half the job. The `catch` block needs to actually do something reasonable: show a clear message, provide a fallback value, or stop the surrounding logic from continuing as if nothing happened. An empty or near-empty `catch` block is rarely the right answer.

## Take-Home Practice

1. Write a function that throws an exception if a discount percentage is outside the range 0 to 100, and call it inside a `try`/`catch` with both a valid and an invalid value.
2. Create a custom exception class, `InvalidOrderException`, and use it in place of the generic `Exception` in one of your own functions.
3. Add a `finally` block to a `try`/`catch` that always prints "Order processing complete," regardless of whether an exception was thrown.

## Recap

- `throw` raises an exception. `try` wraps code that might fail. `catch` handles a specific exception type. `finally` always runs, success or failure.
- PHP's built-in `Exception` class covers most needs, and can be extended to create custom, more specific exception types.
- Reserve exceptions for genuinely exceptional situations, not routine, expected outcomes.
- Never leave a `catch` block empty. Handling an exception means actually doing something about it.

This closes out **Part 3: PHP Advanced**, and with it, this book. You started with a single `echo` and now know how to handle forms, files, cookies, sessions, and what to do when something goes wrong. When you're ready for the next step, look into object-oriented programming (OOP), a way of organizing bigger projects around classes and objects. Until then, keep cooking.
