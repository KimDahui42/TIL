def solution(n):
    current = 1
    ans = 1
    while True:
        if current == n:
            return ans
        elif current * 2 < n:
            continue
        elif current * 2 == n:
            return ans
        else:
            current += 1
            ans += 1
        print(current)
    return ans

