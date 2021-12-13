"""
최대공약수와 최소공배수
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
"""

### 자연수 받기
a, b = map(int, input().split())

### 최대공약수
def max(a, b):
    if a == b:
        return a
    if a > b:
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    elif b > a:
        while a != 0:
            r = b % a
            b = a
            a = r
        return b

### 최소공배수
def min(a, b):
    choiso = a * b
    x = max(a, b)

    return int(choiso / x)


print(max(a, b))
print(min(a, b))