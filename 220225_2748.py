"""
피보나치 수 2 By DP
"""

def fibo(n):
    temp, cur, pre = 0, 1, 1
    for num in range(3, n+1):
        temp = cur
        cur = pre+cur
        pre = temp
        # print(cur, pre, temp)

    # ans = fibo(n-1) + fibo(n-2) # memo 시간 초과

    return cur


if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())

    print(fibo(n))