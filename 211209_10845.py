"""
큐
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""

import sys

n = int(sys.stdin.readline().rstrip())
que = []
for _ in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        que.append(order[1])
    elif order[0] == 'pop':
        if len(que) != 0:
            print(que.pop(0))
        else: print(-1)
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if len(que) == 0:
            print(1)
        else: print(0)
    elif order[0] == 'front':
        if que:
            print(que[0])
        else: print(-1)
    elif order[0] == 'back':
        if que:
            print(que[-1])
        else: print(-1)