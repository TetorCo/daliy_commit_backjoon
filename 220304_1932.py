"""
정수 삼각형
"""
import sys
input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    v = list(map(int, input().split()))
    graph.append(v)
# print(graph)

for i in range(len(graph)-2, -1, -1):
    for v in range(0, len(graph[i])):
        graph[i][v] += max(graph[i+1][v:v+2])
print(graph[0][0])