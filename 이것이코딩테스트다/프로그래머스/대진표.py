import math
def solution(n,a,b):
    answer = 0
    if math.ceil(a/2)==math.ceil(b/2):
        return 1
    while True:
        if n//2<=a and n//2>b or n//2>a and n//2<b:
            while n!=pow(answer,2):
                answer+=1
        break
        n//=2

    return answer

solution(