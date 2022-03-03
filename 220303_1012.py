"""
유기농 배추
"""
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y, stack):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 1:
        if not (x, y) in stack:
            stack.append((x, y))
            dfs(x-1, y, stack)
            dfs(x, y-1, stack)
            dfs(x+1, y, stack)
            dfs(x, y+1, stack)
            return True
    return False


if __name__ == "__main__":
    ## Test case
    T = int(input())

    for _ in range(T):
        ## 세로, 가로, 배추의 수
        N, M, K = map(int, input().split())

        ## 밭
        graph = [[0]*M for _ in range(N)]
        # for i in graph:
        #     for j in i:
        #         print(j, end=' ')
        #     print()

        ## 배추의 위치
        for _ in range(K):
            x, y = map(int, input().split())
            graph[x][y] = 1


        stack = []
        result = 0
        for x in range(N):
            for y in range(M):
                if dfs(x, y, stack) == True:
                    result += 1
        print(result)