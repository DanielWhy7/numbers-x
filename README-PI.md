# πRad-Pro

Memorize the most useful **sin, cos, tan, ctg** values at the 17 standard angles (0° – 360°, step 30°), plus their radian equivalents.

**Version:** 1.1.2

---

## Description

πRad-Pro drills you on trigonometric values at the 17 standard angles. You pick a **mode** (how to traverse the table) and a **function** (sin / cos / tan / ctg / angle in radians), then answer each prompt. Answers use a compact shorthand: `s` for `√` and `p` for `π`.

There is no range prompt — the table is always the full 0° → 360° sweep.

---

## Requirements

- Python 3.x
- No third-party packages (uses only `random.randint`)

---

## Running

```bash
python pirad.py
```

---

## Usage

### 1. Mode

```
Procedural | Random | Reverse | Remember
Mode:
```

| Mode | Aliases | Behavior |
|------|---------|----------|
| **Procedural** | `p`, `proced`, `procedural` | Steps through 0° → 360°, then repeats. |
| **Random** | `r`, `ran`, `rand`, `random`, `rng` | Picks a random angle each turn. |
| **Reverse** | `e`, `rev`, `reverse` | Steps through 360° → 0°, then repeats. |
| **Remember** | `qr`, `remem`, `remember` | Prints the whole table once. No input required. |

### 2. Function

```
SIN | COS | TAN | CTG | A
Func:
```

| Function | Aliases | What it quizzes |
|----------|---------|-----------------|
| `sin` | `sin`, `synapse`, `s` | Sine values |
| `cos` | `cos`, `c` | Cosine values |
| `tan` | `tan`, `tg`, `t` | Tangent values |
| `ctg` | `ctan`, `ctg`, `ct` | Cotangent values |
| `A` | `a` | Radian label for each degree |

Anything unrecognized falls back to **sin**.

### 3. Answer format

The program compares your input after two shorthand substitutions:

- `s` → `√`
- `p` → `π`

| You type | Becomes | Matches |
|----------|---------|---------|
| `s3/2` | `√3/2` | sin 60°, sin 120°, … |
| `s2/2` | `√2/2` | sin 45°, cos 45°, … |
| `p/6` | `π/6` | angle 30° |
| `1/2` | `1/2` | sin 30°, cos 60°, … |
| `-s3/2` | `-√3/2` | negative values need a leading `-` |
| *(empty Enter)* | *(empty)* | undefined values — `tan 90°`, `tan 270°`, `ctg 0°`, `ctg 180°`, `ctg 360°` |

Only these substitutions apply — nothing else is normalized. `√3/3`, for example, must be typed `s3/3`.

### Commands recognized at any prompt

| Purpose | Accepted inputs |
|---------|-----------------|
| **Exit** | `exit`, `break`, `ctrl+c`, `escape`, `ctrlc`, `c`, `q`, `quit` |
| **Change mode** | `m`, `menu`, `home`, `conf`, `config`, `configuration` |

> ⚠️ `c` is **both** the exit command and the `cos` alias — typing `c` at the *Func* prompt exits the program. Type `cos` instead.
>
> `m` / `menu` returns you to mode selection; you'll also be asked for a new function.

---

## Example session

```
πRad-Pro | Version: 1.1.2
_______________________________

Procedural | Random | Reverse | Remember
Mode: procedural

SIN | COS | TAN | CTG | A
Func: cos
_______________________________

sin(0°): 1
Right.
_______________________________

sin(30°): s3/2
Right.
_______________________________

sin(45°): s3/2
Wrong.Correct is s2/2.
_______________________________
```

> The prompt in Procedural and Reverse modes is **hardcoded to `sin(...)`** regardless of the function you picked — see *Known limitations* below. The answer is still checked against the selected function.

A **Remember** session prints the full table once and returns to the mode prompt:

```
Procedural | Random | Reverse | Remember
Mode: remember

SIN | COS | TAN | CTG | A
Func: sin
_______________________________

sin(0°): 0
sin(30°): 1/2
sin(45°): s2/2
...
sin(360°): 0
```

---

## Reference table

The 17 standard angles πRad-Pro quizzes you on:

| Angle | Radians | sin | cos | tan | ctg |
|-------|---------|-----|-----|-----|-----|
| 0° | `0` | `0` | `1` | `0` | — |
| 30° | `p/6` | `1/2` | `s3/2` | `s3/3` | `s3` |
| 45° | `p/4` | `s2/2` | `s2/2` | `1` | `1` |
| 60° | `p/3` | `s3/2` | `1/2` | `s3` | `s3/3` |
| 90° | `p/2` | `1` | `0` | — | `0` |
| 120° | `2p/3` | `s3/2` | `-1/2` | `-s3` | `-s3/3` |
| 135° | `3p/4` | `s2/2` | `-s2/2` | `-1` | `-1` |
| 150° | `5p/6` | `1/2` | `-s3/2` | `-s3/3` | `-s3` |
| 180° | `p` | `0` | `-1` | `0` | — |
| 210° | `7p/6` | `-1/2` | `-s3/2` | `s3/3` | `s3` |
| 225° | `5p/4` | `-s2/2` | `-s2/2` | `1` | `1` |
| 240° | `4p/3` | `-s3/2` | `-1/2` | `s3` | `s3/3` |
| 270° | `3p/2` | `-1` | `0` | — | `0` |
| 300° | `5p/3` | `-s3/2` | `1/2` | `-s3` | `-s3/3` |
| 315° | `7p/4` | `-s2/2` | `s2/2` | `-1` | `-1` |
| 330° | `11p/6` | `-1/2` | `s3/2` | `-s3/3` | `-s3` |
| 360° | `2p` | `0` | `1` | `0` | — |

`—` means the value is undefined. To "answer" it, just press **Enter** on an empty line.

---

## Known limitations (v1.1.2)

- **Prompts in Procedural and Reverse are hardcoded to `sin(...)`** — even when you choose `cos` / `tan` / `ctg` / `A`. The answer is still checked against the selected function, so this is a labelling issue only.
- **Angle mode (`A`) cannot be answered correctly in Procedural mode** — the substitution there is `p → √` instead of `p → π`, so `p/6` is turned into `√/6` and never matches `π/6`. Random mode works fine.
- **`c` is both an exit command and the `cos` alias** — typing `c` at the *Func* prompt exits the program.
- **Mistake counter is global and never displayed** — the `k` counter increments on every wrong answer but no command shows it (marked `#TODO`).
- **No "change function" command mid-session** — the only escape is `m` / `menu`, which also re-asks for the function.
- **No "final tally"** — `Remember` and normal sessions don't show a score when they end.
- **`true` / `yes` aliases are declared but unused** in this version.
- **Missing aliases from the v2.x line** — `pro` and `rem` are **not** recognized here; use `proced` / `remem`.
- **Encoding** — source uses `√`, `π`, `°`. If your editor or terminal shows garbage (`вИЪ`, `ѕА`, `¬∞`), the file has been re-encoded through Windows cp1251. Save the source as UTF-8 to fix the display.
