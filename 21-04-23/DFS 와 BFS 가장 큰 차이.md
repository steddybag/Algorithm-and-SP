# DFS 와 BFS 가장 큰 차이

## 여러가지 값들을 update 구해야 될 게 여러개라면 BFS

* 한 점으로 부터 다른 점까지의 거리들을 전부 다 계산해야된다면 

* BFS로 update 시켜 나가는게 제일 빠르다

  

##  DFS의 경우 대부분 시간 초과가 발생합니다.

* 만약 DFS의 시간초과가 발생한 경우
* BFS로 바꾸어 함수를 적어봅시다.

swea_1795 인수의 생일파티

```python
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
```



위의 문제의 경우에도 처음 DFS를 할 경우 시간초과가 발생합니다.

BFS로 각각의 점들을 update해 나가는 방식으로 문제를 해결 할 수 있습니다.