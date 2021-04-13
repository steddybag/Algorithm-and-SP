import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    #도착가능 1, 아니면 0
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    nx = -1
    delta = [(-1,0),(1,0),(0,-1),(0,1)]
    #시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                nx = i
                ny = j
                break
    #상하좌우 경로탐색
    road = [(nx,ny)]
    res = 0
    while road:
        # 2개 이상 경로가 존재할 경우 stack에 교차점 추가
        nx, ny = road.pop()
        arr[nx][ny] = 1
        for i in delta:
            dx = nx + i[0]
            dy = ny + i[1]
            if dx >=0 and dx < N and dy>=0 and dy<N:
                #경로안에 있다면
                if arr[dx][dy]=='0':
                    road.append((dx,dy))
                elif arr[dx][dy] == '3':
                    res = 1
                    break
        if res == 1:
            break
    print('#{} {}'.format(test_case,res))