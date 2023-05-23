def solution(n):
    tmp, i = bin(n), 1
    cnt = tmp.count('1')
    while True:
        if cnt == bin(n + i).count('1'):
            break
        i += 1
    return n + i