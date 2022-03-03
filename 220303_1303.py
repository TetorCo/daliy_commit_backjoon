"""
전쟁 - 전투

문제
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
"""
from collections import deque
import sys
input = sys.stdin.readline

## 상, 하, 좌, 우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, status):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 'visited'  # 방문한 위치는 재방문 안하게 바꿔준다.
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] != 'visited' and graph[nx][ny] == status:
                    graph[nx][ny] = 'visited'
                    queue.append((nx, ny))
                    cnt += 1
    return cnt + 1



if __name__ == "__main__":
    ## 가로, 세로
    N, M = map(int, input().split())

    graph = [list(input().strip()) for _ in range(M)]

    white, blue = 0, 0

    for x in range(M):
        for y in range(N):
            if graph[x][y] != 'visited':
                if graph[x][y] == 'W':
                    white += bfs(x, y, 'W')**2
                elif graph[x][y] == 'B':
                    blue += bfs(x, y, 'B')**2
    print(white, blue)