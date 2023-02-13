n=int(input())
array=[]
for i in range(n):
    temp=input().split()
    array.append((temp[0],temp[1]))

def setting(data):
    return data[1]

sorted_array=sorted(array,key=setting)

for i in sorted_array:
    print(i[0],end=' ')

