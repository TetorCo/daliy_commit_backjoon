### 시험장 수
n = int(input())

### 각 시험장의 응시자 수
tester = list(map(int, input().split())) # 입력받은 수를 리스트로 저장

### 총감독관과 부감독관이 응시자를 감시할 수 있는 수
b, c = map(int, input().split())

### 각 시험장마다 응시자를 모두 감독하기 위한 최소 수
total = n # 시험장마다 총감독관은 있어야한다.

for t in tester:
    if t - b < 0: # 총감독관 수로 모든 응시자를 감시할 수 있는 경우
        continue
    else:
        ### 부감독관이 감시해야하는 응시자수
        if (t - b) % c != 0: # 부감독관이 한 명 더 필요한 경우
            total += (t -b) // c + 1
        else:
            total += (t - b) // c
print(total)