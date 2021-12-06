def yaksu():
    n, k = map(int, input().split())
    results = []

    for i in range(1, n+1):
        if n % i == 0:
            results.append(i)
    if len(results) < k:
        print(0)
    else: print(results[k-1])

if __name__ == "__main__":
    yaksu()