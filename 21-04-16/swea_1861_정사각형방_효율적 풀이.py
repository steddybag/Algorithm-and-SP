import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    dx = [-1, 1, 0, 0]
    dy = [0,0,-1,1]
    v = [0] * (N*N + 1)
    for n in range(N):
        for m in range(N):
            for i in range(4):
                nx = n + dx[i]
                ny = m + dy[i]
                if N > nx > -1 and N > ny > -1:
                    if arr[nx][ny] == arr[n][m] + 1:
                        v[arr[n][m]] = 1
                        break
    cnt = 0
    start = N*N
    for i in range(N*N+1):
        if v[i] == 1:
            cnt +=1
        elif v[i] == 0:
            if res < cnt + 1:
                start = i - cnt
                res = cnt + 1
            elif res == (cnt + 1):
                start = min(start,i-cnt)
            cnt = 0

    print('#{} {} {}'.format(test_case,start,res))