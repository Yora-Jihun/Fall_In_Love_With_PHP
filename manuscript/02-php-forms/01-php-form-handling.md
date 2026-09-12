# Chapter 22: PHP Form Handling

### Taking the Order

---

## Back in the Kitchen

Everything up to this point has been you writing the recipe and you eating the results. Real cooking means someone else walks up to the counter and tells you what they want. In a web application, that request arrives as a **form**, an HTML page where a visitor types something and sends it to your PHP script.

## The Concept

An HTML form uses the `<form>` tag, with two attributes that matter most:

- **`method`**: either `"get"` or `"post"`, controlling how the browser sends the data.
- **`action`**: which script receives the submitted data. Leaving it empty submits the form back to the exact same page it came from, which is the simplest and safest default for most everyday forms.

The difference between `GET` and `POST` is not just technical trivia:

- **GET** appends the form data directly onto the URL, visible to anyone (`page.php?name=Jirrum`). It's meant for requests that only *read* information, like a search box or a filter, and it should never be used for anything sensitive, since URLs get logged, bookmarked, and shared.
- **POST** sends the data in the request body, not the URL. It's the correct choice for anything that changes something, submits sensitive information, or is simply too long or too structured to belong in a URL, like a contact form or an order form.

Once a form is submitted, its values land in the matching superglobal from Chapter 20: `$_GET` for a GET form, `$_POST` for a POST form.

## In the Code Kitchen

A simple order form, submitting back to itself:

```html
<form method="post">
    <label for="dishName">Dish name:</label>
    <input type="text" id="dishName" name="dishName">

    <label for="servings">Servings:</label>
    <input type="number" id="servings" name="servings">

    <button type="submit">Place Order</button>
</form>
```

Handling it in PHP, checking the request method first before trying to read any submitted data:

```php
<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $dishName = $_POST["dishName"] ?? "";
    $servings = $_POST["servings"] ?? "";

    echo "Order received: " . htmlspecialchars($dishName);
    echo "<br>";
    echo "Servings: " . htmlspecialchars($servings);
}
?>

<form method="post">
    <label for="dishName">Dish name:</label>
    <input type="text" id="dishName" name="dishName">

    <label for="servings">Servings:</label>
    <input type="number" id="servings" name="servings">

    <button type="submit">Place Order</button>
</form>
```

That `if ($_SERVER["REQUEST_METHOD"] === "POST")` check matters. Without it, the script tries to read `$_POST` values that don't exist yet on the very first visit, before the form has ever been submitted, which produces warnings. Checking the request method first means the order-processing code only runs once there's actually an order to process.

Notice both submitted values are wrapped in `htmlspecialchars()` before being echoed back. Every value in `$_POST` came from outside your code, exactly as Chapter 20 warned, and that rule doesn't relax just because the value came from your own form instead of a random URL. A visitor can still type anything into a form field, including HTML or a script tag.

## Kitchen Notes (Best Practices)

- **Use POST for anything that submits data, changes something, or is even slightly sensitive.** Reserve GET for simple, read-only actions like search or filtering.
- **Always check `$_SERVER["REQUEST_METHOD"]` before processing form data**, so the handling code only runs on an actual submission, not on the initial page load.
- **Escape every submitted value with `htmlspecialchars()` before displaying it back**, with no exceptions, even for a field that seems harmless like a dish name.
- **Leave `action` empty to submit a form back to the same page**, rather than manually building the URL yourself. It's simpler and avoids an entire class of mistakes tied to getting that URL wrong.

## Yoras' Mistake

Yoras builds his form-handling code without checking the request method first:

```php
<?php

$dishName = $_POST["dishName"]; // no check, no fallback

echo "Order received: " . htmlspecialchars($dishName);
```

The very first time someone visits this page, before the form has ever been submitted, `$_POST["dishName"]` doesn't exist at all. This throws a warning and treats the missing value as an empty string, producing a confusing "Order received:" message with nothing after it, on a page that was never supposed to show that message yet.

**Lesson:** always guard form-processing code behind a check on `$_SERVER["REQUEST_METHOD"]`, and use `??` for a safe fallback on any individual field, so a page behaves correctly both before and after a form is submitted.

## Take-Home Practice

1. Build a simple form with a `name` and a `message` field, submitted using POST.
2. Handle the submission in PHP, checking the request method first, and display both values back safely with `htmlspecialchars()`.
3. Change the form's method to `"get"` instead, resubmit it, and observe how the values now appear directly in the URL.

## Recap

- Forms use `method="get"` or `method="post"`. GET is for read-only requests; POST is for anything sensitive or state-changing.
- Submitted data lands in `$_GET` or `$_POST`, matching the form's method.
- Always check `$_SERVER["REQUEST_METHOD"]` before processing submitted data.
- Every submitted value must be escaped with `htmlspecialchars()` before being echoed back, with no exceptions.

Next chapter: form validation, or making sure an order actually makes sense before the kitchen starts cooking it.
