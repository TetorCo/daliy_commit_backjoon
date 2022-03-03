"""
빗물
"""
import sys
input = sys.stdin.readline

## 세로, 가로
H, W = map(int, input().split())

block = list(map(int, input().split()))
total = 0

for i in range(1, W-1):
    left = max(block[:i])  # 현재 index에서 왼쪽에 가장 높은 건물
    right = max(block[i:])  # 현재 index에서 오른쪽에 가장 높은 건물

    # left와 right에서 더 낮은 건물 높이와 현재 index의 높이를 빼준다. / 음수가 나올경우 0을 더해줌.
    total += max(0, min(left, right)-block[i])
print(total)