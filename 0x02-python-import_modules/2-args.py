#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    position = len(sys.argv) - 1
    if position == 0:
        print("0 arguments.")
    elif position == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(position))
    for i in range(position):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
