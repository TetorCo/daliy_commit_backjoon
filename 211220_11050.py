"""
이항 계수 1

문제
자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다

출력
이항계수를 출력한다.
"""

def upside(n, k):
    up = 1
    for i in range(n, n-k, -1):
        up *= i
    return up

def downside(n, k):
    down = 1
    for i in range(1, k+1):
        down *= i
    return down
if __name__ == "__main__":
    n, k = map(int, input().split())
    up = upside(n,k)
    down = downside(n,k)
    print(up // down)