#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if(length - 1 == 0):
        print("{} arguments".format(length - 1))
    elif(length - 1 == 1):
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
