"""
분해합

문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
"""
def solve(n):
    result = 0
    for num in range(1, n+1):
        n_list = list(map(int, str(num)))
        result = num + sum(n_list)
        if n == result:
            return num
        if n == num:
            return 0


if __name__ == "__main__":
    n = int(input())
    print(solve(n))

"""
풀이
1부터 입력 받은 값을 반복하면서 str 함수로 list로 만들어줌
만약에 num과 입력 받은 n_list의 합이 n과 같을 경우 return num
입력값과 num이 같다면 0 출력
"""