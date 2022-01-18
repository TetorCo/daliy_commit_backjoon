"""
별 찍기 - 2

문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""
def star_solve(x):
    for i in range(1, x+1): # 0은 찍을 수 없기에 1부터 x+1까지 for문은 반복한다.
        for j in range(x-i):    # 맨 뒤부터 별을 찍어야 하기 때문에 앞 공간은 비워둔다.
            print(' ', end='')
        for j in range(i):  # 맨 뒤부터 하나 씩 별을 찍는다. end를 써서 줄바꿈이 되지 않게 해준다.
            print('*', end='')
        print('')
    # """format을 이용한 한 줄 코딩"""
    # for i in range(x):
    #     print('{:>5}'.format('*'*(i+1)))


if __name__ == "__main__":
    x = int(input())    # 별을 찍고 싶은 개수만큼 입력 받는다.
    star_solve(x)