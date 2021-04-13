T = int(input())
for tc in range(1,T+1):
    #규칙에따라 로봇을 최소 이동횟수로 통과
    #상하좌우로 1칸씩만 가능
    N = int(input())
    # 경기장 정보
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    #RGB존 1개씩
    #가장 가까운 존으로 이동
    # 같은 경우 R-G-B순으로 이동
    # 이동할 수 없는 zone 무시
    # 스테이지마다 최소 1개는 방문
    # 2가 시작점 R:3, G:4, B:5
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                stx = i
                sty = j
                arr[i][j] = 1
                break
    #시작점 찾기
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    stack = [[stx,sty]]
    # DFS로 탐색하다가 해당 R G B가 발견되면 종료후
    # 해당시점부터 다시 시작
    while stack:
        x,y = stack.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]