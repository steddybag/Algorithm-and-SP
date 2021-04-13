import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 부분행렬의 열의개수와 /행의 개수도 서로 다르다
    mat = {}
    for row in range(n):
        col_cnt = 0
        for col in range(n):
            if arr[row][col] != 0:
                col_cnt +=1
            elif col_cnt != 0 and arr[row][col] == 0:
                #0이 아니면 행렬의 행을 구했으므로,
                mat[col_cnt] = mat.get(col_cnt,0)+1
                #cnt값이 없으면 0 있으면 +1을 수행
                col_cnt = 0
        if col_cnt > 0:
            #벽을 만나 끝난 경우도 위와 같이 실행
            mat[col_cnt] = mat.get(col_cnt, 0) + 1
    res = []
    for x,y in mat.items():
        #크기가 작은 순서대로 출력 / 같을 경우 행이 작은 순으로 출력
        res.append([x*y,y,x])
    res.sort()
    print('#{} {}'.format(test_case,len(res)),end='')
    for i in res:
        print(' {} {}'.format(i[1],i[2]),end='')
    print()


