tmp = input()
#이어있는 데이터 이므로
#앞에서부터 10진수화
#0b 붙이기
#내장함수 이용 bin(Ox+이용)
arr = ''
for i in tmp:
    tt = bin(int('0x'+i,16))
    tt = tt[2:] #0b 제거
    arr += tt.zfill(4)
N = len(arr)
n = N//7
if N%7 == 0:
    for i in range(N//7):
        print(int('0b'+arr[7*i:7*(i+1)],2),end=' ')
    print()
else:
    for i in range(N//7):
        print(int('0b'+arr[7*i:7*(i+1)],2),end=' ')
    print(int('0b'+arr[7*n:].zfill(7),2))
    #마지막 남은 개수 7개가 아니면 0 채우기