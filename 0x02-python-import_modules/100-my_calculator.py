#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)
    if length != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    if sys.argv[2] == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif sys.argv[2] == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif sys.argv[2] == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif sys.argv[2] == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
