#argparse is a built-in Python module used to create command-line interfaces.
#it lets your Python script accept inputs from the command line
#python argparse_tutorial.py --number2 4 --operation add

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
#Anything we pass in argument will be in the form of string only.
# There are 2 types of argument: positional and optional. Number1 is positional and Number2 is optional
#we can skip optional arguments but not positional.
    parser.add_argument("number1", help="First number")
    parser.add_argument("--number2", help="Second number")
    parser.add_argument("operation", help="operation")

    args = parser.parse_args()

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "subtract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2

    print("Result:", result)

    print(args.number1)
    print(args.number2)
    print(args.operation)

