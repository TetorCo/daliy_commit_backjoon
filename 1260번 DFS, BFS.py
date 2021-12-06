from collections import deque

n, m, v = map(int, input().split())

### 인덱스와 값을 일치시키기 위해서 n+1개를 사용한다.
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    m1, m2 = map(int, input().split())
    ### 입력된 노드 연결해주기 / 행의 숫자와 열의 숫자가 연결되어 있다는 표시를 해준다.
    graph[m1][m2] = graph[m2][m1] = 1

### 깊이 우선 탐색
def dfs(start_v, visited = []):
    visited.append(start_v)
    print(start_v, end = ' ')

    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (v not in visited):
            dfs(w, visited)

### 너비 우선 탐색
def bfs(start_v):
    visited = [start_v]
    # 리스트를 써서 pop(0)하게 되면 시간복잡도가 0(N)이다.
    # 그래서 시간복잡도가 0(1)인 deque를 사용한다.
    queue = deque()
    queue.append(start_v)
    print(f'애도 큐 : {queue}')
    # queue가 빌 때까지 반복
    while queue:
        # queue에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(f'이건 큐 : {queue}')
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in visited):
                visited.append(w)
                queue.append(w)

dfs(v)
print()
bfs(v)