import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    #0은 길, #1은 벽 출발점 2, 도착점 3
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    N = input()
    arr = [list(input()) for _ in range(16)]
    # 출발점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                break
        if arr[i][j] == '2':
            break

    queue = [(i,j)]
    res = 0
    while queue : #BFS사용
        x, y = queue.pop(0)
        #print(queue)
        for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           #모퉁이가 아니라면
           if 0<=nx<16 and 0<=ny<16:
               if arr[nx][ny] == '0':
                   arr[nx][ny] = '1'
                   queue.append((nx,ny))
               elif arr[nx][ny] == '3':
                   res = 1
                   break
        if res == 1:
            break
    print('#{} {}'.format(test_case,res))
