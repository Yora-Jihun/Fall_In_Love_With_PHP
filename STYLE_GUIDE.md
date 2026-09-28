# The Book Bible: "The Code Kitchen"

This file is the single source of truth for how every chapter is written. Read this before writing or editing any chapter. It keeps the writing style, the running story, and the technical standards consistent across all ~50 chapters.

---

## 1. The Premise

Learning to program feels the same as learning to cook on day one. There are too many unfamiliar words. There's a fear of ruining something. There's a nagging feeling that everyone else already knows the "trick." This book teaches PHP the way a good Filipino home cook teaches a family recipe. You get put in the kitchen. You get a task small enough not to be scary. And you get the *why* behind every step, not just the *what*.

The promise to the reader: by the last page, PHP should feel less like a foreign syntax and more like a recipe you've cooked so many times you don't need the card anymore.

Audience: written to be honest and correct enough for a working developer, but paced and explained for someone who has never programmed before.

## 2. The World: Chef Jirrum's Kitchen

The whole book is framed as a running apprenticeship in one place. **Chef Jirrum's Kitchen** is a small, warm, slightly chaotic Filipino eatery where Chef Jirrum trains new cooks. The reader is the newest apprentice, addressed directly as **"Cook"** (used gender-neutrally, the way "chef" is used in English) throughout the book.

Rules for using the setting:
- The kitchen is introduced once, fully, in the Preface. After that, chapters can drop into it without re-explaining it.
- Not every chapter needs a long scene. A one- or two-line callback ("Back in the kitchen...") is enough to keep continuity. The analogy should serve the lesson, never bury it.
- The metaphor explains *concepts*, not syntax. PHP syntax is still taught precisely and correctly. The kitchen is the lens, not a replacement for accuracy.

## 3. The Cast

Keep this cast small and use it sparingly. It's seasoning, not the meal.

- **Chef Jirrum**: the mentor and narrator's voice. Patient, funny, occasionally exasperated, and always circles back to *why* a rule exists instead of just stating it. Speaks in clear, plain English throughout.
- **You, the Cook**: the reader, addressed directly in second person ("you").
- **Yoras**: the eager but sloppy fellow apprentice who makes the classic beginner mistakes (forgets a semicolon, mixes up `=` and `==`, trusts raw customer input, and so on). Used for "common mistake" callouts so the reader never feels singled out for the same mistake.
- **Aling Nena**: the veteran cook who represents old habits and legacy style. Used sparingly to contrast an old, unsafe way of doing something with the modern, correct PHP 8.x way. Never mocked, just shown that there's a newer, better way now.

Do not introduce new recurring characters without updating this file.

## 4. Writing Style Rules

("Voice" below is a plain writing-craft term for tone and style, meaning how the text reads on the page. This is a text ebook. Nothing here involves audio.)

- **Everything is written in plain, clear English.** Narration, dialogue, and section bodies, all of it, so any reader can pick this up regardless of background. This is an international book, not a region-locked one.
- Filipino dish and ingredient names (adobo, sinigang, lumpia, lechon, and so on) are the one exception. They're used on purpose because they anchor the cooking theme, and each one is explained in plain English the first time it shows up in a chapter. No sentence should ever require outside knowledge of Tagalog to understand.
- Second person, present tense, warm but not childish. Professionals should not feel talked down to.
- One idea per paragraph. Short paragraphs. This is a book people read while a local server is running in another window.
- Humor comes from specificity (a very particular kitchen disaster), not from generic jokes.
- Never let the metaphor contradict the technical truth. If a metaphor and accuracy fight, accuracy wins. The metaphor gets adjusted or dropped.
- **No em dashes.** Use a comma, a period, or parentheses instead. Em dashes are a dead giveaway of AI-written text, and this book should read like it was written by a person.
- **Keep the grammar simple.** Short, plain sentences beat long, layered ones. Avoid stacked clauses, semicolons, and academic phrasing. If a sentence needs to be read twice to be understood, split it into two sentences. Write at a level a high school reader and a working professional can both move through easily.

