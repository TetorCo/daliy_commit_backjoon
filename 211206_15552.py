import sys

def solve():
    num = int(input()) # 반복할 숫자를 입력
    num_list = []      # 더할 숫자를 받을 리스트 입력
    for i in range(num):
        input = sys.stdin.readline().split()
    num_list.append(list(map(int, input)))

    for i in range(len(num_list)):
        sum = num_list[i][0] + num_list[i][1]
    print(sum)

if __name__ == "__main__":
    solve()