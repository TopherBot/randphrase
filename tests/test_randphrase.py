import subprocess
import sys
from pathlib import Path


def run_randphrase(args: list[str] = None) -> subprocess.CompletedProcess:
    cmd = [sys.executable, Path(__file__).parents[2] / "randphrase.py"]
    if args:
        cmd.extend(args)
    return subprocess.run(cmd, capture_output=True, text=True)


def test_default_output():
    result = run_randphrase()
    assert result.returncode == 0
    assert result.stdout.strip() != ""


def test_custom_file(tmp_path):
    custom = tmp_path / "my_phrases.txt"
    custom.write_text("First line\nSecond line\nThird line\n", encoding="utf-8")
    result = run_randphrase(["-f", str(custom)])
    assert result.returncode == 0
    assert result.stdout.strip() in {"First line", "Second line", "Third line"}
