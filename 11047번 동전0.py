n, k = map(int, input().split())
d = []

for i in range(0, k):
    d.append(int(input()))
d.reverse()

count = 0
for coin in d:
    count += n // coin
    print(count)
    n %= coin
print(f'총 사용한 갯수 : {count}')