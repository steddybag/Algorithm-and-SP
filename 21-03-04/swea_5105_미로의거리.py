import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    # N*N 미로/ 출발지 2 도착지 3
    #최소수 / 없으면 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                break
        if arr[i][j] == '2':
            break
    queue = [(i,j)]
    arr[i][j] = 0
    res = 0
    chk = 0
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == '0':
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))
                elif arr[nx][ny] == '3':
                    chk = 1
                    break
        if chk == 1: # index가 arr[3][-1]로 오류가 발생할 수 있으므로
            res = arr[x][y]
            break
    print('#{} {}'.format(test_case,res))