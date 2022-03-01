"""
괄호의 값
"""
import sys
input = sys.stdin.readline

input_string = input().rstrip()
stack = []
temp = 1
result = 0

for s in range(len(input_string)):
    if input_string[s] == '(':
        stack.append(input_string[s])
        temp *= 2
    elif input_string[s] == '[':
        stack.append(input_string[s])
        temp *= 3
    elif input_string[s] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if input_string[s-1] == '(':
            result += temp
        temp = temp // 2
        stack.pop()
    else:
        if not stack or stack[-1] != '[':
            result = 0
            break
        if input_string[s-1] == '[':
            result += temp
        temp = temp // 3
        stack.pop()

if stack:
    result = 0
print(result)