#########################################################
# Square Number X V2.0.0
#########################################################
from random import randint as rint
from typing import Callable, Final

SEPARATOR = "_______________________________"

# public command groups (main.py may use them)
MODE_PROCEDURAL: Final = (
  'p', 'pro', 'proced', 'procedural')
MODE_RANDOM: Final = (
  'r', 'ran', 'rand', 'random', 'rng')
MODE_REVERSE: Final = ('e', 'rev', 'reverse')
MODE_REMEMBER: Final = (
  'qr', 'rem', 'remem', 'remember')

TRUE_CMDS: Final = (
  't', 'true', '1', 'y', 'yes', 'yeah',
  'ye', 'sure')
EXIT_CMDS: Final = (
  'q', '^c', 'exit', 'break', 'ctrl+c',
  'escape', 'ctrlc')
MENU_CMDS: Final = (
  'menu', 'configuration', 'home', 'm')
ERROR_CMDS: Final = ('er', 'error', 'mistake')


class ExitRequested(Exception):
  """User typed an exit command."""


def ask(
  prompt: str,
  input_fn: Callable[[str], str] = input,
) -> str:
  """Read input. Raise ExitRequested on an exit cmd."""
  text = input_fn(prompt)
  if text.lower() in EXIT_CMDS:
    raise ExitRequested
  return text


def parse_int(
  """Parse text as int, or return default.
  Accepts sign and whitespace (e.g. '-5', '+5')."""
  text: str, default: int = 11) -> int:
  try: return int(text)
  except ValueError: return default


def next_number(
  mode: str, prev: int, lo: int, hi: int,
  skip_zero: bool = False) -> int:
  """Return the next number to quiz on.
  Pure, no I/O, no state."""
  if mode in MODE_RANDOM:
    if skip_zero:
      pool = [
        n for n in range(lo, hi + 1)
        if n % 10 != 0]
      if pool:
        return pool[rint(0, len(pool) - 1)]
    return rint(lo, hi)
  if mode in MODE_REVERSE:
    return prev - 1 if prev > lo else hi
  return prev + 1 if prev < hi else lo


def run_session(
  lo: int, hi: int, mode: str, *,
  error_fix: bool = False,
  skip_zero: bool = False,
  input_fn: Callable[[str], str] = input,
  output_fn: Callable[[str], None] = print,
) -> int:
  """Run one quiz session. Return mistake count."""
  mistakes, prev = 0, lo - 1
  while True:
    number = next_number(
      mode, prev, lo, hi, skip_zero)
    prev = number
    correct = number ** 2
    answer = ask(
      f"{number}x{number}: ",
      input_fn).lower()

    if answer == str(correct):
      output_fn("[+] Correct.")
    elif answer in MENU_CMDS:
      output_fn("[*] Mode changed")
      break
    elif answer in ERROR_CMDS:
      output_fn(f"[*] Mistakes: {mistakes}")
    else:
      mistakes += 1
      output_fn(
        f"[-] Wrong. Right answer is {correct}")
      if error_fix:
        prev = lo - 1
  return mistakes


# standalone entry point
# (what runs on a restricted system)
def main() -> None:
  """Minimal CLI. Runs anywhere Python 3.8+."""
  print("\nSquare Number X\n")
  while True:
    lo = parse_int(ask("Enter minimum: "))
    hi = parse_int(ask("Enter maximum: "))
    if lo > hi:
      lo, hi = hi, lo

    mode = ask(
      "\nProcedural | Random | Reverse"
      " | Remember\nMode: ").lower()
    skip_zero = error_fix = False

    if mode in MODE_RANDOM:
      skip_zero = ask(
        "\nSkip multiples of 10\nEnable: "
      ).lower() in TRUE_CMDS
    elif mode not in MODE_REMEMBER:
      error_fix = ask(
        "\nError corrector\nEnable: "
      ).lower() in TRUE_CMDS

    print(SEPARATOR + "\n")

    if mode in MODE_REMEMBER:
      for n in range(lo, hi + 1):
        print(f"{n}x{n}: {n ** 2}")
      continue

    run_session(
      lo, hi, mode, error_fix=error_fix,
      skip_zero=skip_zero)
    print(SEPARATOR + "\n")


if __name__ == '__main__':
  try:
    main()
  except (KeyboardInterrupt, EOFError,
          ExitRequested):
    print("\n^c executed.")
