import math
MAX=100000
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
sqrtMAX=math.ceil(math.sqrt(MAX))
isPrime=[0,0]+[1]*(MAX+1)
for i in range(2,sqrtMAX+1):
    if isPrime[i]==1:
        for j in range(2*i,MAX+1,i):
            isPrime[j]=0
print("Done")
for test_case in range(1, T + 1):
    n=int(input())
    for i in range(2,MAX+1-n):
        if isPrime[i]==0 and isPrime[i+n]==0:
            print(f"#{test_case} {i} {i+n}")
            break