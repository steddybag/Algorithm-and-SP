import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    #L<V<R
    N = int(input())
    arr = list(map(int,input().split()))
    #계속해서 inorder로 점검
    tree=[0]
    for i in range(N):
        chk = []
        tree.append(arr[i])
        n = i+1
        while n//2 :
            if tree[n//2] > tree[n]:
                tmp = tree[n]
                tree[n]=tree[n//2]
                n = n//2
                tree[n] = tmp
            else:
                break
    res=0
    while 1:
        N = N // 2
        res+=tree[N]
        if N==1:
            break
    print('#{} {}'.format(test_case,res))