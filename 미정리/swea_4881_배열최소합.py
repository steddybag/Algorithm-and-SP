import sys
sys.stdin = open('input.txt','r')
# 1개에서 2개로 늘어날때 크면 버린다.
def find_min(row):
    global res, min_val
    if res > min_val:
    # 2번째까지 합이 계산된 min값보다 크다면 계산을 안해봐도 된다.
        return
    if row == N: #끝까지 다 계산하였을 때
        if res < min_val:
            min_val = res
            return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            res += arr[row][i]
            find_min(row+1)
            #계산 후 아니라면 다시 원래대로 Tree형태와 유사
            #3-2-1 계산후 3-2-2도 계산해보기 위함
            #3-2-1에서 아닌게 밝혀지면 3-2-1-4-5 3-2-1-5-4 를 해볼 필요가 없다.
            res -= arr[row][i]
            visit[i] = 0

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 첫 줄 검사 후, 가장 작은 값 찾기
    visit = [0]*N
    # (1~N) 고정(1~N) 순열
    res, min_val = 0,9999
    find_min(0)
    print('#{} {}'.format(test_case,min_val))
