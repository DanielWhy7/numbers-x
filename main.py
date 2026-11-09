import json
import sys
from pathlib import Path
from typing import Final

try:
  from number2x import (
    MODE_REMEMBER, MODE_RANDOM,
    TRUE_CMDS, parse_int, run_session,
    ask, ExitRequested,
  )
except ImportError:
  sys.stderr.write(
    "main.py requires number2x.py in the same directory.\n"
    "On systems without a writable filesystem, "
    "run number2x.py directly.\n"
  )
  raise SystemExit(1)

VERSION: str = "2.1.0"
SEPARATOR: str = "_______________________________"
GREEN: str = "\033[32m"
RED: str = "\033[31m"
RESET: str = "\033[0m"

CONFIG_PATH: Final = (
  Path(__file__).resolve().parent / "config.json")
DEFAULTS: Final = {
  "min": 2, "max": 10, "mode": "p",
  "error_fix": False, "skip_zero": False,
  "total_mistakes": 0,
}


def load_config() -> dict:
  """Load saved config, merged over defaults."""
  try:
    return {**DEFAULTS, **json.loads(CONFIG_PATH.read_text())}
  except (FileNotFoundError, json.JSONDecodeError, OSError):
    return dict(DEFAULTS)


def save_config(cfg: dict) -> None:
  """Persist config. Silently skip on read-only FS."""
  try:
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))
  except OSError:
    pass


def colored_output(text: str) -> None:
  """v1.4.2-style: leading space, [+] green, [-] red."""
  body = " " + text
  if "Correct" in text:
    print(GREEN + body + RESET)
  elif "Wrong" in text:
    print(RED + body + RESET)
  elif "Mode changed" in text:
    print(body + "\n")   # blank line after (v1.4.2 look)
  else:
    print(body)


def prompt_int(label: str, default: int) -> int:
  """Ask for int. Empty -> default. Garbage -> 11."""
  raw = ask(f"{label} [{default}]: ").strip()
  return default if not raw else parse_int(raw)


def prompt_choice(label: str, default: str) -> str:
  """Ask for a mode token. Empty -> default."""
  raw = ask(f"{label} [{default}]: ").strip().lower()
  return raw or default


def prompt_yes(prompt: str, default: bool) -> bool:
  """Ask yes/no. Empty -> default. Truthy -> True."""
  hint = "Y" if default else "N"
  raw = ask(f"{prompt} [{hint}]: ").strip().lower()
  return default if not raw else raw in TRUE_CMDS


def main() -> None:
  """Advanced CLI with persisted config and colors."""
  cfg = load_config()

  print(f"\nSquare Number X | Version: {VERSION}")
  print(f"{SEPARATOR}\n")

  while True:
    lo = prompt_int("Enter minimum", cfg["min"])
    hi = prompt_int("Enter maximum", cfg["max"])
    if lo > hi:
      lo, hi = hi, lo

    mode = prompt_choice(
      "\nProcedural | Random | Reverse | Remember"
      "\nMode",
      cfg["mode"],
    )

    skip_zero = error_fix = False
    if mode in MODE_RANDOM:
      skip_zero = prompt_yes(
        "\nSkip multiples of 10\nEnable",
        cfg["skip_zero"],
      )
    elif mode not in MODE_REMEMBER:
      error_fix = prompt_yes(
        "\nError corrector\nEnable",
        cfg["error_fix"],
      )

    print(SEPARATOR + "\n")

    if mode in MODE_REMEMBER:
      for n in range(lo, hi + 1):
        print(f"{n}x{n}: {n ** 2}")
      continue

    mistakes = run_session(
      lo, hi, mode,
      error_fix=error_fix,
      skip_zero=skip_zero,
      output_fn=colored_output,
    )
    cfg.update(
      min=lo, max=hi, mode=mode,
      error_fix=error_fix, skip_zero=skip_zero,
      total_mistakes=cfg["total_mistakes"] + mistakes,
    )
    save_config(cfg)


if __name__ == '__main__':
  try:
    main()
  except (KeyboardInterrupt, EOFError, ExitRequested):
    print("\nGoodbye.")
