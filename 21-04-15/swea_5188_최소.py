import sys
sys.stdin = open('input.txt','r')

def DFS(x,y,d):
    #조건 잘 읽자 ㅜㅠ 오른쪽이나 아래만 이동가능
    dx = [1, 0]
    dy = [0, 1]
    if x == N-1 and y == N-1:
        global res
        res = min(d,res)
    else:
        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]
            if N>nx and N>ny and [nx,ny]:
                d += arr[nx][ny]
                if d < res:
                    DFS(nx,ny,d)
                d -= arr[nx][ny]
    #if문을 넣는게 함수 호출보다 제한시간적인 측면에서 유리하다...

T=int(input())
for tc in range(1,T+1):
    # 시작 0,0 끝 n,n
    # dfs 알고리즘 사용
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 9999
    DFS(0,0,arr[0][0])

    print('#{} {}'.format(tc,res))