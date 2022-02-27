"""
치킨 배달
"""

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N => 도시의 크기, M => 치킨 집의 개수

### 도시 만들기
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

### 집과 치킨집 위치 찾기
home, chiken = [], []  # home_idx == 1, chiken_idx == 2
for city_idx, c in enumerate(city):
    for line_idx, l in enumerate(c):
        if l == 1:  # home
            home.append([city_idx, line_idx])
        elif l == 2:  # chiken
            chiken.append([city_idx, line_idx])

alive_chiken = list(combinations(chiken, M))
min_sum = float('inf')

for i in alive_chiken:
    sum = 0
    for h in home:
        sum += min([(abs(h[0]-x[0]))+(abs(h[1]-x[1])) for x in i])
    if sum < min_sum:
        min_sum = sum
print(min_sum)