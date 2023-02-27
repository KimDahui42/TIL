n=int(input())
dp=[0]*1000
"""
아래의 타일을 이용해 바닥을 채우는 모든 경우의 수
1. 1*2
2. 2*1
3. 2*2
"""
dp[0]=1
dp[1]=3
dp[2]=5

for i in range(3,n):
    dp[i]=(dp[i-2]*2+dp[i-1])%796796

print(dp[n-1])
