import sys
sys.stdin = open('input.txt','r')

def chk(A,B):
    if len(A) == 1 and len(B) == 1:
        if A[0][0] == B[0][0]:
            return [A[0]]
        elif A[0][0] == 3 or B[0][0] == 3:
            if A[0][0] == 1:
                return [A[0]]
            elif B[0][0] == 1:
                return [B[0]]
            else:
                return [max(A[0],B[0])]
        else:
            return [max(A[0],B[0])]
    else:
        #i=0, j=len(A)
        if len(A) == 1:
            A.append(A[0])
        elif len(B) == 1:
            B.append(B[0])

        if len(A) % 2 == 0:
            a = len(A) // 2
        else:
            a = len(A) // 2 +1
        if len(B) % 2 == 0:
            b = len(B) // 2
        else:
            b = len(B) // 2 +1
        return chk(chk(A[:a],A[a:]),chk(B[:b],B[b:]))
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    #같은 카드 일 경우, 번호가 작을 수록 승자
    t = []
    for i in range(1,N+1):
        t.append((arr[i-1],i))
    if N%2==0:
        n = N//2
    else:
        n = N//2 +1
    res = chk(t[:n],t[n:])
    print('#{} {}'.format(test_case,res[0][1]))
