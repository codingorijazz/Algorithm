import sys

data = sys.stdin.read().splitlines()
for line in data:
    A, B = map(int, line.split())
    print(A+B)