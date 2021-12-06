### 회의 수와 시간들을 담을 리스트 생성
n = int(input())
use = []

### 회의시간을 입력받아서 use리스트에 저장
for i in range(0, n):
    start, end = map(int, input().split())
    use.append([start, end])

### 입력받은 리스트를 회의 시작 시간과 끝나는 시간으로 정렬
use = sorted(use, key=lambda x: (x[0]))
print(use)
use = sorted(use, key=lambda x: (x[1]))
print(use)

### 회의를 할 수 있는 count와 회의가 끝나는 시간을 담을 last 생성
count = 0
last = 0

### 만약에 회의 시작 시간이 last와 같거나 크다면 회의 수를 늘려주고 끝나는 시간을 바꿔줌
for i, j in use:
    if i >= last:
        count += 1
        last = j
print(count)