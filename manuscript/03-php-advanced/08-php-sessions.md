# Chapter 34: PHP Sessions

### The Order Kept at the Table

---

## Back in the Kitchen

A cookie is like a stub the customer keeps in their own pocket. A session is different: it's the order the kitchen itself keeps track of, at the table, for as long as that customer is seated. The customer doesn't carry the actual order ticket around. The kitchen holds onto it, and simply knows which table it belongs to.

## The Concept

A **session** lets you store data on the server, tied to one specific visitor, across multiple page loads, without that data ever being exposed to the visitor's own browser. The mechanism connecting the two is a single small cookie, usually named `PHPSESSID`, holding nothing but a random ID. The browser sends that ID back on every request, and PHP uses it to look up the matching data, which lives entirely on the server.

This is the key difference from the last chapter: **a cookie's actual content sits in the visitor's browser and can be read or changed by them. A session's actual content sits on your server, completely out of the visitor's reach.** Only that one meaningless-looking ID travels back and forth.

Every page that wants to use sessions must call `session_start()` first, before any other output, the same rule that applied to `setcookie()`. Once started, session data lives in the familiar `$_SESSION` superglobal.

## In the Code Kitchen

**Starting a session and storing data in it**

```php
<?php
session_start();

$_SESSION["customerName"] = "Jirrum";
$_SESSION["cart"] = ["Adobo", "Sinigang"];
```

**Reading session data back on a later page**, after calling `session_start()` again

```php
<?php
session_start();

$name = $_SESSION["customerName"] ?? "Guest";
echo "Welcome back, " . htmlspecialchars($name) . "!";
```

Because `session_start()` reconnects to the same session using that one small cookie, `$_SESSION` picks up exactly where it left off, as long as the visitor hasn't cleared their cookies or the session hasn't expired.

**Ending a session**, commonly done on logout

```php
<?php
session_start();

$_SESSION = [];           // clear all session data
session_destroy();        // destroy the session on the server
setcookie(session_name(), "", time() - 3600, "/"); // remove the session cookie itself
```

**A simple login-state check**, a preview of a pattern you'll use constantly in any real application

```php
<?php
session_start();

if (isset($_SESSION["userId"])) {
    echo "You are logged in.";
} else {
    echo "Please log in.";
}
```

## Kitchen Notes (Best Practices)

- **Call `session_start()` at the very top of every page that needs session data**, before any HTML or `echo` output, exactly like `setcookie()`.
- **Use sessions, never cookies, for anything trust-dependent**, like login state, permission levels, or a shopping cart total, precisely because session data can't be read or edited directly by the visitor.
- **Call `session_regenerate_id()` immediately after a successful login.** This issues the visitor a brand new session ID at the exact moment their access level changes, closing off a real, known attack called session fixation, where an attacker tries to trick a visitor into using a session ID the attacker already knows.
- **Set a reasonable session timeout**, so an abandoned, logged-in session on a shared or public computer doesn't stay valid forever.

## Yoras' Mistake

Yoras builds a simple login check, but stores the VIP-customer flag from the earlier Cookies chapter instead of moving it into the session:

```php
<?php
session_start();

// Wrong: still trusting a cookie for something trust-dependent
if (($_COOKIE["isVipCustomer"] ?? "") === "true") {
    $_SESSION["discount"] = 0.20;
}
```

Even after switching to sessions for everything else, this line still reads the same tamperable cookie from Chapter 33 to *decide* whether to grant the discount in the first place. The session itself is safe, but the decision feeding into it wasn't, so the vulnerability survives.

**Lesson:** switching to sessions only helps for the data you actually store *in* the session. The decision of *what* to store there still needs to come from something the visitor can't manipulate, like a real, server-side check against your own records (a database check that a real login system would perform), not a cookie the visitor set themselves.

## Take-Home Practice

1. Start a session, store a customer's name and a small cart array in it, then read both back on a simulated "second page" (a second `session_start()` call further down the same script, or a second file).
2. Write the code to fully log a visitor out: clearing `$_SESSION`, calling `session_destroy()`, and removing the session cookie.
3. Explain, in your own words, why `session_regenerate_id()` matters immediately after a successful login.

## Recap

- A session stores data on the server, tied to one visitor through a single, meaningless session ID cookie.
- `session_start()` must run before any output, on every page using session data.
- Sessions are the correct place for trust-dependent data, since a visitor cannot read or edit session content directly.
- `session_regenerate_id()` after login protects against session fixation. Full logout requires clearing `$_SESSION`, calling `session_destroy()`, and removing the session cookie.

Next chapter: filters, a more systematic way to validate and sanitize the input this book has been treating carefully since Chapter 20.
