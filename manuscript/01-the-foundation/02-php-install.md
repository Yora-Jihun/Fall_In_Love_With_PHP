# Chapter 2: PHP Install

### Setting Up Your Practice Kitchen

---

## Back in the Kitchen

"Before you cook anything," Chef Jirrum says, "you need a kitchen. A stove that turns on. A sink that runs. Right now you have a recipe card and no stove."

That's exactly where you are with `hello.php` from the last chapter. The file is correct, but there's nowhere to run it yet.

## The Concept

To run PHP, you need two things working together: a web server, and PHP itself installed so the server knows how to process `.php` files. Setting both of these up by hand is possible, but most learners and even most professionals use a bundled tool that installs everything at once, already wired together.

The three most common choices are:

- **XAMPP**: a free, cross-platform bundle (Windows, macOS, Linux) that includes Apache (the web server), PHP, and MySQL (a database, which you won't need yet, but will later). It's the most widely used option for beginners because setup is a single installer.
- **Laragon**: a lightweight environment popular on Windows, known for being fast to install and easy to switch PHP versions in.
- **Herd**: a modern, polished local environment originally built for Laravel developers, available for macOS and Windows, that manages PHP versions for you with almost no configuration.

Any of these will get you cooking. This book assumes XAMPP in its examples because it is the most common starting point, but the PHP code itself works identically no matter which one you choose. A recipe doesn't care which brand of stove you're using.

There's also a fourth option worth knowing about, even if you don't use it daily: PHP ships with its own **built-in development server**, no separate installation of Apache required. It's meant strictly for local practice, not for serving a real website to real visitors.

## In the Code Kitchen

**Option A: XAMPP**

1. Download XAMPP from its official site and run the installer.
2. Open the XAMPP Control Panel and click "Start" next to Apache.
3. Find the `htdocs` folder inside your XAMPP installation. This folder is your kitchen counter. Anything you place here becomes reachable through the browser.
4. Move your `hello.php` file from Chapter 1 into `htdocs`.
5. Open a browser and visit `http://localhost/hello.php`.

If everything is set up correctly, you'll see: `Welcome, Cook. The kitchen is open.`

**Option B: PHP's built-in server**

If you already have PHP installed on your system directly, you can skip Apache entirely for practice purposes. Open a terminal in the folder containing `hello.php` and run:

```
php -S localhost:8000
```

Then visit `http://localhost:8000/hello.php` in your browser. This command starts a small, temporary server that only exists while the terminal window stays open. Close the terminal, and the kitchen closes with it.

Either way, confirm your setup works by checking your installed PHP version from a terminal:

```
php -v
```

This should print a version number starting with `8.` This book was written and checked against modern PHP 8.x, so anything in that range will run every example correctly.

## Kitchen Notes (Best Practices)

- **Never use the built-in server for a real, public website.** It's single-threaded and made for local development only. It's a small practice stove, not a commercial kitchen. The PHP manual itself is explicit about this.
- **Keep your local setup and your live website separate in your head from day one.** The practice kitchen (your machine) is where you're allowed to burn things. A production server, one that real visitors use, is not.
- **Check your PHP version regularly**, especially before starting a new project, since language features do change between versions.

## Yoras' Mistake

Yoras installs XAMPP, but drops his `hello.php` file on his Desktop instead of inside `htdocs`. He visits `http://localhost/hello.php` and gets a "Not Found" error, and immediately assumes Apache is broken.

Apache isn't broken. It only serves files from inside its designated folder, the same way a kitchen only cooks what's actually been carried inside it. A file sitting on the Desktop is a file the kitchen has never seen.

**Lesson:** always double-check that your PHP files live inside the folder your server actually serves from (`htdocs` for XAMPP, or whichever folder you launched the built-in server from).

## Take-Home Practice

1. Install XAMPP (or Laragon, or Herd) and get Apache running.
2. Move `hello.php` into the correct folder and load it successfully in your browser.
3. Run `php -v` in a terminal and write down the version number you see.
4. Try the built-in server method as well, just once, so you understand both paths exist.

## Recap

- Running PHP requires a web server plus PHP itself, usually bundled together in a tool like XAMPP, Laragon, or Herd.
- XAMPP serves files from its `htdocs` folder. A file has to be inside that folder to be reachable by the browser.
- PHP's built-in server (`php -S localhost:8000`) is a fast option for local practice, but is never meant for a live, public site.
- Check your installed version with `php -v` before starting any project.

Next chapter: now that the kitchen is open, it's time to learn the basic rules every PHP recipe follows.
