# Chapter 23: PHP Form Validation

### Checking the Order Before You Cook It

---

## Back in the Kitchen

A ticket comes in with no dish name written on it. Another one lists "servings: banana." A good kitchen doesn't just start cooking whatever a confusing ticket seems to suggest. It stops, checks the ticket, and asks the customer to clarify before anything hits the stove. That's validation.

## The Concept

**Validation** means checking submitted data against a set of rules before you use it or act on it, and giving the visitor a clear, specific message about what needs to be fixed if it doesn't pass. Chapter 22 showed how to receive form data. This chapter is about making sure that data is actually usable before you trust it.

A common, reliable pattern looks like this:

1. Check the request method, as shown in the last chapter.
2. Read each expected field, with a safe fallback.
3. Run each field through whatever checks it needs, and collect any problems into an array of error messages.
4. If there are no errors, process the order. If there are errors, redisplay the form along with the specific messages, and, ideally, the visitor's previously entered values, so they don't have to retype everything from scratch.

## In the Code Kitchen

```php
<?php

$errors = [];
$dishName = "";
$servings = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $dishName = trim($_POST["dishName"] ?? "");
    $servings = trim($_POST["servings"] ?? "");

    if ($dishName === "") {
        $errors[] = "Please enter a dish name.";
    }

    if ($servings === "") {
        $errors[] = "Please enter the number of servings.";
    } elseif (!is_numeric($servings) || (int) $servings <= 0) {
        $errors[] = "Servings must be a positive number.";
    }

    if (empty($errors)) {
        echo "Order confirmed: " . htmlspecialchars($dishName) . " for " . htmlspecialchars($servings) . " serving(s).";
    }
}
?>

<?php if (!empty($errors)): ?>
    <ul>
        <?php foreach ($errors as $error): ?>
            <li><?php echo htmlspecialchars($error); ?></li>
        <?php endforeach; ?>
    </ul>
<?php endif; ?>

<form method="post">
    <label for="dishName">Dish name:</label>
    <input type="text" id="dishName" name="dishName" value="<?php echo htmlspecialchars($dishName); ?>">

    <label for="servings">Servings:</label>
    <input type="text" id="servings" name="servings" value="<?php echo htmlspecialchars($servings); ?>">

    <button type="submit">Place Order</button>
</form>
```

A few details worth slowing down on:

- `trim()` runs first, so a field containing only spaces is correctly treated as empty, rather than sneaking past the check.
- The `value="<?php echo htmlspecialchars($dishName); ?>"` on each input re-fills the form with what the visitor already typed, called a "sticky form," so a mistake in one field doesn't force them to retype everything else.
- `empty($errors)` checks whether the errors array has anything in it at all. Only when it's completely empty does the order get confirmed.
- The alternative `if: ... endif:` syntax appears here for the first time. It's functionally identical to regular curly-brace `if` blocks, and is commonly preferred specifically inside a template like this, where PHP and HTML are mixed together, since it reads a little more cleanly than closing braces scattered among HTML tags.

## Kitchen Notes (Best Practices)

- **Validate on the server, always, even if you also validate in the browser with JavaScript or HTML attributes like `required`.** Browser-side checks can be bypassed entirely by anyone who wants to. Server-side validation, the kind covered in this chapter, is the only check that can't be skipped.
- **Collect every error at once, rather than stopping at the first problem found.** A visitor who fixes one mistake only to be shown a brand new one they hadn't seen yet has a frustrating experience for no good reason.
- **Always redisplay previously entered values, escaped, using the sticky form pattern.** Losing everything a visitor already typed because of one small mistake is a needless bit of friction.

## Yoras' Mistake

Yoras validates the servings field, but checks the raw string before trimming it:

```php
<?php

$servings = $_POST["servings"] ?? "";

if ($servings === "") {
    $errors[] = "Please enter the number of servings.";
}
```

A visitor who accidentally types a few spaces into the field, `"   "`, passes this check, since `"   " === ""` is false. The order proceeds with a servings value that's really just whitespace, and any later math on it produces confusing results.

**Lesson:** always `trim()` a text field before checking whether it's empty, so whitespace-only input is correctly caught as missing, exactly as shown in the working example above.

## Take-Home Practice

1. Add a `customerName` field to the order form example, and validate that it isn't empty (after trimming).
2. Test the servings validation with a few different inputs: empty, a letter, a negative number, and a valid positive number. Confirm each produces the expected result.
3. Confirm the sticky form behavior works: submit the form with one field wrong, and check that the other fields keep their previously typed values.

## Recap

- Validation checks submitted data against clear rules, before it's trusted or acted on.
- Collect all validation errors into an array, rather than stopping at the first one.
- `trim()` before checking for emptiness, so whitespace-only input is correctly treated as missing.
- Sticky forms, redisplaying previously entered (and escaped) values, make fixing a mistake far less frustrating for the visitor.
- Server-side validation is mandatory. Browser-side validation is a nice convenience, never a substitute.

Next chapter: a closer, focused look at required fields specifically.
