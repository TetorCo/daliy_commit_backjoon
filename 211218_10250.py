"""
ACM 호텔
여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.

프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 

프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

풀이
층수는 N에서 건물층수를 나눈 나머지가 되고, 호수는 N에서 건물 층수를 나눈 몫 + 1이 된다.
만약 N이 건물층수의 배수인 경우에는 층수는 입력받은 층수 그대로 되고 호수는 N에서 건물층수를 나눈 몫이 된다.
"""

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    floor, room, customer = map(int, sys.stdin.readline().split())
    ### 층수 구하기
    if customer % floor == 0:
        cus_room = customer // floor
        print((floor*100) + cus_room)
    else:
        cus_floor =  customer % floor
        cus_room = (customer // floor) + 1
        print((cus_floor * 100) + cus_room)