T = 10
for test_case in range(1, T + 1):
    dump=int(input())
    arr=list(map(int,input().split()))
    front,end=0,len(arr)-1
    arr.sort()
    while dump>0:
        arr[front],arr[end]=arr[front]+1,arr[end]-1
        smaller_front,bigger_end=front,end
        dump-=1
        for i in range(0,end):
            if arr[i]<arr[front]:
                arr[i],arr[front]=arr[front],arr[i]
                break
        for i in range(end,front,-1):
            if arr[i]>arr[end]:
                arr[i],arr[end]=arr[end],arr[i]
    print(f"#{test_case} {arr[end]-arr[front]}")