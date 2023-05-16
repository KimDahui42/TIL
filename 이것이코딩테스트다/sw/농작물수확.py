T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    arr = [[int(i) for i in input()] for _ in range(n)]
    for i in range(n // 2 + 1):
        answer += sum(arr[i][n // 2 - i: n // 2 + i + 1])
    for i in range(n - 1, n // 2, -1):
        gap = n - i - 1
        answer += sum(arr[i][n // 2 - gap: n // 2 + gap + 1])
    print(f"#{test_case} {answer}")