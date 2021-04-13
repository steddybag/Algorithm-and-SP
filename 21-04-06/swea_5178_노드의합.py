import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    N,M,L = map(int,input().split())
    #postorder L->R->V
    tree = [0]*(N+1)
    for i in range(M):
        idx, val =map(int,input().split())
        tree[idx]=val
    arr = list(range(2,N+1))
    while arr:
        l = arr.pop()
        if l%2==0:
            tree[l//2]=tree[l]
        else:
            r=arr.pop()
            tree[r//2]=tree[l]+tree[r]
    print('#{} {}'.format(test_case,tree[L]))