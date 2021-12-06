def sosu():
    n = int(input())
    m = int(input())
    sosu_list = []
    sum_sosu = 0
    count = 0

    for sosu in range(n, m+1):
        for i in range(1, sosu+1):
            if sosu % i == 0:
                count += 1
            if count > 2:
                break
        if count == 2:
            sosu_list.append(sosu)
        count = 0

    if len(sosu_list) == 0:
        print('-1')
    else:
        print(sum(sosu_list))
        print(min(sosu_list))

if __name__ == "__main__":
    sosu()