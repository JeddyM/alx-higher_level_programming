#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1, sys

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit (1)
    #using a dictionary to map sign to function
    funcs = {"+":add, "-": sub, "*": mul, "/": div}
    if op not in list(funcs.keys()):
        print(" Unknown operator. Available operators: +, -, * and /")
        sys.exit (1)


    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, op, b, funcs[c](a, b)))
