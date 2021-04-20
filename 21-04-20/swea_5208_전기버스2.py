import sys
sys.stdin = open('input.txt','r')

def charge(start,cap,cnt):
    global res
    if start + cap >= N:
        res = min(res,cnt)
        return
    elif res <= cnt:
        return
    else :
        for i in range(1,cap+1):
            charge(start+i,arr[start+i],cnt+1)

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    N = arr[0]
    res = 9999
    charge(1,arr[1],0)
    print('#{} {}'.format(tc,res))
