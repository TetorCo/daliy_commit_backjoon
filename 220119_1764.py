"""
듣보잡

문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.
"""
"""
1. N과 M을 입력받는다.
2. Counter을 사용해서 중복된 값을 찾아낸다.
3. value가 1이상의 값만 출력한다.
"""

def solve(n, m):
    from collections import Counter

    h_list = []
    for _ in range(n+m):
        x = input().rstrip()
        h_list.append(x)

    c = Counter(h_list)

    result = []
    for key, value in c.items():
        if value > 1:
            result.append(key)

    result.sort()
    return len(result), result


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    num, name = solve(N, M)

    print(num)
    for na in name:
        print(na)