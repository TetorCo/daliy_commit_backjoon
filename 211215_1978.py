"""
소수 찾기
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
"""
import sys

### N개 수와 소수 입력받기
n = int(input())
so = list(map(int, sys.stdin.readline().split()))

def sosu(i):
    if i == 1:
        return False
    elif i == 2:
        return True
    for m in range(2, i):
        if i % m == 0:
            return False
    return True

if __name__ == "__main__":
    cnt = 0
    for i in so:
        if sosu(i):
            cnt += 1
    print(cnt)