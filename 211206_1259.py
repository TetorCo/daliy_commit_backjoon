"""
팰린드롬수
어떤 단어를 뒤에서부터 읽어도 똑같은 수를 말한다.
각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.
"""
import sys
def reserve_num():
    num_list = []
    while True:
        num = int(sys.stdin.readline())
        num_list.append(num)
        if num == 0:
            del num_list[-1]
            break

    for i in range(len(num_list)):
        if str(num_list[i]) == str(num_list[i])[::-1]:
            print('yes')
        else: print('no')

if __name__ == "__main__":
    reserve_num()