## 5. Accuracy and Originality Rules

1. Every factual or technical claim (what a function does, version history, the current PHP release, how a language feature behaves) must be checked against current, authoritative sources (the php.net manual, RFCs, or a current reputable source) before it's written. This matters most for anything version- or date-sensitive, since PHP keeps changing.
2. Never copy sentences, phrasing, or example structure from php.net or any other source. Explanations, analogies, and code examples must be original. It's fine, and expected, to teach the same *concept* the manual teaches. It's not fine to reuse its words.
3. Code examples are original, written for this book, and checked for correctness (traced through by hand or actually run), not lifted from documentation or tutorials.
4. When a fact is time-sensitive (for example, "the current PHP version"), phrase it so the book ages well. Say "as of PHP 8.x" or "at the time of writing" instead of stating it as a permanent fact.

## 6. Code Standards (what every code sample must follow)

These rules aren't Laravel-specific, since this is core PHP. But the underlying professional habits are the same ones enforced in our engineering skills, translated into plain PHP:

- **Type safety first.** Prefer `declare(strict_types=1);`, typed properties, and typed function signatures once the book has introduced types (from the "Casting" chapter onward). Frame this as "measure, don't eyeball it." Precise measurements make a recipe repeatable.
- **Never trust raw input.** Any example touching form data, files, or query strings must show validation or sanitization (for example, `filter_var`, or `htmlspecialchars` on output). Frame this as "wash it before it goes in the pot." This is non-negotiable even in a beginner example. We don't teach insecure habits "for simplicity."
- **Escape all output.** Any example that echoes user-supplied data into HTML must escape it. No exceptions, even in a two-line demo.
- **Small, named, single-purpose functions.** This mirrors "one recipe, one dish." A function should do one thing a reader can name.
- **Testable mindset.** Where it fits naturally (Functions, Exceptions, and later OOP chapters), show how you'd check that a piece of code actually works. A quick manual check or a simple assertion is enough. Frame this as "taste before you serve it." There's no need for a full testing framework in the core chapters. The habit matters more than the tool here.
- **Modern PHP.** Use current PHP 8.x idioms (typed properties, arrow functions, `match`, named arguments, constructor property promotion once OOP starts) instead of outdated PHP 5 or PHP 7 era patterns, unless the point of the section is explicitly historical.

## 7. Chapter Template

Every chapter file follows this shape. Section names can be renamed for flavor, but the function of each part stays the same:

1. **Cold open (scene).** A short kitchen moment that sets up *why* today's concept matters. 2 to 6 short paragraphs.
2. **The Concept.** The plain-English, technically accurate explanation of the PHP feature. This section must be correct and complete even if the reader skipped the scene.
3. **In the Code Kitchen.** The real PHP syntax, with worked examples built up in small steps.
4. **Kitchen Notes (Best-Practice Notes).** A short callout box of best practices, gotchas, and security notes tied to Section 6 above.
5. **Yoras' Mistake.** One common beginner error related to the topic, shown, explained, and corrected. Optional for very short chapters, but preferred.
6. **Take-Home Practice.** 2 to 4 small exercises the reader can cook on their own local setup.
7. **Recap.** A tight bullet-point summary of what was learned.

## 8. The Concept to Kitchen Glossary

This is the canonical mapping. Reuse these terms consistently instead of inventing new metaphors per chapter. Consistency is what makes the running narrative pay off.

