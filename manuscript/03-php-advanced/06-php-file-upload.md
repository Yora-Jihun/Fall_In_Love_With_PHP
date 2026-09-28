# Chapter 32: PHP File Upload

### A New Recipe Card From a Customer

---

## Back in the Kitchen

Sometimes a customer hands you something directly. A photo of a dish they loved elsewhere. A signed form. A document for a catering order. Handling a file that arrives from outside your own kitchen deserves more caution than almost anything else covered in this book, because you're not just reading text anymore. You're accepting an actual file, of a type you didn't choose, from someone you don't know.

## The Concept

An HTML form can include a file input, but it needs one extra attribute beyond what Chapter 22 covered: `enctype="multipart/form-data"`, without which file data won't actually be sent at all.

Once submitted, information about the uploaded file lands in the `$_FILES` superglobal, first mentioned back in Chapter 20, structured like this for a field named `recipeCard`:

- `$_FILES["recipeCard"]["name"]`: the original filename, exactly as it was on the visitor's own computer.
- `$_FILES["recipeCard"]["type"]`: the file's MIME type, as reported by the browser.
- `$_FILES["recipeCard"]["tmp_name"]`: a temporary location on the server where PHP has already placed the file.
- `$_FILES["recipeCard"]["error"]`: an error code, `UPLOAD_ERR_OK` (which equals `0`) if everything went fine.
- `$_FILES["recipeCard"]["size"]`: the file's size, in bytes.

Here is the single most important fact in this entire chapter: **`name` and `type` are both reported by the visitor's browser, and neither one can be trusted.** A visitor, or anyone sending a request directly without even using a browser, can claim a file named `virus.exe` is actually `photo.jpg`, and claim its type is `image/jpeg`, regardless of what the file actually is. Believing either value without independently checking the file itself is a well-known, serious security mistake.

## In the Code Kitchen

Create a new file named `upload.php` in your `kitchen` folder. Next to it, create an empty folder named `uploads`, which is where the saved images will go. The PHP handling code goes at the top of `upload.php`, and the form goes below it, the same shape as the order form in Chapter 22. Save the file (Ctrl+S, or Cmd+S on a Mac), then open `http://kitchen.test/upload.php`.

Keeping `uploads` inside `kitchen` is fine for practice on your own computer. For a real website, see the Kitchen Notes below.

The form:

```html
<form method="post" enctype="multipart/form-data">
    <label for="recipeCard">Upload a recipe photo:</label>
    <input type="file" id="recipeCard" name="recipeCard">
    <button type="submit">Upload</button>
</form>
```

Handling it at the top of `upload.php`, with the checks that actually matter:

```php
<?php

$errors = [];
$uploadDir = __DIR__ . "/uploads/";
$allowedTypes = ["image/jpeg", "image/png"];
$maxSize = 2 * 1024 * 1024; // 2 MB

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_FILES["recipeCard"])) {
    $file = $_FILES["recipeCard"];

    if ($file["error"] !== UPLOAD_ERR_OK) {
        $errors[] = "There was a problem uploading the file.";
    } elseif ($file["size"] > $maxSize) {
        $errors[] = "The file is too large. Maximum size is 2 MB.";
    } else {
        // Check the file's ACTUAL type by inspecting its content,
        // never by trusting $file["type"], which the browser can misreport.
        $actualType = mime_content_type($file["tmp_name"]);

        if (!in_array($actualType, $allowedTypes, true)) {
            $errors[] = "Only JPEG and PNG images are allowed.";
        }
    }

    if (empty($errors)) {
        // Generate a new, random filename. Never trust or reuse the
        // visitor-supplied original filename directly.
        $extension = $actualType === "image/png" ? "png" : "jpg";
        $newFilename = bin2hex(random_bytes(16)) . "." . $extension;

        if (move_uploaded_file($file["tmp_name"], $uploadDir . $newFilename)) {
            echo "Upload successful.";
        } else {
            echo "Failed to save the uploaded file.";
        }
    }
}
```

Notice `move_uploaded_file()`, not a generic file-copy function. It specifically checks that the file actually came from a genuine, valid upload, which is an extra safeguard beyond what a generic file operation would give you.

## Kitchen Notes (Best Practices)

- **Never trust `$_FILES[...]["type"]` or the original `name`.** Check the file's real content type using something like `mime_content_type()`, and generate your own new, random filename rather than reusing anything the visitor sent.
- **Always enforce a maximum file size**, both in your PHP code and, realistically, at the web server level too, to avoid a visitor overwhelming your server with an enormous upload.
- **Store uploaded files outside your publicly served web folder when possible, or in a folder configured to never execute code.** An uploaded file that somehow contains executable code should never be able to run, no matter what its extension claims to be.
- **Always use `move_uploaded_file()`, never a generic copy or rename function, for handling the temporary uploaded file.**

## Yoras' Mistake

Yoras builds an upload feature and, to keep things "simple," trusts the browser-reported type directly:

```php
<?php

$file = $_FILES["recipeCard"];

if ($file["type"] === "image/jpeg" || $file["type"] === "image/png") {
    move_uploaded_file($file["tmp_name"], __DIR__ . "/uploads/" . $file["name"]);
    echo "Upload successful.";
}
```

This looks reasonable, but it has two real problems. First, `$file["type"]` is exactly what the visitor's browser *claims* the file is, and a malicious visitor can send any value they want here, regardless of the file's actual content. Second, using `$file["name"]` directly means a visitor could upload a file literally named something like `../../config.php`, attempting the exact path traversal issue flagged back in the File Handling chapter, potentially overwriting a file well outside the intended uploads folder.

**Lesson:** verify a file's actual content type independently, never from a value the browser sent, and always generate a fresh, random filename yourself rather than trusting anything about the name the visitor's file arrived with.

## Take-Home Practice

1. Build the upload form and handler from this chapter, allowing only JPEG and PNG images under 2 MB.
2. Test it by attempting to upload a file of a disallowed type, and confirm it's correctly rejected.
3. Explain, in your own words, why checking `mime_content_type()` is meaningfully safer than checking `$_FILES[...]["type"]`.

## Recap

- `$_FILES` holds information about an uploaded file, but its `name` and `type` fields are reported by the visitor's browser and cannot be trusted on their own.
- Always verify a file's actual type by inspecting its content, and enforce a maximum size.
- Always generate a new, random filename for a saved upload, rather than reusing the original.
- Use `move_uploaded_file()` specifically, and consider storing uploads outside your publicly served folder.

Next chapter: cookies, small pieces of data kept in the customer's own pocket between visits.
