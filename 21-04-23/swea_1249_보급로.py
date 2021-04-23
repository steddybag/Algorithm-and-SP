import sys
sys.stdin = open("input.txt", "r")

def BFS():
    q = [(0,0)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:

                if dis[nx][ny] > dis[x][y] + arr[nx][ny]:
                    dis[nx][ny] = dis[x][y] + arr[nx][ny]
                    q.append((nx,ny))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 합이 최소
    arr = []
    for i in range(N):
        tmp = input()
        tmp2 = []
        for j in tmp:
            tmp2.append(int(j))
        arr.append(tmp2)
    dis = [[9999]*N for _ in range(N)]
    dis[0][0] = 0
    BFS()

    print('#{} {}'.format(test_case, dis[N-1][N-1]))