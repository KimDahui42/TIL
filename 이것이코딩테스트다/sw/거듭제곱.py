T = 10
for test_case in range(1, T + 1):
    input()
    n,m=map(int,input().split())
    def pow(x,y):
        if y==1:
            return x
        if y==0:
            return 1
        else:
            return x*pow(x,y-1)
    answer=pow(n,m)
    print(f"#{test_case} {answer}")
