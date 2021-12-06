def num_list():
    total = []
    for num in range(1, 1001):
        total.extend([num] * num)
    return total

if __name__ == "__main__":
    start, end = map(int, input().split())
    sum = 0
    for n in num_list()[start - 1:end]:
        sum += n
    print(sum)