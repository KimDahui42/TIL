n=int(input())
array=list(map(int,input().split()))
sorted_array=sorted(list(set(array)))

def binarySearch(target):
    start,end=[0,len(sorted_array)-1]
    while start<=end:
        mid=(start+end)//2
        if sorted_array[mid]==target:
            return mid
        elif sorted_array[mid]<target:
            start=mid+1
        else:
            end=mid-1

for i in array:
    print(binarySearch(i), end=' ')


