#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    position = len(sys.argv) - 1
    for i in range(position):
        argument = sys.argv[i + 1]
        result += int(argument)
    print("{}".format(result))
        
