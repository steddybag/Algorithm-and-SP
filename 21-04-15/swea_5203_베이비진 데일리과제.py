import sys
sys.stdin = open('input.txt','r')

def chk_run_tri(A):
    # 3개이상이었다고 가정
    for i in range(10):
        if A[i] >=3 :
            return True
        #tri 체크
        elif i <8:
            if A[i] >0 and A[i+1] >0 and A[i+2] >0:
                #triple이면
                return True
        #run 체크
    return False

T = int(input())
for test_case in range(1,T+1):
    arr = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    victory = 0
    #가진 게 없다고 가정
    for i in range(len(arr)):
        if i%2 == 0:
            p1[arr[i]]+=1
        else:
            p2[arr[i]]+=1

        if i > 5 : #3개이상부터 필요
            if chk_run_tri(p1):
                victory = 1
                break
            elif chk_run_tri(p2):
                victory = 2
                break
    print('#{} {}'.format(test_case,victory))