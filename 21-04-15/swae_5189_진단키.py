import sys
sys.stdin = open('input.txt','r')

def p(N):
    picked = []

    def recur():
        if len(picked) == N-1:
            global res
            res.append(picked[:])
            return

        for i in range(1,N):
            if i not in picked:
                picked.append(i)

                recur() #순열
                picked.pop()
                #다시 초기화
    recur()

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 첫과 끝은 0 고정 1,2 or 2,1 순열문제
    #1,2,3 - 1,3,2 - 2,1,3 - 2,3,1 - 3,1,2 - 3,2,1
    res = []
    p(N) #경우의 수 출력
    # print(res)
    fin = 9999
    for route in res:
        sum = 0
        for j in range(N-1):
            if j == 0:
                sum += arr[0][route[j]]
            if j == N-2:
                sum+=arr[route[j]][0]
            else:
                sum+=arr[route[j]][route[j+1]]
        fin = min(fin,sum)
    print('#{} {}'.format(tc,fin))