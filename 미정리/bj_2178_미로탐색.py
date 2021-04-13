import sys
sys.stdin = open('input.txt','r')

def BFS(chk):
    x,y = chk[-1]
    if x == N-1 and y == M-1:
        return len(chk)
    st = []
    dt = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(4):
        nx = x+dt[i][0]
        ny = y+dt[i][1]
        if N > nx >=0 and M > ny >= 0:
            if arr[nx][ny] == '1':
                if not ((nx,ny) in chk):
                    tmp = chk[:]
                    tmp.append((nx,ny))
                    st.append(BFS(tmp))
    if st :
        return min(st)
    else:
        return 9999

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N) ]

print(BFS([(0,0)]))