import math
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    arr=list(map(int,input().split()))
    size=len(arr)
    cnt=0
    for i in range(2,size-2):
        if arr[i-2]<arr[i] and arr[i-1]<arr[i] and arr[i+1]<arr[i] and arr[i+2]<arr[i]:
            cnt+=arr[i]-max(arr[i-2],max(arr[i-1],max(arr[i+1],arr[i+2])))

    if arr[0]>arr[1] and arr[0]>arr[2]:
        cnt+=arr[0]-max(arr[1],arr[2])
    if arr[1]>arr[0] and arr[1]>arr[2] and arr[1]>arr[3]:
        cnt+=arr[1]-max(arr[0],max(arr[2],arr[3]))
    if arr[size-2]>arr[size-1] and arr[size-2]>arr[size-3] and arr[size-2]>arr[size-4]:
        cnt+=arr[size-2]-max(arr[size-4],max(arr[size-3],arr[size-1]))
    if arr[size-1]>arr[size-2] and arr[size-1]>arr[size-3]:
        cnt+=arr[size-1]-max(arr[size-2],arr[size-3])

    print(f"#{test_case} {cnt}")