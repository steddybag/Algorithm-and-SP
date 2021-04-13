import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    # 회전시 특징 세로에서 위로 읽으면 된다.
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr_90 = [[0]*N for _ in range(N)]
    arr_180 = [[0]*N for _ in range(N)]
    arr_270 = [[0]*N for _ in range(N)]
    #90
    for col in range(N):
        for row in range(N-1,-1,-1):
            arr_90[col][N-1-row] = arr[row][col]
    #180
    for col in range(N):
        for row in range(N-1,-1,-1):
            arr_180[col][N-1-row] = arr_90[row][col]
    #270
    for col in range(N):
        for row in range(N-1,-1,-1):
            arr_270[col][N-1-row] = arr_180[row][col]
    print('#{}'.format(test_case))
    for i in range(N):
        a1 = ''
        a2 = ''
        a3 = ''
        for t1 in arr_90[i]:
            a1 += str(t1)
        for t1 in arr_180[i]:
            a2 += str(t1)
        for t1 in arr_270[i]:
            a3 += str(t1)
        print('{} {} {}'.format(a1,a2,a3))