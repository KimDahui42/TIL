n=int(input())
array=sorted(list(map(int,input().split())))
m=int(input())
m_array=list(map(int,input().split()))

def binary_search(target):
    start,end=[0,n-1]
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return 0

for i in m_array:
    print(binary_search(i))
