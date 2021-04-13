import sys
sys.stdin = open('input.txt','r')

def inorder(n):
    if n < len(tree):
        inorder(2*n)
        tree[n]=cnt[0]
        cnt[0]+=1
        inorder(2*n+1)
T = int(input())
for test_case in range(1, T + 1):
    #L<V<R
    N = int(input())
    #계속해서 inorder로 점검
    tree=[0]*(N+1)
    cnt = [1]
    inorder(1)
    print('#{} {} {}'.format(test_case,tree[1],tree[N//2]))