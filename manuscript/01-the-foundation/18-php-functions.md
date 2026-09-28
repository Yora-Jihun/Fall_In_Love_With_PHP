# Chapter 18: PHP Functions

### The Recipe Card

---

## Back in the Kitchen

Chef Jirrum doesn't re-explain how to make rice every single time it's needed for a dish. He wrote the steps once, on a card labeled "Steamed Rice," and now anyone in the kitchen can follow that card whenever rice is needed, without reinventing it from scratch each time. That reusable card is a function.

## The Concept

A **function** is a named, reusable block of code that performs a specific task. You define it once, and you can call it, meaning run it, as many times as you need, from anywhere in your script.

```php
function functionName($parameter1, $parameter2) {
    // code that runs when the function is called
    return $result; // optional: sends a value back to whoever called it
}
```

- **Parameters** are the inputs a function expects, listed in its parentheses when it's defined.
- **Arguments** are the actual values you pass in when you call the function.
- **`return`** sends a value back out of the function, and immediately stops the function from running any further.

A function that doesn't `return` anything simply finishes after its last line runs, and hands back `null` implicitly.

Modern PHP lets you specify the type of each parameter, and the type of value the function returns, which is exactly the "measure, don't eyeball it" discipline from earlier chapters, made concrete:

```php
function calculateTotal(int $quantity, float $unitPrice): float {
    return $quantity * $unitPrice;
}
```

## In the Code Kitchen

Create a new file named `functions-practice.php` in your `kitchen` folder, and open it at `http://kitchen.test/functions-practice.php`. Type each example below into that file, one at a time. Save the file (Ctrl+S, or Cmd+S on a Mac) before you refresh the page, or the browser will still show the old version.

```php
<?php

function calculateTotal(int $quantity, float $unitPrice): float {
    return $quantity * $unitPrice;
}

$total = calculateTotal(3, 65.50);
echo $total; // 196.5
```

**Default parameter values**, useful when a value is usually the same but occasionally needs to change:

```php
<?php

function applyDiscount(float $price, float $discountRate = 0.10): float {
    return $price - ($price * $discountRate);
}

echo applyDiscount(200);       // uses the default 10% discount
echo "<br>";
echo applyDiscount(200, 0.25); // overrides it with a 25% discount
```

**Named arguments**, a modern PHP feature that lets you specify which parameter you're setting by name, useful when a function has several parameters and you want the call itself to read clearly:

```php
<?php

echo applyDiscount(price: 200, discountRate: 0.25);
```

**Arrow functions**, a compact syntax for very short, single-expression functions, common when passing a small function into another function (a pattern covered fully in the Callback Functions chapter):

```php
<?php

$double = fn(int $n): int => $n * 2;
echo $double(21); // 42
```

**Variable scope**: a variable created inside a function only exists inside that function. It has no effect on, and no access to, a variable of the same name outside it:

```php
<?php

$total = 100; // outside the function

function showTotal() {
    $total = 50; // a completely different, separate $total, local to this function
    echo $total; // 50
}

showTotal();
echo $total; // still 100, completely unaffected
```

## Kitchen Notes (Best Practices)

- **Give every function a single, clear job, and a name that describes exactly that job.** `calculateTotal()` is a good name. `doStuff()` tells the next reader nothing.
- **Type your parameters and return values once you're comfortable with the basics.** It catches entire categories of mistakes before the code even runs, and makes a function's contract obvious without reading its internals.
- **Avoid relying on variables from outside a function unless they're explicitly passed in as parameters.** A function that only depends on its own parameters is far easier to test, reuse, and reason about than one that reaches out for variables sitting elsewhere in the script.

## Yoras' Mistake

Yoras writes a function expecting it to update a variable declared outside it:

```php
<?php

$total = 0;

function addToTotal($amount) {
    $total = $total + $amount; // this is a brand new, local $total
    echo $total;
}

addToTotal(50); // prints 50
echo $total;     // still 0, the outer $total was never touched
```

Yoras expected the outer `$total` to become `50`. Instead, the function created its own separate, local `$total`, used it, and then it disappeared entirely once the function finished. The outer `$total` was never involved.

**Lesson:** a function can't see or change an outside variable unless that variable is explicitly passed in as a parameter, or explicitly returned and reassigned by the caller. The fix here is to return the new value and store it yourself:

```php
<?php

function addToTotal($currentTotal, $amount) {
    return $currentTotal + $amount;
}

$total = 0;
$total = addToTotal($total, 50);
echo $total; // 50, correctly updated
```

## Take-Home Practice

1. Write a function `calculateTax(float $amount, float $rate): float` that returns the tax on a given amount, and call it with a couple of different values.
2. Give a function a default parameter value, then call it once using the default and once overriding it.
3. Write a short arrow function that checks whether a number is even, and test it against a few numbers.

## Recap

- A function is a named, reusable block of code, defined once and called as many times as needed.
- Parameters are a function's expected inputs. Arguments are the actual values passed in when calling it.
- `return` sends a value back and immediately ends the function.
- A variable created inside a function is local to that function and cannot be seen or changed from outside it.
- Modern PHP supports typed parameters and return types, default values, named arguments, and short arrow functions.

Next chapter: arrays, the tray that lets one variable hold many ingredients at once.
