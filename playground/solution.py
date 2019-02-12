import sys


def sum_digits():
    rezult = 0
    digit = sys.argv[1]
    if digit.isdigit():
        for i in digit:
            rezult += int(i)
    return rezult


if __name__ == '__main__':
    print(sum_digits())
