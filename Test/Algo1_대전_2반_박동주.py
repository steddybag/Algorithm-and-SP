T = int(input())
for tc in range(1,T+1):
    #N 지도크기 , M 폭탄수
    N, M = map(int,input().split())
    # 폭발력에 따라 대각선 길이 증가
    # 폭발력은 1 ~ 5 사이
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    # 적군 배치 입력

    # 방향 왼쪽 위,왼쪽 아래, 오른쪽 아래
    dx=[-1,-1,1,1 ]
    dy=[-1,1,1,-1 ]

    visited = [[0]*N for _ in range(N)]
    for i in range(M):
        x,y, p = map(int,input().split())
        visited[x][y] = 1
        for t in range(4):
            for idx in range(1,p+1):
                nx = x+dx[t]*idx
                ny = y+dy[t]*idx
                # 한방향으로 쭉 가다가 끝을 만나면 break
                if N>nx>=0 and N>ny>=0:
                    visited[nx][ny] = 1
                else:
                    break
    # 필터 같이 해당 visited가 방문 했으면 1이므로
    # 각각의 원소와 배치도를 곱해서 피해를 입은 적군의 총 수 계산
    sum = 0
    for i in range(N):
        for j in range(N):
            sum+= arr[i][j]*visited[i][j]

    print('#{} {}'.format(tc,sum))