| PHP Concept | Kitchen Metaphor |
|---|---|
| PHP itself | The style and method of cooking used in this kitchen |
| Local server (this book uses Herd; sites live in folders inside `Herd` and load at `http://<folder>.test`; the book's editor is VS Code, set as Herd's IDE) | The practice kitchen, before you cook for real guests (production) |
| Browser / output | The dining table where the finished dish is served |
| Variable | A labeled container holding one ingredient at a time |
| Data types | Categories of ingredients: text (`string`), measurements (`int`/`float`), yes-or-no taste checks (`bool`), a tray of several items (`array`) |
| Constants | The one heirloom measurement in a family recipe that never changes |
| Operators | Kitchen actions, like combining, comparing, and adjusting a dish |
| `echo` / `print` | Plating and serving the dish so it's visible at the table |
| Casting | Repackaging an ingredient into a different container without changing what it fundamentally is |
| Math functions | The kitchen scale and measuring cups |
| If / Else / Switch | Tasting the dish and deciding what to do next |
| Loops | A repeated motion, like stirring until the sauce thickens or folding a spring roll wrapper by wrapper |
| Functions | A recipe card: a named, reusable set of steps |
| Arrays | A serving tray with multiple compartments for several ingredients at once |
| Superglobals | The shared communal pantry every station in the kitchen can reach into |
| Regex | The quality inspector checking whether something matches the exact spec |
| Forms | The order slip a customer fills out at the counter |
| Date and Time | The kitchen clock and the "best cooked before" timer |
| Include | Borrowing a recipe card from another binder to slot into today's menu |
| File handling | Writing to and reading from the kitchen's recipe notebook |
| File upload | A customer or cook handing you a new recipe card to file into the binder |
| Cookies | A small loyalty stub the customer keeps with them between visits |
| Sessions | The order the kitchen keeps track of while the customer is still seated |
| Filters | The strainer that catches anything that shouldn't go into the pot |
| Callback functions | Telling a fellow cook, "when you finish that, do this next," handing off what happens next |
| JSON | A standardized recipe card format any kitchen, not just this one, can read |
| Exceptions | A kitchen mishap (something burned, something dropped) and having a plan for when it happens |
| OOP (overall) | Moving from cooking one dish at a time to running a proper recipe system you can repeat and franchise |
| Class / Object | The recipe card (class, the blueprint) versus the actual plated dish (object, one instance made from it) |
| Constructor | `Mise en place`, the prep that always happens the moment you start a dish |
| Destructor | Cleaning the station once the dish is done and served |
| Access modifiers | Menu-public recipes (`public`), Grandma's locked recipe drawer (`private`), and family-only recipes shared within the kitchen (`protected`) |
| Inheritance | A family recipe passed down generations, each adding its own twist |
| Class constants | The one rule of a recipe lineage that's never allowed to change |
| Abstract classes | A cookbook entry that demands "every version of this dish must have a marinate step" without dictating exactly how |
| Interfaces | A food-safety standard: any dish that claims to be a `MainCourse` must be able to `serve()` |
| Traits | A technique (like a marinade method) you can mix into any recipe, regardless of family line |
| Static methods/properties | Shared kitchen equipment, like the communal stove or master spice rack, used without needing your own personal copy |
| Namespaces | Organizing recipes into labeled cookbook sections so two kitchens' "Adobo" don't collide |
| Iterables | Working your way down a buffet table, one dish at a time, in order |

## 9. Book Map (working order)

Front matter, then **The Foundation** (Introduction through Regex), then **PHP Forms**, then **PHP Advanced**, then **PHP OOP**, following the reader-provided table of contents. Chapter files live under `manuscript/`, one Markdown file per chapter, numbered to match reading order.

## 10. Status

- [x] Book bible established
- [x] Front matter drafted (title page, preface, table of contents)
- [x] **Part 1, The Foundation: complete** (Chapters 1 to 21, PHP Introduction through PHP Regex)
- [x] **Part 2, PHP Forms: complete** (Chapters 22 to 26, Form Handling through the complete example)
- [x] **Part 3, PHP Advanced: complete** (Chapters 27 to 39, Date and Time through Exceptions)
- [ ] Part 4, PHP OOP (Chapters 40 to 53)
