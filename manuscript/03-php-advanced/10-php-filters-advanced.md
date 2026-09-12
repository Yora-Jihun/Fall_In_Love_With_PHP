# Chapter 36: PHP Filters, Advanced

### Straining the Whole Order at Once

---

## Back in the Kitchen

Checking one ingredient at a time through the strainer works, but a real order ticket has several items on it at once. It's worth having a way to run everything through the strainer together, in one pass, rather than one line of code per field.

## The Concept

`filter_var_array()` and `filter_input_array()` apply a whole set of filters to a whole array of values, or directly to a whole superglobal, in a single call. You describe what you want by passing an array where each key is a field name, and each value is either a filter constant, or, for more control, an array specifying the filter along with extra options and flags.

This is especially useful for cleaning up the kind of multi-field validation first built back in the Forms section, replacing several repetitive lines with one clearly structured definition of the rules.

## In the Code Kitchen

**`filter_var_array()`, filtering a plain array of values**

```php
<?php

$input = [
    "servings" => "4",
    "email" => "cook@kitchen.com",
    "website" => "not-a-url",
];

$filters = [
    "servings" => FILTER_VALIDATE_INT,
    "email" => FILTER_VALIDATE_EMAIL,
    "website" => FILTER_VALIDATE_URL,
];

$result = filter_var_array($input, $filters);

var_dump($result["servings"]); // int(4)
var_dump($result["email"]);    // string, the valid email
var_dump($result["website"]);  // bool(false), failed validation
```

**`filter_input_array()`, pulling straight from `$_POST`**

```php
<?php

$filters = [
    "customerName" => FILTER_UNSAFE_RAW, // no validation, just retrieve as-is (still needs escaping later)
    "servings" => FILTER_VALIDATE_INT,
    "email" => FILTER_VALIDATE_EMAIL,
];

$data = filter_input_array(INPUT_POST, $filters);

$errors = [];

if (empty(trim($data["customerName"] ?? ""))) {
    $errors[] = "Please enter your name.";
}

if ($data["servings"] === false || $data["servings"] === null) {
    $errors[] = "Servings must be a whole number.";
}

if ($data["email"] === false || $data["email"] === null) {
    $errors[] = "Please enter a valid e-mail address.";
}
```

**Using flags and options for finer control**, here allowing a float with fractional parts

```php
<?php

$options = [
    "options" => [
        "min_range" => 0,
    ],
    "flags" => FILTER_FLAG_ALLOW_FRACTION,
];

$price = filter_var("19.99", FILTER_VALIDATE_FLOAT, $options);
var_dump($price); // float(19.99)
```

This chapter's array-based approach and the Forms section's earlier, more manual style solve the same problem in different ways. The manual style from Chapter 23 is easier to follow while learning, since every check is spelled out step by step. The array-based style shown here scales better once a form has many fields, since the rules for every field are declared together, in one clear, structured place, rather than scattered across several separate `if` statements.

## Kitchen Notes (Best Practices)

- **Reach for `filter_input_array()` once a form has enough fields that individual `if` checks start feeling repetitive.** It centralizes the validation rules in one readable block, which is easier to review and maintain as a form grows.
- **Remember `FILTER_UNSAFE_RAW` performs no validation or sanitization at all.** It exists purely to retrieve a raw value through the same consistent interface. Anything read this way still needs the exact same care as any other untrusted input: validated appropriately, and escaped with `htmlspecialchars()` before display.
- **Don't reach for this array-based style before you're genuinely comfortable with the simpler, one-field-at-a-time approach from the Forms section.** Both are correct. This one is a scaling tool, not a replacement for understanding the fundamentals first.

## Yoras' Mistake

Yoras filters an entire form at once, and assumes every returned value is automatically safe to use directly:

```php
<?php

$filters = [
    "customerName" => FILTER_UNSAFE_RAW,
    "servings" => FILTER_VALIDATE_INT,
];

$data = filter_input_array(INPUT_POST, $filters);

echo "Hello, " . $data["customerName"]; // no escaping applied at all
```

`FILTER_UNSAFE_RAW`, true to its name, does nothing to make a value safe. It's the plainest possible passthrough. Echoing `$data["customerName"]` directly into HTML is exactly as risky as echoing `$_POST["customerName"]` directly would have been, since filtering it with `FILTER_UNSAFE_RAW` changed nothing about its safety.

**Lesson:** running a value through the filter system doesn't automatically make it safe to display. Validation and sanitization happen on the way in. Escaping with `htmlspecialchars()` still has to happen separately, on the way out, every single time.

## Take-Home Practice

1. Use `filter_var_array()` to validate a small array representing an order: a servings count (integer) and an e-mail address.
2. Rewrite the complete order form from Chapter 26 using `filter_input_array()` instead of individual field checks, and compare how the two versions read.
3. Explain, in your own words, why a value retrieved with `FILTER_UNSAFE_RAW` still needs to be escaped before being displayed.

## Recap

- `filter_var_array()` and `filter_input_array()` apply a full set of validation or sanitization rules to multiple fields in a single call.
- This array-based style scales well for larger forms, but the fundamentals from the Forms section still apply underneath it.
- `FILTER_UNSAFE_RAW` performs no safety checks at all. It's a plain retrieval, not a safety guarantee.
- Filtering handles validation and sanitization on the way in. Escaping with `htmlspecialchars()` is still required on the way out.

Next chapter: callback functions, or handing a fellow cook instructions for what to do next.
