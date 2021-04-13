import sys
sys.stdin = open('input.txt','r')

def inorder(n):
    if n<=N :
        tmp = tree[n]
        if tmp[0]=='-':
            a = inorder(tmp[1])
            b = inorder(tmp[2])
            return a-b
        elif tmp[0]=='+':
            a = inorder(tmp[1])
            b = inorder(tmp[2])
            return a+b
        elif tmp[0]=='/':
            a = inorder(tmp[1])
            b = inorder(tmp[2])
            return int(a/b)
        elif tmp[0]=='*':
            a = inorder(tmp[1])
            b = inorder(tmp[2])
            return a*b
        else:
            return int(tmp[0])

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree =[ [] for i in range(N+2) ]
    #이진트리가 아니다...
    for i in range(1,N+1):
        arr = input().split()
        arr.pop(0)
        tree[i].append(arr.pop(0))
        while arr:
            tree[i].append(int(arr.pop(0)))
    result = inorder(1)
    print('#{} {}'.format(test_case,result))