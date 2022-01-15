"""
프린터 큐

문제
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

입력
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

출력
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
"""

import sys
from collections import deque

def print_que_solve(imp, idx_imp, m):
    cnt = 0
    while True:
        top = max(imp) # imp에서 제일 큰 값
        if imp[0] != top: # imp의 첫번째 값과 top가 같지 않다면
            imp.append(imp.popleft()) # imp의 첫번째 값을 맨 뒤로 옳겨준다.
            idx_imp.append(idx_imp.popleft()) # imp의 첫번째 값 인덱스도 맨 뒤로 옳겨준다.
        else: # imp의 첫 번째 값과 top가 같다면
            cnt += 1 # 문서가 나오는 순서
            imp.popleft() # imp의 제일 첫 번째 값
            if idx_imp.popleft() == m: # idx_imp의 첫 번째 값과 궁금한 문서가 같을 경우
                return cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    test_case = int(input())

    for _ in range(test_case):
        n, m = map(int, input().split()) # N은 문서의 개수, M은 궁금한 문서의 현재 위치
        importance = deque(list(input().split())) # n개 문서의 중요도
        idx_imp = deque(list(range(n))) # 기존 문서의 인덱스
        print(print_que_solve(importance, idx_imp, m))

"""
풀이
즁요한 점은 코드가 진행되면 기존의 큐가 섞여버리기 때문에 idx_imp를 만들어서 내가 궁금한 문서의
현재 위치도 같이 움직이면서 찾을 수 있게 하는 것이다.
"""