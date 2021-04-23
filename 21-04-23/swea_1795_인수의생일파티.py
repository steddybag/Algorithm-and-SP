import sys
sys.stdin = open("input.txt", "r")

#가는건 BFS
def BFS(st):
    q = [st]
    while q:
        cur = q.pop(0)
        for i in range(N):
            if dis[cur][i] != 0 and V[i] > V[cur] + dis[cur][i]:
                V[i] = V[cur] + dis[cur][i]
                dis[st][i] = V[i]
                q.append(i)

def BFS1(end):
    q = [end]
    while q:
        cur = q.pop(0)
        for i in range(N):
            if dis[i][cur] != 0 and T[i] > T[cur] + dis[i][cur]:
                T[i] = T[cur] + dis[i][cur]
                dis[i][end] = T[i]
                q.append(i)

T = int(input())
for test_case in range(1, T + 1):
    N,M,X = map(int,input().split())
    # M 관계수, 사람 1부터 시작
    dis = [[0]*(N) for _ in range(N)]

    for i in range(M):
        x,y,c = map(int,input().split())
        dis[x-1][y-1] = c

    V = [9999999]*N
    T = [9999999] * N
    V[X-1] = 0
    T[X-1] = 0
    BFS(X-1)
    BFS1(X-1)
    res = [V[i]+T[i] for i in range(N)]

    print('#{} {}'.format(test_case,max(res)))