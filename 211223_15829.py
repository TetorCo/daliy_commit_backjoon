"""
Hashing

입력
첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.

입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.

출력
문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.
"""
import sys

def solve(abc_str):
    result = 0
    for i in range(len(abc_str)):
        result += (ord(abc_str[i])-96) * (31 ** i)
    return result % 1234567891

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    abc_str = list(input().rstrip()) # 입력 값 리스트
    print(solve(abc_str))