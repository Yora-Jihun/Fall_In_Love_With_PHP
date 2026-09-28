# Chapter 33: PHP Cookies

### The Loyalty Stub in the Customer's Pocket

---

## Back in the Kitchen

Some restaurants hand out a small loyalty stub. Nothing valuable on its own, just enough to say "you've been here before." The restaurant doesn't need to remember your face. The stub in your own pocket does the remembering, and you bring it back with you next time. That's exactly what a cookie is.

## The Concept

A **cookie** is a small piece of data that your PHP script asks the visitor's browser to store, and which that browser then sends back automatically on every future request to your site, until it expires or is deleted. Unlike ordinary variables, which vanish the instant a page finishes loading, a cookie survives between separate visits, because it's stored on the visitor's own machine, not on your server.

`setcookie()` creates one, and its most useful parameters are:

- **name**: what the cookie is called.
- **value**: what it holds.
- **expire**: a timestamp for when it should stop being sent. Leaving this out makes it a "session cookie," which disappears once the browser closes.
- **httponly**: when `true`, prevents JavaScript running on the page from reading the cookie at all, a meaningful security protection against certain attacks.
- **secure**: when `true`, tells the browser to only ever send this cookie over an encrypted HTTPS connection.

Once set, a cookie's value shows up in the `$_COOKIE` superglobal on every subsequent request, exactly like `$_GET` and `$_POST`, and it deserves exactly the same suspicion. A cookie's value can be read and modified by the visitor themselves, using nothing more than their own browser's developer tools. **Never store anything a visitor shouldn't be able to see or change inside a cookie**, and never trust a cookie's value without validating it, the same rule that's applied to every other superglobal since Chapter 20.

## In the Code Kitchen

A cookie only shows its value on the *next* request, so this chapter uses three small files in your `kitchen` folder, one for each step. Save all three (Ctrl+S, or Cmd+S on a Mac) before you start. Open `http://kitchen.test/set-cookie.php` first (the page stays blank, which is expected), then `http://kitchen.test/read-cookie.php` to see the cookie come back. Finally, open `delete-cookie.php`, then reload `read-cookie.php` to see it's gone.

**Setting a cookie**, in `set-cookie.php`

```php
<?php

// Remember a visitor's preferred theme for 30 days.
setcookie(
    "preferredTheme",
    "dark",
    time() + (30 * 24 * 60 * 60), // 30 days from now, in seconds
    "/",     // available across the entire site
    "",      // current domain
    false,   // secure: true in production, over HTTPS
    true     // httponly: not accessible to JavaScript
);
```

`setcookie()` must be called before any actual output (any HTML, any `echo`) is sent to the browser, since cookies are sent as part of the response headers, which have to go out first.

**Reading a cookie back**, in `read-cookie.php`, on any later page load or visit:

```php
<?php

$theme = $_COOKIE["preferredTheme"] ?? "light"; // default if the cookie was never set
echo "Using theme: " . htmlspecialchars($theme);
```

**Deleting a cookie**, in `delete-cookie.php`, by setting its expiration to a moment in the past:

```php
<?php

setcookie("preferredTheme", "", time() - 3600, "/");
```

There's no dedicated "delete" function. Setting an already-expired time is simply how a browser is told to discard it.

## Kitchen Notes (Best Practices)

- **Never store sensitive information in a cookie**, such as a password, a credit card number, or anything that would cause harm if the visitor (or someone else using their machine) could read or edit it directly. Session data, covered in the next chapter, is the correct tool when data needs to stay private and untouched by the visitor.
- **Always set `httponly` to `true`** for cookies that don't specifically need to be read by JavaScript, closing off one common avenue certain attacks use to steal cookie data.
- **Always set `secure` to `true` on a live, production site** running over HTTPS, so the cookie is never sent over an unencrypted connection.
- **Validate a cookie's value before trusting it**, exactly as with `$_GET` or `$_POST`, since a visitor can edit their own cookies freely.

## Yoras' Mistake

Yoras stores a customer's discount eligibility directly in a cookie:

```php
<?php

setcookie("isVipCustomer", "true", time() + 86400);
```

Later, another part of the site checks this cookie to decide whether to apply a VIP discount:

```php
<?php

if (($_COOKIE["isVipCustomer"] ?? "") === "true") {
    echo "VIP discount applied!";
}
```

Any visitor can open their browser's developer tools, manually change that cookie's value to `"true"`, and grant themselves a discount they were never actually entitled to, since the entire check relies on data the visitor's own browser is trusted to report honestly.

**Lesson:** never use a cookie to store something a visitor could benefit from tampering with, like a discount, a permission level, or a login state. That kind of data belongs in a session, covered next, where it's stored on the server, entirely outside the visitor's reach.

## Take-Home Practice

1. Set a cookie storing a visitor's preferred number of servings for future visits, with a 7-day expiration.
2. Read that cookie back on a page reload, showing a sensible default if it hasn't been set yet.
3. Write the code to delete that same cookie, and confirm it's gone on the next page load.

## Recap

- A cookie is a small piece of data stored in the visitor's browser, sent back automatically on future requests.
- `setcookie()` must run before any other output. `$_COOKIE` reads a cookie's current value.
- A cookie is deleted by setting its expiration to a time in the past.
- Cookies are visible and editable by the visitor. Never store sensitive or trust-dependent data (like a discount flag or login state) in one.

Next chapter: sessions, where data stays private on the server instead.
