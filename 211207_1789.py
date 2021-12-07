"""
수들의 합
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 떄 자연수 N의 최댓값은?
"""
def num_sum():
    num = int(input())
    n = 1
    while n * (n + 1) / 2 <= num:
        n += 1
    print(n-1)

if __name__ == "__main__":
    num_sum()