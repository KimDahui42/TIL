import sys
def solution(begin, target, words):
    answer = 0
    max_val=sys.maxsize
    min_val=max_val

    if target not in words:
        return answer

    def changable(a,b):
        cnt=0
        if len(a)!=len(b):
            return False
        for i,alphabet in enumerate(a):
            if alphabet!=b[i]:
                cnt+=1
        if cnt==1:
            return True
        return False    

    def bfs(begin):
        current=begin
        cnt=1
        for word in words:
            if current==target:
                return cnt
            if changable(current,target):
                return cnt+1
            if changable(current,word):
                print(word)
                current=word
                cnt+=1
        return max_val
    
    for i in words:
        if changable(begin,i):
            print(i)
            val=bfs(i)
            if min_val>val:
                min_val=val
    
    answer=min_val
            
    return answer


begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))