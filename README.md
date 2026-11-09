# Square Number X — V2.0.0

A simple command-line trainer for memorizing square numbers (`n × n = ?`), written in pure Python with no external dependencies.

This trainer is intended for **two-digit squares** — for example, `25 × 25` up to `95 × 95` — though any range can be used.

---

## Description

`Square Number X` quizzes you on the squares of numbers within a range you choose. It supports several traversal modes (counting up, counting down, random order), a **Remember** mode that just prints the table, an optional **error corrector**, and an optional **skip-multiples-of-10** filter for Random mode. The mistake counter is kept per session.

---

## Requirements

- Python 3.8 or newer
- No third-party packages required

---

## Running

Launch the program from a terminal with Python 3.8 or newer.

---

## Usage

### 1. Range

```
Enter minimum: 25
Enter maximum: 29
```

- If an entered value is **not a number**, it defaults to `11`.
- If `minimum > maximum`, the two values are swapped automatically.
- Pressing an **exit command** at any prompt closes the program.

### 2. Mode

```
Procedural | Random | Reverse | Remember
Mode:
```

| Mode | Aliases | Behavior |
|------|---------|----------|
| **Procedural** | `p`, `pro`, `proced`, `procedural` | Counts up from minimum to maximum, then loops back to the minimum. |
| **Random** | `r`, `ran`, `rand`, `random`, `rng` | Picks numbers randomly within the range. |
| **Reverse** | `e`, `rev`, `reverse` | Counts down from maximum to minimum, then loops. |
| **Remember** | `qr`, `rem`, `remem`, `remember` | Just prints every `n x n = n²` in range, then returns to the range prompt. |

### 3. Extra options

- **Random mode** — *“Skip multiples of 10 / Enable:”*
  > Numbers ending in `0` are excluded from the random pool. If the range contains only multiples of 10, a normal random pick within the range is used instead.

- **Procedural / Reverse modes** — *“Error corrector / Enable:”*
  > If enabled, a wrong answer **restarts the sequence from the minimum**. If disabled, the sequence continues as usual.

Answer with a **true value** to enable an option: `t`, `true`, `1`, `y`, `yes`, `yeah`, `ye`, `sure`.

---

## During the quiz

The program prompts:

```
25x25:
```

The answer is compared case-insensitively.

| Input | Result |
|-------|--------|
| Correct number | `[+] Correct.` |
| Menu / mode command | `[*] Mode changed` — returns to the range/mode setup |
| Error command | `[*] Mistakes: <k>` — shows the current session mistake count (does **not** count as a wrong answer) |
| Anything else | `[-] Wrong. Right answer is <n²>` — mistake counter increments; if the error corrector is on, the sequence restarts from the minimum |

> The mistake counter is **local to a session**: it starts at `0` every time a session begins, and is reset when you return to the menu.

### Commands recognized at *any* prompt

| Purpose | Accepted inputs |
|---------|-----------------|
| Exit program | `q`, `^c`, `exit`, `break`, `ctrl+c`, `escape`, `ctrlc` |
| Change mode | `menu`, `configuration`, `home`, `m` |
| Show mistakes | `er`, `error`, `mistake` |
| “True” | `t`, `true`, `1`, `y`, `yes`, `yeah`, `ye`, `sure` |

> Exit commands are checked at every input, including the minimum/maximum prompts and the option prompts. The check is case-insensitive (`Q` works too). `Ctrl+C` and EOF also exit cleanly.

---

## Example session

```
Square Number X

Enter minimum: 25
Enter maximum: 29

Procedural | Random | Reverse | Remember
Mode: procedural

Error corrector
Enable: y

25x25: 625
[+] Correct.
26x26: 686
[-] Wrong. Right answer is 676
25x25:
```

Notes on this example:

- With the error corrector enabled, the wrong answer at `26x26` restarts the sequence at the minimum (`25x25`).

A **Remember** session prints the whole table and then returns to the range prompt:

```
Square Number X

Enter minimum: 25
Enter maximum: 27

Procedural | Random | Reverse | Remember
Mode: remember
_______________________________

25x25: 625
26x26: 676
27x27: 729
```

---

## Changes in V2.0.0

- **Skip multiples of 10 is now implemented** in Random mode (in v1.4.1 it was prompted but ignored).
- **Exit is handled cleanly** through a dedicated exit request instead of stopping deep inside input parsing. `Ctrl+C` and EOF are also caught cleanly at the top level.
- **Mistake counter is per session** instead of a global that persisted across mode changes.
- **Range is auto-normalized**: if `minimum > maximum`, they are swapped.
- **Negative numbers now parse correctly** when entering a range.
- **Exit and option checks are case-insensitive** (input is lowercased).
- The **“Mistakes” command no longer changes the sequence position** (this was the `#IDK` behavior in v1.4.x).
- The dead loop and the global run flag have been removed.
- The “Skip numbers that ends at 0” wording was corrected to **“Skip multiples of 10”**.

---

## Known limitations (v2.0.0)

- The program is **English-only** (no localization).
- The session mistake count is shown only on demand via the `er` / `error` / `mistake` command; there is no final tally when a session ends.
- In Remember mode the table is printed and then control returns to the **range** prompt
- Random mode can pick the same number twice in a row (expected behavior for independent random draws).
- No separator is printed between individual questions; separators appear only at session boundaries.
