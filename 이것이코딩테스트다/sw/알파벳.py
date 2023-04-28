T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt=0
    line=input()
    for i in range(len(line)):
        if i==0 and line[0]=='a':
            cnt=1
        elif i==0 and line[0]!='a':
            break
        elif ord(line[i])-ord(line[i-1])!=1:
            break
        else:
            cnt+=1
    print(f"#{test_case} {cnt}")