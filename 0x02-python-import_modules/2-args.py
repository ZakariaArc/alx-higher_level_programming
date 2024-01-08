#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]

    num_args = len(args)

    if num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
