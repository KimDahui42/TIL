n,m,l=list(map(int,input().split()))
rest_map=sorted(list(map(int,input().split())))
interval_map=sorted([rest_map[0]]+[rest_map[i]-rest_map[i-1] for i in range(1,n)]+[l-rest_map[n-1]])

def binary_search(target):
    start,end=[0,len(interval_map)-1]
    while start<=end:
        mid=(start+end)//2
        if interval_map[mid]==target:
            return mid
        elif interval_map[mid]>target and interval_map[mid-1]<target:
            return mid-1
        elif interval_map[mid]<target and interval_map[mid+1]>target:

for _ in range(m+1):
    max=interval_map.pop(len(interval_map)-1)
    if max%2==0:
        
