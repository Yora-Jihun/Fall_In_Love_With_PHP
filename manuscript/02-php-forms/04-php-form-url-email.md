# Chapter 25: PHP Form URL and E-mail

### Checking the Shape, Not Just the Presence

---

## Back in the Kitchen

Confirming a field isn't blank is step one. Step two, for certain fields, is confirming it actually looks like what it claims to be. A delivery address field that isn't empty but just says "asdf" passed the required check and failed everyone anyway. E-mail addresses and web addresses are the two most common fields that need this deeper level of checking.

## The Concept

Back in the Regex chapter, this book's own advice was to prefer a purpose-built function over a hand-written pattern for common, well-known formats. E-mail addresses and URLs are exactly that case. PHP provides `filter_var()`, a general-purpose validation and sanitization function, along with a set of built-in filters covering these common formats:

- **`FILTER_VALIDATE_EMAIL`** checks whether a string is shaped like a valid e-mail address.
- **`FILTER_VALIDATE_URL`** checks whether a string is shaped like a valid URL.

`filter_var()` returns the validated value if it passes, or `false` if it doesn't, which makes it simple to use directly inside a condition.

It's worth being precise about what this actually guarantees: `FILTER_VALIDATE_EMAIL` confirms an address is correctly *formatted*. It does not confirm the address actually exists, belongs to a real person, or can receive mail. Format and existence are two entirely different questions, and this filter only answers the first one.

## In the Code Kitchen

```php
<?php

$errors = [];
$email = "";
$website = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = trim($_POST["email"] ?? "");
    $website = trim($_POST["website"] ?? "");

    if ($email === "") {
        $errors[] = "Please enter your e-mail address.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "That doesn't look like a valid e-mail address.";
    }

    if ($website !== "" && !filter_var($website, FILTER_VALIDATE_URL)) {
        $errors[] = "That doesn't look like a valid website address.";
    }
}
```

Notice the `website` field is checked a little differently. It's treated as optional. The validation only runs `filter_var()` on it *if* something was actually entered (`$website !== ""`), since an empty, optional field shouldn't be flagged as an invalid URL.

You can see `filter_var()` in isolation clearly here:

```php
<?php

var_dump(filter_var("cook@kitchen.com", FILTER_VALIDATE_EMAIL));  // string, the valid email itself
var_dump(filter_var("not-an-email", FILTER_VALIDATE_EMAIL));      // bool(false)

var_dump(filter_var("https://example.com", FILTER_VALIDATE_URL)); // string, the valid URL itself
var_dump(filter_var("just some text", FILTER_VALIDATE_URL));      // bool(false)
```

## Kitchen Notes (Best Practices)

- **Use `filter_var()` with the built-in filters for e-mail and URL checks, instead of writing a custom regex.** It's a well-tested, standard part of PHP, and it correctly handles far more edge cases than most hand-written patterns would.
- **Remember that valid format does not mean the address is real or reachable.** If you genuinely need to confirm an e-mail address belongs to someone, the standard approach is sending a confirmation link to that address and waiting for it to be clicked, a technique outside the scope of this book, but worth knowing exists.
- **Only validate an optional field's format if something was actually entered.** An empty optional field should be allowed to stay empty, not rejected for "failing" a format check it was never meant to be judged against.

## Yoras' Mistake

Yoras writes an e-mail check like this:

```php
<?php

$email = trim($_POST["email"] ?? "");

if (strpos($email, "@") !== false) {
    echo "Valid email!";
}
```

This accepts `"@"` on its own, and `"a@b"`, and plenty of other clearly broken addresses, because it only checks for the presence of an `@` symbol somewhere in the string, using a string function from Chapter 8, rather than actually validating the address's overall shape.

**Lesson:** checking for a single character is not the same as validating a format. `filter_var($email, FILTER_VALIDATE_EMAIL)` correctly rejects malformed addresses that a simple `strpos()` check would let straight through.

## Take-Home Practice

1. Add e-mail validation to a contact form, using `filter_var()`, with a clear error message for an invalid format.
2. Add an optional `website` field, validated only when it isn't empty.
3. Test both fields with a mix of valid and clearly invalid values, and confirm the results match what you'd expect.

## Recap

- `filter_var($value, FILTER_VALIDATE_EMAIL)` and `filter_var($value, FILTER_VALIDATE_URL)` check whether a string is correctly formatted as an e-mail address or URL.
- Valid format is not the same as a real, reachable address. `filter_var()` only checks the shape.
- Only run a format check on an optional field if it actually has a value.
- Prefer `filter_var()`'s built-in filters over a hand-written regex for well-known formats like e-mail and URLs.

Next chapter: putting everything from the Forms section together into one complete, working example.
