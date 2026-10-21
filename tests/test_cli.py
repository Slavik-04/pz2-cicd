import subprocess
import sys
def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "calculator", *args],
        capture_output=True,
        text=True,
    )
def test_cli_add():
    result = run_cli("add", "2", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"
def test_cli_division_by_zero():
    result = run_cli("div", "1", "0")
    assert result.returncode == 1
    assert "Error" in result.stdout
