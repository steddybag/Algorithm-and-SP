import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    dx = [-1, 1, 0, 0]
    dy = [0,0,-1,1]
    start = 99999
    for n in range(N):
        for m in range(N):
            #시작점 알아보는 것
            # N^2이하 숫자가 모드 다르다
            # 시작점 선별가능 ex) max_cnt가 남은 수 이상이면 할 필요 X
            if N*N - arr[n][m] <= res :
                pass
            chk = 1
            cnt = 1
            x,y = n,m
            while chk:
                chk = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if N > nx > -1 and N > ny > -1:
                        if arr[nx][ny] == arr[x][y] + 1:
                            x = nx
                            y = ny
                            chk = 1
                            cnt += 1
                            break
            if res < cnt :
                res = cnt
                start = arr[n][m]
            elif res == cnt:
                start = min(start,arr[n][m])

    print('#{} {} {}'.format(test_case,start,res))