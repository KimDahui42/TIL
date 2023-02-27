x=int(input())
storage=list(map(int,input().split()))

dp=[0]*100
dp[0]=storage[0]
dp[1]=storage[1]

for i in range(2,x):
    dp[i]=max(dp[i-1],dp[i-2]+storage[i])    

print(dp[x-1])

