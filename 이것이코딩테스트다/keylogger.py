from collections import deque
t=int(input())
for _ in range(t):
    line=input()
    front_q=deque()
    back_q=deque()
    for ch in line:
        if ch=='<':
            if len(front_q)!=0:
                back_q.extendleft(front_q.pop())
        elif ch=='>':
            if len(back_q)!=0:
                front_q.extend(back_q.popleft())
        elif ch=='-':
            if len(front_q)!=0:
                front_q.pop()
        else:
            front_q.extend(ch)
    print(''.join(front_q)+''.join(back_q))
        