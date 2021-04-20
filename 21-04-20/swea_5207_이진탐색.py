import sys
sys.stdin = open('input.txt','r')
def binsearch(a,low,high,flag):
    mid = (low+high)//2
    # print(A[mid],a,flag)
    if A[mid] > a:
        if flag == 0:
            return False
        return binsearch(a,low,mid-1,0) # 좌측이므로 flag = 0
    elif A[mid] < a:
        if flag == 1:
            return False
        return binsearch(a,mid+1,high,1)
    else:
        return True

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in B:
        if binsearch(i,0,N-1,2): # flag =2 처음실행의경우 상관없으므로
            cnt +=1

    print('#{} {}'.format(tc,cnt))