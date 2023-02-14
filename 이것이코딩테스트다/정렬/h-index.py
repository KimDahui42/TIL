def solution(citations):
    #자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후, 
    # 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.
    answer = 0
    array=sorted(citations,reverse=True)
    if len(array)==1:
        if array[0]==0:
            return 0
        else:
            return 1
    for i,val in enumerate(array):
        index=i+1
        print(index,val)
        if index==val:
            return index
        if index>val:
            return i
    return len(array)

citations=[100,100,100]
print(">>>",solution(citations))

citations=[10,8,5,4,3]
print(">>>",solution(citations))

citations=[25,8,5,3,3]
print(">>>",solution(citations))

citations=[2]
print(">>>",solution(citations))

citations=[0]
print(">>>",solution(citations))
