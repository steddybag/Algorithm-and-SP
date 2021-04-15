import sys
sys.stdin = open("input.txt", "r")

def DFS(A,n,num,cnt):
    global chk_max
    if A == tmp:
        #중복이 있으면
        if list(set(A)) == A:
            if (cnt-num)%2==1:
                #어차피 일의자리랑 10의자리 왔다갔다하는거
                A[-1],A[-2] = A[-2],A[-1]
        chk_max = int("".join(A))
        return

    elif num == cnt:
        # global chk_max
        chk_max = max(int("".join(A)),chk_max)
        return
    else:
        if n < len(A):
            DFS(A,n+1,num,cnt) # 안바꿔도 되는 경우
            #다음 걸로 넘어간다.
        for i in range(n,len(A)):
            A[i], A[n] = A[n], A[i]
            DFS(A,n+1,num+1,cnt)
            A[i], A[n] = A[n], A[i]
            #다시 원상태로

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    #selectionSort큰순으로
    # 횟수만큼 교환 이루어지고 동일한 위치 교환 중복 가능
    M = int(M)
    arr = []
    chk_max = 0
    cnt = M
    for i in N:
        arr.append(i)
    # 데이터 형 변환
    tmp = sorted(arr,reverse=True)
    DFS(arr,0,0,cnt)
    print('#{} {}'.format(tc,chk_max))

