import sys
sys.stdin = open('input.txt','r')

def produce(cost,idx,chk_list):
    if idx == N-1:
        cost += arr[idx][chk_list[0]]
        global res
        res = min(res,cost)
    elif res <= cost:
        return
    else :
        for j in chk_list:
            tmp = chk_list[:]
            tmp.remove(j)
            produce(cost+arr[idx][j],idx+1,tmp)

T = int(input())
for tc in range(1,T+1):
    # 15! > 1000 이므로 전체 경우의 수를 뽑고는 X
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = [ i for i in range(N)]
    res = 9999
    produce(0,0,A)
    print('#{} {}'.format(tc,res))