from collections import deque

T = 10
for test_case in range(1, T + 1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    idx = -1
    for i in range(100):
        s, n = deque(), deque()
        for j in range(100):
            if arr[j][i] == 2 and len(n) != 0:
                s.append(j)
            elif arr[j][i] == 2:
                n.append(j)
        tmp_s, tmp_n = -1, -1
        while s and n:
            if tmp_s==-1:
                tmp_s=s.pop()
            tmp_n = n.pop()
            if tmp_s>tmp_n:
                cnt+=1
            elif tmp_s<tmp_n:
                tmp_s=-1

