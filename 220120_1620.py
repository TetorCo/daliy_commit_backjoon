"""
나는야 포켓몬 마스터 이다솜
"""
"""
1. 첫번째줄 도감에 수록되어있는 포켓몬의 개수 N과 맞춰야 하는 문제의 개수 M을 입력받는다.
2. 두번째줄 N개의 줄에 포켓몬의 번호가 1 ~ N번까지 포켓몬을 입력받는다.
3. M개의 줄에는 맞춰야 하는 문제를 입력 받는다. 알파벳으로 들어오면 번호를 말해야 하고 번호가 들어오면
해당하는 문자를 출력해준다.
"""
import sys

def solve(pocketmon_num, quiz_num):
    pk = {} # 포켓몬 번호와 이름을 담을 리스트 생성 / key : pocketmon_num, value : name
    for n in range(1, pocketmon_num+1):
        name = input().rstrip()
        n = str(n)
        pk[n] = name # 번호와 이름을 리스트에 추가

    rever_pk = dict(map(reversed, pk.items()))  # key : name, value : pocketmon_num

    for _ in range(quiz_num):
        quiz = input().rstrip()
        try:
            int(quiz)   # 입력 받은 값이 숫자일 경우 / pk의 key일 경우
            print(pk[quiz])
        except: # 입력 받은 값이 문자일 경우 / pk의 value일 경우
            print(rever_pk[quiz])


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    solve(N, M)