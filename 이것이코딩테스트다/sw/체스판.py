T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    check_row_arr,check_col_arr={},{}
    flag=True
    for i in range(8):
        line=input()
        for j in range(8):
            word=line[j]
            if word=='O':
                if i not in check_row_arr and j not in check_col_arr:
                    check_row_arr[i]=j
                    check_col_arr[j]=i
                else:
                    flag=False
                    break
        if not flag:
            continue
    print(f"#{test_case} yes") if flag and len(check_row_arr)==8 else print(f"#{test_case} no")

    