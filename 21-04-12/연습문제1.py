arr = input()
#이어있는 데이터 이므로
#앞에서부터 10진수화
#0b 붙이기
N = len(arr)
sum = 0
n = N//7
if N%7 == 0:
    for i in range(N//7):
        print(int('0b'+arr[7*i:7*(i+1)],2),end=' ')
else:
    for i in range(N//7):
        print(int('0b'+arr[7*i:7*(i+1)],2),end=' ')
    print(int('0b'+arr[7*n:].zfill(7),2))
    #마지막 남은 개수 7개가 아니면 0 채우기
print()