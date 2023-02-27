import sys
n=int(input())
array=sorted(list(map(int,input().split())))
m=int(input())
array_m=list(map(int,input().split()))
answer=[]
def binary_search(target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return False

for item in array_m:
    if binary_search(item,0,n-1):
        answer.append("yes")
    else:
        answer.append("no")

print((' ').join(answer))


