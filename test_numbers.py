import pytest
from number2x import (
  next_number, parse_int, ask, run_session,
  ExitRequested,
)


def test_next_number_procedural():
  assert next_number("p",  1, 1, 10) == 2
  assert next_number("p", 10, 1, 10) == 1
  assert next_number("p",  0, 1, 10) == 1


def test_next_number_reverse():
  assert next_number("e", 10, 1, 10) == 9
  assert next_number("e",  1, 1, 10) == 10


def test_next_number_random_in_range():
  for _ in range(100):
    n = next_number("r", 0, 5, 15)
    assert 5 <= n <= 15


def test_next_number_skip_zero():
  for _ in range(100):
    assert next_number("r", 0, 1, 100, True) % 10 != 0


def test_next_number_skip_zero_empty_pool():
  assert next_number("r", 0, 10, 10, True) == 10


def test_parse_int_valid():
  assert parse_int("42") == 42
  assert parse_int("-5") == -5
  assert parse_int("+5") == 5
  assert parse_int(" 5 ") == 5


def test_parse_int_fallback():
  assert parse_int("abc") == 11
  assert parse_int("") == 11
  assert parse_int("²") == 11
  assert parse_int("½") == 11
  assert parse_int("9" * 5000) == 11


def test_ask_raises_on_exit():
  for cmd in ("q", "Q", "exit", "EXIT", "escape"):
    with pytest.raises(ExitRequested):
      ask("", input_fn=lambda _: cmd)


def test_ask_returns_regular_input():
  assert ask("", input_fn=lambda _: "hello") == "hello"


def test_run_session_counts_mistakes():
  answers = iter(["3", "4", "menu"])   # wrong → right → break
  out = []
  mistakes = run_session(
    2, 2, "p",
    input_fn=lambda _: next(answers),
    output_fn=out.append,
  )
  assert mistakes == 1
  assert any("Wrong" in s for s in out)
  assert any("Correct" in s for s in out)
