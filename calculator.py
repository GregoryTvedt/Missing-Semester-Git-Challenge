#!/usr/bin/env python3

OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,  # oops
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def main() -> None:
    print("calc - enter: <num> <op> <num>   (ops: + - * /)   quit to exit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if line in ("", "q", "quit", "exit"):
            break

        parts = line.split()
        if len(parts) != 3:
            print("usage: <num> <op> <num>")
            continue

        left, op, right = parts
        if op not in OPS:
            print(f"unknown op: {op}")
            continue

        try:
            a = float(left)
            b = float(right)
            result = OPS[op](a, b)
        except ZeroDivisionError:
            print("error: division by zero")
            continue
        except ValueError:
            print("error: numbers must be numbers")
            continue

        if result == int(result):
            result = int(result)
        print(result)


if __name__ == "__main__":
    main()
