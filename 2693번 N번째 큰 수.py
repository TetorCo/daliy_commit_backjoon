def arr():
    num = int(input())
    total = []
    for _ in range(num):
        total.append(list(map(int, input().split())))
    return total

if __name__ == "__main__":
    sort_list = arr()
    for idx in range(len(sort_list)):
        re_list = sorted(sort_list[idx], reverse = True)
        print(re_list[2])