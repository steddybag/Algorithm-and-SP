import sys
sys.stdin = open('input.txt','r')
global visited
T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    origin_arr = [list(map(int,input().split())) for _ in range(N) ]
    # 등산로 가장 높은 봉우리 / 자기보다 낮은 지형 상하좌우만 가능
    # K만큼 깎는 것만 가능
    # 처음에 가장 높은 등산로만 찾자
    arr = origin_arr[:]
    global visited
    visited = [[False] * N for _ in range(N)]
    starts = []
    st_value = 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > st_value :
                st_value = arr[i][j]
                starts = [ (i,j) ]
            elif arr[i][j] == st_value:
                starts.append((i,j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    def DFS(x, y, cnt, cut):
        global ans
        global visited
        print(visited)
        ans = max(ans,cnt)
        #print(ans,cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 먼저 값을 벗어난 경우 continue로 패스
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue

            # 이미 방문했으면 True
            if visited[nx][ny]: continue

            # 깎아야 될 지형이라면
            if arr[nx][ny] >= arr[x][y]:
                if cut == 0:  # 한번도 깎지 않았다면
                    for j in range(K):
                        tmp = arr[nx][ny]
                        cut_tmp = arr[nx][ny] - j

                        if arr[x][y] > cut_tmp:
                            visited[nx][ny] = True
                            arr[nx][ny] = cut_tmp
                            DFS(nx, ny, cnt + 1, cut + 1)
                            # 원상복구
                            arr[nx][ny] = tmp
                            visited[nx][ny] = False
            # 현재지형보다 낮은 지형일 경우 프리패스
            else:
                visited[nx][ny] = True
                DFS(nx,ny,cnt+1,cut)
                visited[nx][ny] = False
    for i in starts:
        x = i[0]
        y = i[1]
        visited[x][y] = True
        DFS(x,y,1,0)
        visited[x][y] = False
    print(visited)
    print(ans)
    print(arr)