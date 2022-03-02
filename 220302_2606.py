"""
바이러스
"""
import sys
input = sys.stdin.readline

def dfs(graph, value, visited):
    visited[value] = True
    for i in graph[value]:
        if not visited[i]:
            dfs(graph, i, visited)
    return visited


def bfs(graph, value, visited):
    from collections import deque
    queue = deque([value])
    print(queue)
    visited[value] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1) ]  # 1번부터 진행하기 때문에 0번 인덱스를 비워둠

    for _ in range(M):
        x, y = map(int, input().split())  # x, y는 서로 연결된 컴퓨터
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (N+1)  # 0번 노드는 사용하지 않을 거라서 +1을 해준다.

    value = 1  # 1번 컴퓨터가 감염된 경우이므로 1로 지정
    virus_list = bfs(graph, value, visited)
    virus_list = dfs(graph, value, visited)

    cnt = 0
    for bool in virus_list[2:]:  # 1번을 제외한 리스트 중에서 True만 카운트
        if bool == True:
            cnt += 1
    print(cnt)