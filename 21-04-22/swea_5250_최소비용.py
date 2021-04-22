import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    dis = [[999999]*N for _ in range(N)]
    dis[0][0] = 0 #시작점
    q = []
    q.append((0,0))
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                gap = 1
                if arr[x][y] < arr[nx][ny]:
                    gap = arr[nx][ny] - arr[x][y] + 1
                # 최소값으로 업데이트
                # 크루스칼 알고리즘
                if dis[nx][ny] > dis[x][y]+gap:
                    dis[nx][ny] = dis[x][y]+gap
                    q.append((nx,ny))
                    #다시 돌아올 교차점에 추가(업데이트를 하였으므로)

    print('#{} {}'.format(test_case,dis[N-1][N-1]))