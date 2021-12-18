"""
수 정렬하기 3

문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
import sys

n = int(input())
num_list = [0] * 10001 # 길이가 10,000인 리스트 생성

for _ in range(n):
    num = int(sys.stdin.readline())
    num_list[num] += 1 # 입력받은 값은 수 만큼 index에 +1

for n in range(len(num_list)):
    if num_list[n] != 0: # 만약 해당 index의 값이 0이 아니라면 해당 index의 값만큼 index 출력
        for _ in range(num_list[n]):
            print(n)
"""
풀이
입력받는 숫자가 0 부터 10,000 사이의 숫자만 입력 받는다.
먼저, 0으로 가득차있는 길이가 10,000인 list를 만들고 입력 받는 수를 index 값으로 하여 
해당 index의 값을 +1씩 증가해주고 해당 리스트를 반복문으로 돌면서 0이 아닌 값의 index를
들어 있는 값 만큼 출력해주면 된다.
"""