"""
미로 탐색
"""
import sys
from collections import deque
input = sys.stdin.readline

## bfs
def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        ## 만약 좌표 끝에 왔다면 visited 출력
        if x == N-1 and y == M-1:
            return visited[x][y]
        ## 상하좌우 확인
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            ## graph에 벗어나지 않을 경우
            if 0 <= nx < N and 0 <= ny < M:
                ## 방문 배열이 0이고, graph가 1일 때 방문 배열 업데이트 후 queue에 현재 위치 추가
                if visited[nx][ny] == 0 and graph[x][y] == '1':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

if __name__ == "__main__":
    ## 세로, 가로
    N, M = map(int, input().split())

    ## 붙어서 입력되기 때문에 띄워서 2차원 배열로 만들기
    graph = []
    for _ in range(N):
        miro = input().rstrip()
        miro = list(''.join(miro))
        graph.append(miro)

    ## 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ## 방문한 배열 만들기
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1

    print(bfs(0, 0, visited))