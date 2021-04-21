import sys
sys.stdin = open('input.txt','r')

def DFS(cur,cnt):
    global res
    if cnt > res:
        res = cnt
    visited[cur] = 1
    for j in range(1,N+1):
        if adj_list[cur][j] == 1:
            if visited[j] == 0:
                DFS(j,cnt+1)
                visited[j] = 0 #다시 원상태로 복구

T = int(input())
for tc in range(1,T+1):
    # 15! > 1000 이므로 전체 경우의 수를 뽑고는 X
    N, M = map(int,input().split())

    adj_list = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int,input().split())
        adj_list[x][y] = 1
        adj_list[y][x] = 1
    res = 0
    for i in range(1,N+1):
        visited = [0] * (N+1)
        DFS(i,1) #초기값 무조건 1개이상 이므로

    print('#{} {}'.format(tc,res))