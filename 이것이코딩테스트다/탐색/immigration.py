n=6
times=[7,10]

def solution(n,times):
    answer=0
    array=[[],[]]

    for i in range(len(times)):
        array[0].append(0) # 진입 시점
        array[1].append(False) # 현재 심사받는 사람이 있는지

    def findMin():
        minVal=0
        start,end=[0,len(times)-1]
        while start<=end:
            mid=(start+end)//2
            


        return minVal

    return answer

print(solution(n,times))