# Chapter 26: PHP Form Complete Example

### The Full Order Ticket

---

## Back in the Kitchen

Chef Jirrum lays a completed, real order ticket on the counter. Customer name, dish, quantity, contact e-mail, all filled in correctly, no blanks, no nonsense values. "This," he says, "is what every ticket should look like before it reaches the stove. Everything you've learned in this section exists to produce exactly this."

This chapter builds one complete order form, start to finish, combining every idea from this section: handling the submission, validating required fields, checking a specific format, and giving the visitor clear feedback.

## The Concept

There's no new syntax in this chapter. It's a synthesis of Chapters 22 through 25, assembled into one realistic, working form:

- Handle the request method correctly (Chapter 22).
- Validate required fields using `trim()` and `=== ""` (Chapters 23 and 24).
- Validate the e-mail format using `filter_var()` (Chapter 25).
- Collect every error at once, and redisplay the form as a sticky form if anything failed.
- Escape every value on its way back out, without exception.

## In the Code Kitchen

Create a new file named `order-form.php` in your `kitchen` folder, and open it at `http://kitchen.test/order-form.php`. The whole example below goes into that one file. Save it (Ctrl+S, or Cmd+S on a Mac) before you refresh the page.

```php
<?php

$errors = [];
$customerName = "";
$dishName = "";
$servings = "";
$email = "";
$orderConfirmed = false;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $customerName = trim($_POST["customerName"] ?? "");
    $dishName = trim($_POST["dishName"] ?? "");
    $servings = trim($_POST["servings"] ?? "");
    $email = trim($_POST["email"] ?? "");

    if ($customerName === "") {
        $errors[] = "Please enter your name.";
    }

    if ($dishName === "") {
        $errors[] = "Please choose a dish.";
    }

    if ($servings === "") {
        $errors[] = "Please enter the number of servings.";
    } elseif (!is_numeric($servings) || (int) $servings <= 0) {
        $errors[] = "Servings must be a positive number.";
    }

    if ($email === "") {
        $errors[] = "Please enter your e-mail address.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "That doesn't look like a valid e-mail address.";
    }

    if (empty($errors)) {
        $orderConfirmed = true;
        // In a real application, this is where you'd save the order
        // or send a confirmation e-mail. Both are covered later in this book.
    }
}
?>

<!DOCTYPE html>
<html>
<body>

<h1>Order Form, Chef Jirrum's Kitchen</h1>

<?php if ($orderConfirmed): ?>
    <p>
        Thank you, <?php echo htmlspecialchars($customerName); ?>!
        Your order for <?php echo htmlspecialchars($servings); ?> serving(s) of
        <?php echo htmlspecialchars($dishName); ?> has been received.
        A confirmation will be sent to <?php echo htmlspecialchars($email); ?>.
    </p>
<?php else: ?>

    <?php if (!empty($errors)): ?>
        <ul>
            <?php foreach ($errors as $error): ?>
                <li><?php echo htmlspecialchars($error); ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <form method="post">
        <label for="customerName">Your name:</label>
        <input type="text" id="customerName" name="customerName"
               value="<?php echo htmlspecialchars($customerName); ?>">
        <br>

        <label for="dishName">Dish:</label>
        <input type="text" id="dishName" name="dishName"
               value="<?php echo htmlspecialchars($dishName); ?>">
        <br>

        <label for="servings">Servings:</label>
        <input type="text" id="servings" name="servings"
               value="<?php echo htmlspecialchars($servings); ?>">
        <br>

        <label for="email">E-mail:</label>
        <input type="text" id="email" name="email"
               value="<?php echo htmlspecialchars($email); ?>">
        <br>

        <button type="submit">Place Order</button>
    </form>

<?php endif; ?>

</body>
</html>
```

Read through this once from top to bottom, matching each section to the chapter it came from. Nothing here is new. What's new is seeing all of it work together, in the shape a real, small form actually takes.

## Kitchen Notes (Best Practices)

- **Only show the success message once every single check has passed.** `$orderConfirmed` only becomes `true` inside the `empty($errors)` block, so there's no path where a partially valid order gets treated as confirmed.
- **Keep the confirmed-order view and the form-with-errors view clearly separate**, as shown with the `if / else` around the whole page body, so a visitor never sees a confusing mix of a "thank you" message and a list of errors at the same time.
- **Escape absolutely everything on the way out, in every branch, with no exceptions**, including the confirmation message. This is worth restating one more time, since it's the single habit that matters most in this entire section.

## Yoras' Mistake

Yoras builds something similar, but shows the confirmation message based only on whether the form was submitted, not on whether it actually passed validation:

```php
<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // ...validation happens here...
    echo "Thank you for your order!"; // shown regardless of $errors
}
```

A customer who left every field blank still sees "Thank you for your order!", right above a list of errors saying the order wasn't actually valid. This confuses the customer and, worse, suggests to them that something was processed when nothing was.

**Lesson:** always gate a success message behind a genuine check that validation fully passed, such as `empty($errors)`, never just behind "the form was submitted."

## Take-Home Practice

1. Build the complete order form from this chapter yourself, from scratch, without copying it directly. Get it running on your local setup.
2. Add one more required field of your choosing (a delivery address, for instance), following the exact same pattern as the others.
3. Deliberately submit the form with a mix of valid and invalid fields, and confirm the sticky form correctly keeps the valid ones filled in while flagging only the invalid ones.

## Recap

- A complete form combines request handling, required-field checks, format validation, sticky redisplay, and consistent escaping, all working together.
- A success message should only appear once validation has genuinely and fully passed, never just because the form was submitted.
- Every value that reaches the page, in every branch of the logic, must be escaped with `htmlspecialchars()`.

This closes out **Part 2: PHP Forms**. Next up: **Part 3, PHP Advanced**, covering dates, files, cookies, sessions, and what to do when something in the kitchen goes wrong.
