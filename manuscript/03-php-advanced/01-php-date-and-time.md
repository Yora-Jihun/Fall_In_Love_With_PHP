# Chapter 27: PHP Date and Time

### The Kitchen Clock

---

## Back in the Kitchen

A kitchen runs on timing. When the special started. How long the adobo has been simmering. When the last order came in. None of that means anything without a clock on the wall everyone agrees on.

## The Concept

PHP's `date()` function formats the current date and time (or a specific timestamp) into a readable string, using a set of format characters:

- `Y`: four-digit year (2026)
- `m`: two-digit month (01 to 12)
- `d`: two-digit day (01 to 31)
- `H`: two-digit hour, 24-hour format
- `i`: two-digit minutes
- `s`: two-digit seconds
- `l`: full day name (Monday)
- `F`: full month name (January)

Underneath all of this is the **Unix timestamp**, a single number counting the seconds elapsed since January 1, 1970. `time()` returns the current timestamp. Nearly every date function in PHP either produces or accepts one of these numbers.

For anything beyond simple formatting, especially date math (adding days, comparing two dates, handling timezones), PHP's object-oriented `DateTime` class is the more reliable, modern tool. It's introduced briefly here, and will feel more familiar once Part 4 covers classes and objects properly.

## In the Code Kitchen

**Basic formatting**

```php
<?php

echo date("Y-m-d");           // 2026-09-12
echo "<br>";
echo date("l, F j, Y");       // Friday, September 12, 2026
echo "<br>";
echo date("H:i:s");           // 14:30:00
```

**Working with timestamps**

```php
<?php

$now = time();
echo $now; // a large number, seconds since January 1, 1970

echo date("Y-m-d H:i:s", $now); // formats that specific timestamp
```

**Parsing human-friendly text with `strtotime()`**

```php
<?php

$tomorrow = strtotime("+1 day");
echo date("Y-m-d", $tomorrow);

$specificDate = strtotime("2026-12-25");
echo date("l", $specificDate); // Friday (whatever day Dec 25, 2026 falls on)
```

**The `DateTime` class, for anything more involved**

```php
<?php

$orderTime = new DateTime();
echo $orderTime->format("Y-m-d H:i:s");

$orderTime->modify("+30 minutes");
echo $orderTime->format("H:i:s"); // 30 minutes ahead of when it was created
```

`DateTime` objects also compare cleanly against each other, which is far more reliable than comparing formatted strings or raw timestamps by hand once real scheduling logic is involved.

## Kitchen Notes (Best Practices)

- **Set your timezone explicitly**, either with `date_default_timezone_set("Asia/Manila")` at the top of your script, or in your server's `php.ini` configuration. Without an explicit timezone, PHP falls back to a default that may not match your actual audience, which causes confusing, hard-to-spot timing bugs.
- **Prefer the `DateTime` class over raw timestamp math once your logic gets more complex than simple display**, since it correctly handles things like months with different lengths and daylight saving time, which manual timestamp arithmetic can get subtly wrong.
- **Never store a formatted date string as your only source of truth.** Store the actual timestamp or a proper `DateTime` value, and format it for display only at the point where it's actually shown to someone.

## Yoras' Mistake

Yoras builds a "time until closing" feature, calculating it by hand with raw timestamps:

```php
<?php

$closingTime = strtotime("22:00:00");
$now = time();
$secondsLeft = $closingTime - $now;

echo $secondsLeft; // works fine before 10 PM, but goes negative right after
```

This works fine most of the day, but at 10:01 PM, `$secondsLeft` becomes negative, since `strtotime("22:00:00")` always resolves to today's 10 PM, even after it has already passed, rather than rolling forward to tomorrow's 10 PM.

**Lesson:** be explicit about which day you mean. `strtotime("today 22:00:00")` versus `strtotime("tomorrow 22:00:00")` removes the ambiguity, and for anything beyond a quick calculation like this, the `DateTime` class's comparison methods are usually the more robust choice.

## Take-Home Practice

1. Print today's date in the format "Month Day, Year" (for example, "September 12, 2026").
2. Use `strtotime()` to calculate and print the date exactly one week from today.
3. Create a `DateTime` object, add 2 hours to it with `modify()`, and print the result.

## Recap

- `date()` formats the current time or a given timestamp using format characters like `Y`, `m`, `d`, `H`, `i`, and `s`.
- `time()` returns the current Unix timestamp. Nearly all date functions revolve around this number.
- `strtotime()` converts human-friendly text like `"+1 day"` into a timestamp.
- The `DateTime` class is the more reliable tool for date math and comparisons.
- Always set your timezone explicitly, rather than relying on a server default.

Next chapter: `include`, or borrowing a recipe card from another binder.
