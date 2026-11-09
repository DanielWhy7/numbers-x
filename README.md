# Square Number X

A simple command-line trainer for memorizing square numbers (n × n = ?), written in pure Python with no external dependencies.

**Version:** 1.4.1

---

## Description

`Square Number X` quizzes you on the squares of numbers within a range you choose. It supports several ways to traverse the range (counting up, counting down, or in random order), a "Remember" mode that just prints the table, an optional error corrector, and a running mistake counter.

---

## Requirements

- Python 3.x
- No third-party packages required (uses only `random.randint`)

---

## Running

```bash
python main.py
```

---

## Usage

When the program starts, you enter a range and pick a mode.

### 1. Range

```
Enter minimum: 21
Enter maximum: 29
```

- If the entered value is **not a number**, it defaults to `11`.
- Pressing an exit command at any prompt (see below) closes the program.

### 2. Mode

```
Procedural | Random | Reverse | Remember
Mode: 
```

| Mode | Aliases | Behavior |
|------|---------|----------|
| **Procedural** | `p`, `proced`, `procedural` | Counts up from minimum to maximum, then loops back to the minimum. Asks you for each answer. |
| **Random** | `r`, `ran`, `rand`, `random`, `rng` | Picks numbers randomly within the range. Asks you for each answer. |
| **Reverse** | `e`, `rev`, `reverse` | Counts down from maximum to minimum, then loops. Asks you for each answer. |
| **Remember** | `qr`, `remem`, `remember` | Just prints every `n x n = n²` in range. No input required. |

### 3. Extra options

- **Random mode:** asks *"Skip numbers that ends at 0 — Enable:"*
  > ⚠️ Note: the answer is collected but **not actually used** in version 1.4.1 (feature not yet implemented).
- **Procedural / Reverse modes:** asks *"Error corrector — Enable:"*
  > If enabled, a wrong answer **restarts the sequence from the minimum**. If disabled, the sequence continues as usual.

Answer **True values** to enable an option: `t`, `true`, `1`, `y`, `yes`, `yeah`.

---

## During the quiz

The program prompts:

```
7x7:
```

Type your answer. Outcomes:

| Input | Result |
|-------|--------|
| Correct number | `[+] Correct.` |
| Menu / mode command | `[*] Mode changed` — returns to range/mode setup |
| Error command | `[*] Mistakes: <k>` — shows current mistake count (does **not** count as a wrong answer) |
| Anything else | `[-] Wrong. Right answer is <n²>` — mistake counter increments |

### Commands recognized at *any* prompt

| Purpose | Accepted inputs |
|---------|-----------------|
| Exit program | `q`, `exit`, `break`, `escape`, `ctrl+c`, `ctrlc`, `^c` |
| Change mode | `menu`, `configuration`, `home`, `m` |
| Show mistakes | `er`, `error`, `mistake` |
| "True" | `t`, `true`, `1`, `y`, `yes`, `yeah` |

> The exit command is checked at every input, including the minimum/maximum prompts and option prompts.

---

## Example session

```
Square Number X | Version: 1.4.1
_______________________________

Enter minimum: 11
Enter maximum: 19

Procedural | Random | Reverse | Remember
Mode: procedural

Error corrector
Enable: y
_______________________________

11x11: 121
 [+] Correct.
_______________________________

12x12: 141
 [-] Wrong. Right answer is 144
_______________________________

11x11:        ← error corrector restarted from minimum
```

---

## Known limitations (v1.4.1)

- **"Skip numbers ending in 0"** is prompted in Random mode but never applied.
- The inner `while run:` loop is never explicitly terminated (`run` is never set to `False`); returning to the menu relies on a `break`.
- The mistake counter `k` is global and persists across mode changes during a single run.
- Language support is a `#TODO` — the program is English-only.
- The `"Mistakes"` command resets `prevnumber = number - 1`, which affects the next procedural/reverse step in a way that isn't fully defined (`#IDK` in source).
