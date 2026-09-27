# Chapter 6: PHP Echo / Print

### Plating the Dish

---

## Back in the Kitchen

You've been cooking in Chapters 1 through 5, but nothing has actually reached a customer yet. A finished dish sitting in the kitchen, never carried out to the table, might as well not exist to the person waiting to eat it. `echo` and `print` are how a dish leaves the kitchen.

## The Concept

`echo` and `print` both send output to the browser. They're used constantly, and beginners often ask which one to use. Here's the honest, complete answer:

- **`echo`** has no return value, and can take multiple values at once, separated by commas.
- **`print`** always returns the integer `1`, and can only take a single value.
- **Performance difference between them is negligible** to the point of not mattering in any real project. `echo` is used slightly more often in modern PHP code, largely by convention, and that's what this book uses going forward.

Both display exactly what you give them. If you give them a string, they display that string. If you give them a number, PHP converts it to text automatically before displaying it.

One small heads-up. Later, you'll meet two more tools with similar names: `var_dump()` in Chapter 7 and `print_r()` in Chapter 19. Don't mix up `print_r()` with `print`. They're different tools. `echo` and `print` serve the dish to the customer. `var_dump()` and `print_r()` are for you, the cook, to peek inside a variable and see exactly what it holds. For now, `echo` is all you need.

## In the Code Kitchen

```php
<?php

$dish = "Chicken Adobo";
$price = 150;

echo $dish;
echo "<br>";
echo "Price: ", $price, " pesos"; // echo accepts multiple values
echo "<br>";

print "This also works, but only takes one value at a time.";
```

That `"<br>"` is plain HTML, a line break tag, dropped in as ordinary text. Remember, PHP is generating a page that a browser will read as HTML, so if you want a visible line break on the page, you need an actual HTML tag, not just a new line in your PHP file. A blank line inside your PHP code is invisible to the browser.

You can also combine variables and text into a single string, using the concatenation operator from the last chapter, or a technique called string interpolation, which only works inside double quotes:

```php
<?php

$dish = "Sinigang";

echo "Today's special is " . $dish . "."; // concatenation
echo "<br>";
echo "Today's special is $dish.";         // interpolation, double quotes only
```

Both lines print the same thing. Interpolation, dropping the variable name directly inside a double-quoted string, is often considered more readable once you're comfortable with it. Single quotes never interpolate. `'Today's special is $dish.'` would print the literal text `$dish`, dollar sign and all, not the value inside it. Chapter 8 covers this distinction in full.

## Kitchen Notes (Best Practices)

- **Escape any value that came from a user before echoing it into HTML.** This chapter's examples use text we wrote ourselves, which is safe. Starting in the Forms section of this book, you'll be echoing text that a stranger typed into a form, and that always needs to pass through `htmlspecialchars()` first. This habit is introduced properly there, but it's worth knowing the rule exists from here on.
- **Pick one of `echo` or `print` and stick with it across a project.** Mixing both styles in the same codebase adds nothing but visual noise for whoever reads it later.
- **Use `<br>` or wrap output in proper HTML tags (`<p>`, `<h1>`, and so on) rather than relying on plain line breaks**, since a browser ignores plain whitespace when rendering HTML.

## Yoras' Mistake

Yoras writes this and can't figure out why his page shows the text `$total` instead of a number:

```php
<?php

$total = 250;
echo 'Your total is $total pesos.';
```

Single quotes don't interpolate variables. Inside single quotes, `$total` is just a dollar sign and five letters, nothing more. PHP has no reason to look it up as a variable.

**Lesson:** if you want a variable's value to appear inside a string, either use double quotes for interpolation, or use concatenation with the `.` operator, which works with either quote style.

## Take-Home Practice

1. Print three lines of output using `echo`, each on its own visible line in the browser (remember `<br>`).
2. Write one line using string concatenation and an equivalent line using double-quote interpolation. Confirm they produce identical output.
3. Deliberately reproduce Yoras' mistake, single quotes around a variable, then fix it two different ways.

## Recap

- `echo` and `print` both send output to the browser. `echo` accepts multiple values and has no return value; `print` accepts one value and returns `1`.
- Double-quoted strings support variable interpolation. Single-quoted strings do not.
- `<br>` or proper HTML tags control visible line breaks in the browser. Blank lines in your PHP file don't.
- Any user-supplied value needs to be escaped before it's echoed into HTML, a rule that becomes essential once real input enters the picture.

Next chapter: data types, or getting familiar with the different kinds of ingredients PHP works with.
