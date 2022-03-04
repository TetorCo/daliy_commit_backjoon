"""
일곱 난쟁이
"""
import sys
input = sys.stdin.readline

def solve(key):
    for i in range(len(key)-1, -1, -1):
        point = key[i]
        for j in key[:i]:
            search = key_sum - 100 - point
            if j == search:
                key.remove(j)
                key.remove(point)
                return key


if __name__ == "__main__":
    key = []
    for _ in range(9):
        key.append(int(input()))

    key_sum = sum(key)
    key.sort()

    for v in solve(key):
        print(v)