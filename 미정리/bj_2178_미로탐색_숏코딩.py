import sys
sys.stdin = open('input.txt','r')
n, m = map(int,input().split())
queue = []
dx = [0,-1,1,0]
dy = [1,0,0,-1]
s = [list(input()) for _ in range(n)]
queue = [[0,0]]
#어렵게 생각하지 말고 직관적으로 생각할 것
s[0][0] = 1
while queue:
    a, b = queue[0][0],queue[0][1]
    queue.pop(0)
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if n>x>=0 and m>y>=0 and s[x][y] == '1':
            queue.append([x,y])
            s[x][y] = s[a][b] + 1
#작은 단위에서 늘어난다는 식으로 생각
print(s[n-1][m-1])