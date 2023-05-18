T = 10
for test_case in range(1, T + 1):
    input()
    target=input()
    line=input()
    l_size=len(line)
    t_size=len(target)
    cnt=0
    for i in range(l_size-t_size+1):
        cnt = cnt+1 if line[i:i+t_size] == target else cnt
    print(f"#{test_case} {cnt}")