# Chapter 20: PHP Superglobals

### The Shared Communal Pantry

---

## Back in the Kitchen

Most containers in the kitchen belong to one station. A prep bowl at the vegetable station stays at the vegetable station. But a few things, the walk-in fridge, the master spice rack, are shared by the entire kitchen, reachable from any station, at any time, without anyone having to carry them over first. PHP has a handful of variables built exactly like that.

## The Concept

**Superglobals** are built-in PHP arrays that are automatically available everywhere in your script, in any function, without needing to be passed in as a parameter first, the way an ordinary variable would need to be (recall Chapter 18's lesson on scope). The most important ones to know:

- **`$_GET`**: data sent to the script through the URL, such as `page.php?id=5`.
- **`$_POST`**: data sent by a submitted HTML form, using the POST method. Covered fully in the Forms section.
- **`$_SERVER`**: information about the server and the current request, such as the current script's filename or the visitor's request method.
- **`$_SESSION`**: data that persists across multiple page loads for one specific visitor, covered fully in the Sessions chapter.
- **`$_COOKIE`**: small pieces of data stored in the visitor's own browser, covered fully in the Cookies chapter.
- **`$_FILES`**: information about a file the visitor uploaded, covered in the File Upload chapter.
- **`$_ENV`**: environment variables set outside of PHP itself, often used for configuration.
- **`$_REQUEST`**: a combination of `$_GET`, `$_POST`, and `$_COOKIE` together, generally best avoided in favor of checking the specific superglobal you actually mean.

Here's the single most important idea in this whole chapter, one that shapes everything in the upcoming Forms section: **every value inside a superglobal came from outside your own code.** A visitor typed it, or their browser sent it, or it arrived over the network. None of it should ever be trusted or used directly without being checked first.

## In the Code Kitchen

```php
<?php

// visiting page.php?id=5 makes this available:
echo $_GET["id"] ?? "No ID provided"; // 5

echo "<br>";
echo $_SERVER["REQUEST_METHOD"]; // GET, POST, etc., depending on how the page was requested
```

Notice the `??` from Chapter 14. It's essential here, since a key that was never actually sent will trigger a warning if you try to access it directly without checking first:

```php
<?php

// safe: falls back to "guest" if "name" was never sent
$name = $_GET["name"] ?? "guest";
echo "Hello, $name!";
```

An even more explicit, and often clearer, way to check is `isset()`, which tests whether a key exists at all before you try to use it:

```php
<?php

if (isset($_GET["id"])) {
    echo "ID was provided: " . $_GET["id"];
} else {
    echo "No ID provided.";
}
```

## Kitchen Notes (Best Practices)

- **Never echo a superglobal's value directly into HTML without escaping it first.** `htmlspecialchars($_GET["name"])`, not `$_GET["name"]` on its own, once real user input is involved. This is the single most important security habit in this entire book, and it starts mattering the moment superglobals enter the picture.
- **Never trust a superglobal's value as-is for anything meaningful**, such as a price, a permission check, or a database lookup, without validating it first. A visitor can send whatever they want in `$_GET` or `$_POST`, including values you never intended to allow.
- **Prefer `$_GET` and `$_POST` specifically over `$_REQUEST`.** Being explicit about where a value is expected to come from makes your code's intent clear, and avoids a category of confusion `$_REQUEST` can quietly introduce.

## Yoras' Mistake

Yoras builds a small page that greets a visitor by name from the URL, and writes:

```php
<?php

echo "Welcome, " . $_GET["name"] . "!";
```

This works fine for a normal name. But because he's echoing the value straight into the page with no escaping at all, a visitor could put HTML or even a script tag into that URL parameter, and it would be rendered by the browser exactly as if Chef Jirrum's Kitchen had written it. This is a real, well-known vulnerability called cross-site scripting, and it's a direct result of trusting a superglobal's value without escaping it.

**Lesson:** any time a superglobal's value is shown back to the browser, it must pass through `htmlspecialchars()` first:

```php
<?php

echo "Welcome, " . htmlspecialchars($_GET["name"] ?? "guest") . "!";
```

## Take-Home Practice

1. Create a page that reads a `name` value from `$_GET`, with a safe default if it's missing, and displays it safely using `htmlspecialchars()`.
2. Print `$_SERVER["REQUEST_METHOD"]` and confirm what it shows when you load the page normally in a browser.
3. Explain, in your own words, why `$_GET["id"]` should never be trusted directly in a database query or a price calculation without being checked first.

## Recap

- Superglobals (`$_GET`, `$_POST`, `$_SERVER`, `$_SESSION`, `$_COOKIE`, `$_FILES`, `$_ENV`) are built-in arrays available everywhere in a script, unlike ordinary variables.
- Every value inside a superglobal originated outside your own code, and must be treated as untrusted.
- `isset()` and `??` guard against accessing a key that was never sent.
- Any superglobal value displayed on a page must be escaped with `htmlspecialchars()` first.

Next chapter: regex, the quality inspector that checks whether a piece of text matches an exact pattern.
