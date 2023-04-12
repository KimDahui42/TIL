def solution(prices):
    answer=[0]*len(prices)
    stack=[]
    for i,v in enumerate(prices):
        # 스택이 비었거나 마지막 보다 다음 요소가 더 클 때
        if i==len(prices)-1:
            while len(stack)>0:
                _,pop_i=stack.pop()
                answer[pop_i]=i-pop_i
        elif len(stack)==0 or stack[-1][0]<=v:
            stack.append((v,i))
        else:
            while len(stack)>0 and stack[-1][0]>v:
                _,pop_i=stack.pop()
                answer[pop_i]=i-pop_i
            stack.append((v,i))
    return answer

if __name__=='__main__':
    prices=[1, 2, 3, 2, 3]
    # return = [4, 3, 1, 1, 0]
    print(solution(prices))