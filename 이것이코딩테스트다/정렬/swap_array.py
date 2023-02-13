n,k=map(int,input().split())
cnt=0
answer=0
arr_a=sorted(list(map(int,input().split())))
arr_b=sorted(list(map(int,input().split())),reverse=True)
for i in range(n):
    if cnt>=k:
        break
    if arr_a[i]<arr_b[i]:
        cnt+=1
        arr_a[i],arr_b[i]=arr_b[i],arr_a[i]
    else:
        break

print(sum(answer))

