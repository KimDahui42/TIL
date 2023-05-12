T = int(input())
for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    arr=''
    code={
        "0001101":'0',"0011001":'1',"0010011":'2',"0111101":'3',"0100011":'4',
        "0110001":'5',"0101111":'6',"0111011":'7',"0110111":'8',"0001011":'9'
    }
    for _ in range(n):
        line=input()
        if arr!='':
            continue
        line=line.lstrip('0')
        if line=='':
            continue
        else:
            arr=line
            
    splited,answer=[],''
    if test_case==7:
        print(arr)
    if arr[0:4] in ("1101","1011"):
        tmp=''
        if arr[0:6] in ("110111","101111"):
            tmp="0"+arr
        else:
            tmp="000"+arr
        splited=[tmp[i:i+7] for i in range(0,56,7)]
    elif arr[0:5] in ("11001","10011"):
        tmp="00"+arr
        splited=[tmp[i:i+7] for i in range(0,56,7)]
    elif arr[0:6] in ("111101","100011","110001","111011"):
        tmp="0"+arr
        splited=[tmp[i:i+7] for i in range(0,56,7)]
    
    odd,even,total=0,0,0
    
    for i in splited:
        answer+=code[i]

    for i in range(8):
        num=int(answer[i])
        total+=num
        if i%2==0:
            odd+=num
        else:
            even+=num
    print(f"#{test_case} 0") if (odd*3+even)%10!=0 else print(f"#{test_case} {total}")
