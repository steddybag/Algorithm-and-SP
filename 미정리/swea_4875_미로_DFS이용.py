import sys
sys.stdin = open('input.txt','r')
def isSafe(ddx, ddy):
    return -1 < ddx < mazesize and -1 < ddy < mazesize and maze[ddx][ddy] != '1'


def bfs(maze):
    for i in range(mazesize):
        for j in range(mazesize):
            if maze[i][j] == '2':
                xs, ys = [i, j]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visit = [[0]*mazesize for _ in range(mazesize)]
    queue = [[xs, ys]]
    visit[xs][ys] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if isSafe(ddx, ddy) and visit[ddx][ddy] == 0:
                queue.append([ddx, ddy])
                visit[ddx][ddy] = 1
                if maze[ddx][ddy] == '3':
                    return 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    global mazesize
    mazesize = int(input())
    maze = []
    for i in range(mazesize):
        maze.append(''.join(input().split()))

    print('#%d %s' % (test_case, bfs(maze)))