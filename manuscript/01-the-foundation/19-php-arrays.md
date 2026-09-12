# Chapter 19: PHP Arrays

### The Serving Tray

---

## Back in the Kitchen

One container holds one ingredient. That's what a variable does. But a full order rarely comes as a single item. It's a tray: rice here, viand there, a drink on the side, all carried together as one unit, in a specific arrangement. PHP's answer to that is the array.

## The Concept

An **array** is a single variable that holds multiple values. PHP arrays come in two everyday flavors:

- **Indexed arrays**, where each value is automatically numbered, starting at `0`.
- **Associative arrays**, where you choose your own name (called a key) for each value, instead of a plain number.

Arrays can also be **multidimensional**, meaning an array can hold other arrays inside it, useful for representing something like an entire order made up of several items, each with their own details.

## In the Code Kitchen

**Indexed arrays**

```php
<?php

$menu = ["Adobo", "Sinigang", "Lumpia"];

echo $menu[0]; // Adobo, the first item, since counting starts at 0
echo "<br>";
echo $menu[2]; // Lumpia
echo "<br>";
echo count($menu); // 3, the total number of items
```

**Associative arrays**

```php
<?php

$dish = [
    "name" => "Sinigang",
    "price" => 180,
    "spicy" => false,
];

echo $dish["name"];  // Sinigang
echo "<br>";
echo $dish["price"]; // 180
```

**Looping through an array with `foreach`**

```php
<?php

$menu = ["Adobo", "Sinigang", "Lumpia"];

foreach ($menu as $dish) {
    echo $dish . "<br>";
}
```

For an associative array, `foreach` can hand you both the key and the value at once:

```php
<?php

$dish = ["name" => "Sinigang", "price" => 180];

foreach ($dish as $key => $value) {
    echo "$key: $value<br>";
}
```

**A multidimensional array**, an order made of several dishes

```php
<?php

$order = [
    ["name" => "Adobo", "price" => 150],
    ["name" => "Sinigang", "price" => 180],
];

foreach ($order as $item) {
    echo $item["name"] . " costs " . $item["price"] . "<br>";
}
```

**A few commonly used array functions**

```php
<?php

$menu = ["Adobo", "Sinigang"];

$menu[] = "Lumpia";        // adds a new item to the end
array_push($menu, "Lechon"); // also adds to the end, one or more items at once

sort($menu); // sorts the array alphabetically, in place

print_r($menu); // prints the whole array in a readable format, useful for debugging
```

Two more functions worth knowing early, since they come up constantly once you're comfortable with the basics: `array_map()` applies a function to every item in an array and returns a new array of the results, and `array_filter()` returns only the items that pass a given check.

```php
<?php

$prices = [100, 200, 300];

$withTax = array_map(fn($price) => $price * 1.12, $prices);
print_r($withTax); // each price increased by 12%

$expensiveOnly = array_filter($prices, fn($price) => $price > 150);
print_r($expensiveOnly); // only 200 and 300
```

## Kitchen Notes (Best Practices)

- **Use `print_r()` or `var_dump()`, not `echo`, when debugging an array.** `echo`ing an array directly produces the unhelpful word "Array" with no details.
- **Use associative arrays whenever the meaning of each value matters more than its position.** `$dish["price"]` is instantly clear. `$dish[1]` requires the reader to remember what position 1 means.
- **Remember arrays are numbered starting at 0, not 1.** This trips up nearly every beginner at least once, and is worth double-checking any time you're working with a specific index.

## Yoras' Mistake

Yoras tries to grab the third item from a three-item menu:

```php
<?php

$menu = ["Adobo", "Sinigang", "Lumpia"];
echo $menu[3]; // this does not exist
```

This produces a warning, not the third dish. The array has indexes `0`, `1`, and `2`, three items total, but no index `3`. Yoras counted the items as if numbering started at 1.

**Lesson:** the last valid index in an indexed array is always one less than the total count. For a 3-item array, the valid indexes are `0`, `1`, and `2`. `count($menu) - 1` will always give you the last valid index, no matter how many items the array holds.

## Take-Home Practice

1. Create an indexed array of four dish names, then print the second and fourth items using their correct indexes.
2. Create an associative array representing one dish, with keys for `name`, `price`, and `spicy`, then print all three values.
3. Loop through an indexed array of prices using `foreach`, and print each price after adding 12% tax to it.

## Recap

- An array is a single variable holding multiple values, either indexed by number (starting at 0) or by a chosen key (associative).
- `foreach` is the standard way to loop through an array, and can retrieve both key and value at once for associative arrays.
- `count()`, `sort()`, `array_push()`, `array_map()`, and `array_filter()` cover a large share of everyday array work.
- `print_r()` and `var_dump()`, not `echo`, are the tools for actually seeing what's inside an array.

Next chapter: superglobals, the shared pantry every part of a PHP script can reach into.
