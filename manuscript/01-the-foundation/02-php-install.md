# Chapter 2: PHP Install

### Setting Up Your Practice Kitchen

---

## Back in the Kitchen

"Before you cook anything," Chef Jirrum says, "you need a kitchen. A stove that turns on. A sink that runs. Right now you have a recipe card and no stove."

That's exactly where you are with `hello.php` from the last chapter. The file is correct, but there's nowhere to run it yet.

## The Concept

To run PHP, you need two things working together: a web server, and PHP itself installed so the server knows how to process `.php` files. Setting both of these up by hand is possible, but most learners and even most professionals use a bundled tool that installs everything at once, already wired together.

This book uses **Herd**. It's a free tool for Windows and macOS, made by the Laravel team. One installer gives you PHP and a web server (called nginx), already set up to work together. There's nothing to configure by hand.

We picked Herd for two reasons:

- **It's easy to set up.** Install it, open it, and your practice kitchen is ready.
- **It's easy to keep up to date.** Herd can install or update PHP with one click. You won't be stuck on an old version of PHP without knowing it.

You may also hear about other tools, like XAMPP or Laragon. They work too, and the PHP code in this book runs the same on any of them. A recipe doesn't care which brand of stove you use. But every setup step in this book is written for Herd.

There's one more option worth knowing about. PHP comes with its own small **built-in server**. It's handy for quick practice, and it's a good choice if you're on Linux, where Herd isn't available. It's only for your own computer, never for a real website with real visitors.

## In the Code Kitchen

**Option A: Herd (used in this book)**

1. Download Herd from its official site (herd.laravel.com) and run the installer.
2. Open Herd. It creates a folder called `Herd` in your user folder. On Windows, that's `%USERPROFILE%\Herd`. On macOS, it's `~/Herd`.
3. Inside the `Herd` folder, make a new folder called `kitchen`. This folder is your kitchen counter. Herd turns every folder in here into its own website.
4. Move your `hello.php` file from Chapter 1 into the `kitchen` folder.
5. Open a browser and visit `http://kitchen.test/hello.php`.

If everything is set up correctly, you'll see: `Welcome, Cook. The kitchen is open.`

The folder name becomes the web address. A folder called `kitchen` becomes `kitchen.test`. A folder called `menu` would become `menu.test`.

**Set VS Code as Herd's editor**

In Chapter 1, you wrote `hello.php` in **VS Code**, the editor this book uses. If you use a different editor, Herd also works with PhpStorm and Sublime Text. The steps below are the same, just pick your editor instead.

Herd can open your sites and files straight in your editor. For that to work, tell Herd which editor you use:

1. Open Herd's **Settings**.
2. Go to the **General** tab.
3. Find the IDE setting and choose **VS Code**.

That's it. Now when Herd opens a site or a file, it opens in VS Code instead of some other editor. It's like putting your favorite knife on the counter before you start cooking, so you're not digging through drawers later.

**Option B: PHP's built-in server**

If you already have PHP installed on your computer, you can use this for quick practice. Open a terminal in the folder that has `hello.php` and run:

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
- **Keep PHP up to date.** Herd makes this one click, so there's no reason to skip it. Newer versions bring fixes and new features.

## Yoras' Mistake

Yoras installs Herd, but drops his `hello.php` file on his Desktop instead of inside the `Herd` folder. He visits `http://kitchen.test/hello.php` and gets an error. Right away, he decides Herd is broken.

Herd isn't broken. It only serves files from inside its own folder, the same way a kitchen only cooks what's been carried inside it. A file sitting on the Desktop is a file the kitchen has never seen.

**Lesson:** always check that your PHP files are inside the folder your server uses. For Herd, that's a folder inside `Herd`, like `Herd/kitchen`. For the built-in server, it's the folder you started it from.

## Take-Home Practice

1. Install Herd and open it. In Settings, under the General tab, set your IDE to VS Code.
2. Make a `kitchen` folder inside the `Herd` folder, move `hello.php` into it, and load `http://kitchen.test/hello.php` in your browser.
3. Run `php -v` in a terminal and write down the version number you see.
4. Try the built-in server method as well, just once, so you understand both paths exist.

## Recap

- Running PHP needs a web server plus PHP itself. This book uses Herd, which installs both for you and makes updating PHP one click.
- Herd serves every folder inside its `Herd` folder as a website. A folder called `kitchen` becomes `http://kitchen.test`.
- This book uses VS Code as its editor. Set it as Herd's IDE under Settings, in the General tab.
- PHP's built-in server (`php -S localhost:8000`) is a fast option for local practice, but is never meant for a live, public site.
- Check your installed version with `php -v` before starting any project.

Next chapter: now that the kitchen is open, it's time to learn the basic rules every PHP recipe follows.
