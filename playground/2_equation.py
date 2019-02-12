import sys


def solution():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    D = b**2 - 4 * a * c
    r1 = r2 = 0
    if D > 0:
        r1 = (-b - (D) ** 0.5) / (2 * a)
        r2 = (-b + (D) ** 0.5) / (2 * a)
    elif D == 0:
        r1, r2 = -b / 2 * a
    else:
        r1, r2 = None
    print(int(r1))
    print(int(r2))


if __name__ == '__main__':
    solution()
