"""
수 찾기

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
import sys
input = sys.stdin.readline

### N 입력 받기
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()


### M 입력 받기
m = int(input())
m_list = list(map(int, input().split()))


### 최종 출력
length = len(n_list)
for m in m_list:
    left = 0
    right = length-1
    cnt = 0
    while left <= right:
        mid = (left+right) // 2
        if n_list[mid] == m:
            print(1)
            cnt += 1
            break
        elif n_list[mid] > m:
            right = mid - 1
        else:
            left = mid + 1
    if cnt != 1:
        print(0)