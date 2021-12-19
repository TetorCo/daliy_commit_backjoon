import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))
    max_num = max(num)
    num.remove(max_num)
    if sum(num) == 0:
        break
    if (num[0] * num[0]) + (num[1] * num[1]) == max_num*max_num:
        print("right")
    else: print("wrong")