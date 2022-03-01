"""
1로 만들기
"""
import sys
input = sys.stdin.readline

def make_one(x, dp):
    if x < 4:  # x가 4이하 일경우 사전에 정의해놓은 dp list에서 슬라이싱을 이용해서 값을 구한다.
        dp = dp[:x+1]
        return dp[-1]

    for i in range(4, x+1):
        ## 1로 뺐을 때의 경우
        dp.append(dp[i-1]+1)

        ## 2로 나누어 질때의 경우 앞서 1로 뺐을 때의 경우와 비교해서 최솟값을 dp[i]에 넣어준다.
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        """+1을 해주는 이유 : 예를 들어서 5가 1이 되는 수가 3이고,
        10은 먼저 2로 나눈 후에 5가 1이 되는 수를 보는 것이 때문에 1을 더해주어야 한다."""

        ## 3으로 나누어 질때의 경우 앞서 최솟 값과 비교해서 dp[i]에 넣어준다.
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        """ 9 => 3 => 1 // 10 => 9 => 3 => 1 """
    return dp[-1]


if __name__ == "__main__":
    x = int(input())
    dp = [0, 0, 1, 1]  # 기본 값 지정
    print(make_one(x, dp))