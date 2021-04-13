import sys
sys.stdin = open('input.txt','r')

T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def inorder(n):
    tmp = child[n]
    if len(tmp) == 3:
        inorder(tmp[1])
        print(tmp[0],end='')
        inorder(tmp[2])
    elif len(tmp) == 2:
        inorder(tmp[1])
        print(tmp[0], end='')
    else:
        print(tmp[0], end='')
for test_case in range(1, T + 1):
    N = int(input())
    child=[[] for i in range(N+1)]
    for i in range(1,N+1):
        arr = list(input().split())
        arr.pop(0)
        child[i].append(arr[0])
        arr.pop(0)
        while arr:
            child[i].append(int(arr.pop(0)))

    print('#{} '.format(test_case),end='')
    inorder(1)
    print()