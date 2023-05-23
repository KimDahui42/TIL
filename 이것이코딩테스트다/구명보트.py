from collections import deque


def solution(people, limit):
    answer, front, end = 0, 0, len(people) - 1
    people.sort()
    q = deque(people)
    current = q.pop()
    while q:
        tmp = q.popleft()
        if current + tmp <= limit:
            current += tmp
            if not q:
                answer += 1
        else:
            q.appendleft(tmp)
            answer += 1
            current = q.pop()
            if not q:
                answer += 1

    return answer if answer != 0 else 1