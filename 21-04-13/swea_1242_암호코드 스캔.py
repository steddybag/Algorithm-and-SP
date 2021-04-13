import sys
sys.stdin = open("input.txt", "r")

T = int(input())
code = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}

def reduce(c,b,a):
    min_num = min(c,b,a)
    # a는 첫째 1
    # b는 중간 0
    # c는 전환 후 1
    c //= min_num
    b //= min_num
    a //= min_num
    return str(c)+str(b)+str(a)

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    # 16진수 -> 2진수 16진수 4*14 = 56 14개 28개 42개 ... 필요
    ans = 0
    result = []
    visited = []

    bin_arr = ['']*N
    for i in range(N):
        for j in range(M): #2진수 10진수 변환보다 dict 형태가 빠르다.
            bin_arr[i] += bin(int('0x'+arr[i][j],16))[2:].zfill(4)

    for t in range(N):
        a=b=c=0
        for x in range(4*M-1,-1,-1): #역순
            if c == 0 and b == 0 and bin_arr[t][x] == '1':
                a+=1
            elif a>0 and c==0 and bin_arr[t][x]=='0':
                b+=1
            elif a*b>0 and bin_arr[t][x]=='1':
                c+=1

            if a*b*c>0 and bin_arr[t][x] == '0':
                result.append(code[reduce(c,b,a)])
                a=b=c=0

            if len(result) == 8:
                result = result[::-1]#역순 정렬 append하였으므로
                val = (result[0] + result[2] + result[4] + result[6])*3 + (result[1]+result[3]+result[5]) + result[7]

                if val%10==0 and result not in visited:
                    ans += sum(result)

                visited.append(result)
                result=[] #초기화

    print('#{} {}'.format(test_case,ans))