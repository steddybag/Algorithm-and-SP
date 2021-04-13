import sys
sys.stdin = open('input.txt','r')

def inorder(n):
    if n < len(tree):
        inorder(2*n)
        if chk:
            if chk[-1][1] > tree[n]:
                tmp = tree[n]
                nn = chk[-1][0]
                tree[n] = tree[nn]
                tree[nn] = tmp
            chk.append([n, tree[n]])
        else:
            chk.append([n,tree[n]])
        inorder(2*n+1)
T = int(input())
for test_case in range(1, T + 1):
    #L<V<R
    N = int(input())
    #계속해서 inorder로 점검
    tree=[0]
    for i in range(1,N+1):
        chk = []
        tree.append(i)
        inorder(1)
    print('#{} {} {}'.format(test_case,tree[1],tree[N//2]))