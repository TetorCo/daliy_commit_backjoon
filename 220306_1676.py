"""
팩토리얼 0의 개수

문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
"""
import sys
input = sys.stdin.readline

def solve(n):
    if n == 0:
        return 0
    if n == 1:
        return n
    return n * solve(n-1)


if __name__ == "__main__":
    import math
    N = int(input())
    zero = 0
    # search_zero = list(str(solve(N)))  # 이건 95%에서 에러가 뜨고
    fac_zero = list(str(math.factorial(N)))  # lib를 사용했을 때는 통과가 된다...
    pos = True
    length = len(fac_zero)-1

    while pos:
        if length < 0:
            break
        if fac_zero[length] == '0':
            zero += 1
            length -= 1
        else:
            break
    print(zero)