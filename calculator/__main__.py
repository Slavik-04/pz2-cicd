"""Консольный запуск: python -m calculator <add|sub|mul|div> <a> <b>."""
import sys
from calculator.core import add, subtract, multiply, divide
OPERATIONS = {"add": add, "sub": subtract, "mul": multiply, "div": divide}
def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 3 or argv[0] not in OPERATIONS:
        print("Usage: python -m calculator <add|sub|mul|div> <a> <b>")
        return 2
    operation, a, b = argv[0], float(argv[1]), float(argv[2])
    try:
        print(OPERATIONS[operation](a, b))
    except ValueError as error:
        print(f"Error: {error}")
        return 1
    return 0
if __name__ == "__main__":
    sys.exit(main())
