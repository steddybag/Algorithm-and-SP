import sys
sys.stdin = open('input.txt','r')

def prob(cost,idx,chk_list):
    if idx == N-1:
        cost *= arr[idx][chk_list[0]]/100
        global res
        res = max(cost,res)
    elif res > cost:
        return
    else:
        for i in chk_list:
            if arr[idx][i] != 0:
                tmp = chk_list[:]
                tmp.remove(i)
                prob(cost*arr[idx][i]/100,idx+1,tmp)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    res = 0
    prob(1,0,A)
    res *= 100
    print('#{} {:.6f}'.format(tc,res))
