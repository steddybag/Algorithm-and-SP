import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    #V 노드의 개수, E간선정보, 양방향
    V, E = map(int,input().split())
    arr = [ [] for _ in range(V+1) ]
    visited = [ 0 for _ in range(V+1)]
    #2차원 배열을 쓰는것보다 데이터양에 효과적
    for _ in range(E):
        x,y = map(int,input().split())
        arr[x].append(y)
        arr[y].append(x)
    #print(arr)
    S,G = map(int,input().split())
    #BFS 탐색
    queue = [S]
    res = 0
    while queue:
        tmp = queue.pop(0)
        for i in arr[tmp]:
            if i == G:
                break
            elif visited[i] == 0:
                visited[i] = visited[tmp] + 1
                queue.append(i)
        if i == G:
            res = visited[tmp] + 1
            break
    print('#{} {}'.format(test_case,res))