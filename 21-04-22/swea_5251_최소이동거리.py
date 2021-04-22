import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int,input().split())
    # N 마지막 연결지점 E는 도로 개수
    dis = [[0]*(N+1) for _ in range(N+1)]
    adj_list = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for i in range(E):
        x,y,w = map(int,input().split())
        dis[x][y] = w
        dis[y][x] = w
        adj_list[x].append(y)
        adj_list[y].append(x)
    V = [99999]*(N+1)
    q = [(0,0)]
    V[0] = 0
    i = 0
    while q:
        cur,cur_d = q.pop(0)
        if visited[i]:
            continue
        visited[cur] = 1
        for i in adj_list[cur]:
            # 크루스칼 알고리즘
            if V[i] > dis[cur][i]+cur_d:
                V[i] = dis[cur][i]+cur_d
                q.append((i,V[i]))

    print('#{} {}'.format(test_case,V[N]))

