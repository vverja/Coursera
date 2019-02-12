import sys


def print_stairs():
    stairs = sys.argv[1]
    if stairs.isdigit():
        num_of_stairs = int(stairs)
        for i in range(1, num_of_stairs + 1):
            s1 = " " * (num_of_stairs - i)
            s2 = "#" * i
            print(s1 + s2)


if __name__ == '__main__':
    print_stairs()
