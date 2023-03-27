x=int(input())
dp=[0]*1000001
dp[2]=1
dp[3]=1
for i in range(2, x+1):
    if dp[i]==0:
        dp[i]=dp[i-1]+1
    if i+1<=x:
        if dp[i+1]==0 or dp[i+1]>dp[i]+1:
            dp[i+1]=dp[i]+1
    if i*2<=x:
        if dp[i*2]==0 or dp[i*2]>dp[i]+1:
            dp[i*2]=dp[i]+1
    if i*3<=x:
        if dp[i*3]==0 or dp[i*3]>dp[i]+1:
            dp[i*3]=dp[i]+1

print(dp[x])
    