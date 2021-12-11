"""
스택
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""
# 출력해야하는 명령 함수
class stack():
    def __init__(self):
        self.stack = []


    def push(self, num):
        self.stack.append(num)


    def pop(self):
        if len(self.stack) == 0: print(-1)
        else:
            print(self.stack.pop())


    def size(self):
        print(len(self.stack))


    def empty(self):
        if len(self.stack) == 0: print(1)
        else: print(0)


    def top(self):
        if len(self.stack) == 0: print(-1)
        else: print(self.stack[-1])


if __name__ == "__main__":
    import sys
    # 명령의 개수
    n = int(sys.stdin.readline())
    s = stack()


    for _ in range(n):
        order = sys.stdin.readline().split()
        if order[0] == 'push':
            s.push(order[1])
        elif order[0] == 'pop':
            s.pop()
        elif order[0] == 'size':
            s.size()
        elif order[0] == 'empty':
            s.empty()
        elif order[0] == 'top':
            s.top()