"""
1. x가 5로 나누어떨어지면 5로 나눈다.
2. x가 3으로 나누어떨어지면, 3으로 나눈다.
3. x가 2로 나누어떨어지면, 2로 나눈다.
4. x에서 1을 뺀다.
"""
x=int(input())
dp=[0]*(x+1)

for i in range(1,x+1):
    current=dp[i-1]
    if dp[i]==0:
        dp[i]=dp[i-1]+1
    if i*2<=x:
        if dp[i*2]==0 or dp[i*2]<dp[i-1]+1:
            dp[i*2]=dp[i-1]+1
    if i*3<=x:
        if dp[i*3]==0 or dp[i*3]<dp[i-1]+1:
            dp[i*3]=dp[i-1]+1
    if i*5<=x:
        if dp[i*5]==0 or dp[i*5]<dp[i-1]+1:
            dp[i*5]=dp[i-1]+1

print(dp[x])
    