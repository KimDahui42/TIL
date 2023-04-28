T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    flag=True
    n,m=map(int,input().split())
    arr=[input() for _ in range(n)]
    for i in range(n):
        if not flag:
            break
        for j in range(m-1):
            print(i,j)
            if i==n-1:
                if arr[i][j]=='#' and arr[i][j+1]=='#' or arr[i][j]=='.' and arr[i][j+1]=='.':
                    flag=False
                    break
            else:
                if arr[i][j]=='#' and arr[i][j+1]=='#' or arr[i][j]=='#' and arr[i+1][j]=='#':
                    flag=False
                    break
                elif arr[i][j]=='.' and arr[i][j+1]=='.' or arr[i][j]=='.' and arr[i+1][j]=='.':
                    flag=False
                    break

    print(f"#{test_case} possible") if flag else print(f"#{test_case} impossible")