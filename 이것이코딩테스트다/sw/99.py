import math

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    max_num=0
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            max_num=i
    print(f"#{tc} {max_num-1+n//max_num-1}")