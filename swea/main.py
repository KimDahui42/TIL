T = int(input())
for test_case in range(1, T + 1):
    answer=0
    n,d=map(int,input().split())
    arr=[tuple(map(int,input().split())) for _ in range(n)]
    print(f"#{test_case} {answer}")
