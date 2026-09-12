# Chapter 38: PHP JSON

### A Recipe Card Any Kitchen Can Read

---

## Back in the Kitchen

A recipe written in one kitchen's private shorthand is useless handed to a completely different kitchen. But a recipe written in a standard, universally understood format, clear ingredient lists, clear steps, can be read and cooked by anyone, anywhere, regardless of what kitchen wrote it. JSON is that standard format, but for data instead of food.

## The Concept

**JSON** (JavaScript Object Notation) is a lightweight, text-based format for representing structured data, built from just a few simple shapes: objects (key-value pairs, wrapped in `{ }`), arrays (ordered lists, wrapped in `[ ]`), strings, numbers, booleans, and `null`. Despite the name, it's used far beyond JavaScript. It's the de facto standard format for web APIs, configuration files, and data exchange between completely different systems and programming languages, precisely because nearly every language, PHP included, can read and write it.

PHP gives you two core functions:

- **`json_encode($value)`** converts a PHP array (or object) into a JSON string.
- **`json_decode($jsonString, $associative)`** converts a JSON string back into PHP data. Passing `true` as the second argument returns associative arrays, matching the array style from Chapter 19. Leaving it as `false` (the default) returns generic PHP objects instead.

## In the Code Kitchen

**Encoding PHP data into JSON**

```php
<?php

$dish = [
    "name" => "Sinigang",
    "price" => 180,
    "spicy" => false,
    "tags" => ["sour", "soup"],
];

$json = json_encode($dish);
echo $json;
// {"name":"Sinigang","price":180,"spicy":false,"tags":["sour","soup"]}
```

For readable, human-friendly output, useful while developing or debugging, add the `JSON_PRETTY_PRINT` flag:

```php
<?php

echo json_encode($dish, JSON_PRETTY_PRINT);
```

**Decoding JSON back into PHP**

```php
<?php

$json = '{"name":"Sinigang","price":180,"spicy":false}';

$dish = json_decode($json, true); // true = return an associative array

echo $dish["name"];  // Sinigang
echo "<br>";
echo $dish["price"]; // 180
```

**Checking for a decoding error**

`json_decode()` returns `null` both when the JSON is genuinely the value `null`, and when the JSON string is malformed and couldn't be parsed at all. To tell these apart reliably, check `json_last_error()`:

```php
<?php

$json = '{"name": "Sinigang", invalid}'; // deliberately broken JSON

$data = json_decode($json, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    echo "Failed to parse JSON: " . json_last_error_msg();
} else {
    print_r($data);
}
```

## Kitchen Notes (Best Practices)

- **Always pass `true` as the second argument to `json_decode()`**, unless you have a specific reason to want objects instead of arrays, since associative arrays fit naturally with everything else this book has taught since Chapter 19.
- **Always check `json_last_error()` after decoding data that came from outside your own script**, such as an API response or an uploaded file, rather than assuming it parsed correctly.
- **Treat decoded JSON as untrusted input, exactly like a superglobal, if it originated outside your own code.** A successfully parsed JSON string tells you the *format* was valid. It tells you nothing about whether the actual *values* inside it are safe, sensible, or expected. Validate the specific fields you need, the same way you would with `$_POST`.

## Yoras' Mistake

Yoras receives an order as JSON from an external system, and uses it immediately without checking anything:

```php
<?php

$json = file_get_contents("php://input"); // raw request body, in a real API
$order = json_decode($json, true);

$total = $order["quantity"] * $order["price"]; // no checks at all
```

If the JSON was malformed, `json_decode()` silently returns `null`, and `$order["quantity"]` on the very next line produces a warning and an unusable result, well past the point where the real problem actually occurred. Worse, even if the JSON *is* valid, nothing here confirms `quantity` and `price` are the sensible numbers this code assumes they are.

**Lesson:** check `json_last_error()` immediately after decoding, and validate the specific fields you actually plan to use, exactly as this book has taught for every other source of outside data since the Superglobals chapter. A successfully parsed JSON string is not the same thing as trustworthy data.

## Take-Home Practice

1. Encode an array representing a small order (dish name, quantity, price) into a JSON string, using `JSON_PRETTY_PRINT`.
2. Decode that same string back into an associative array, and print each field.
3. Deliberately pass a broken JSON string into `json_decode()`, check `json_last_error()`, and print a clear error message.

## Recap

- JSON is a lightweight, widely supported format for structured data, built from objects, arrays, strings, numbers, booleans, and null.
- `json_encode()` converts PHP data to a JSON string. `json_decode($json, true)` converts it back into an associative array.
- `json_last_error()` (and `json_last_error_msg()`) reliably detects a failed decode, since `null` alone is ambiguous.
- Successfully decoded JSON is still untrusted data if it came from outside your own script, and needs the same validation as any other outside input.

Next chapter: exceptions, or having a real plan for when something in the kitchen goes wrong.
