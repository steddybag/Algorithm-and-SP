import sys
sys.stdin = open('input.txt','r')

def preorder(n):
    if child[n][0] != 0:
        preorder(child[n][0])
        if child[n][1] !=0:
            preorder(child[n][1])
    cnt[0]+=1


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    child = [[0,0] for i in range(E+2)]
    for i in range(E):
        tmp = child[arr[2*i]]
        if tmp[0] == 0:
            tmp[0] = arr[2*i+1]
        else:
            tmp[1] = arr[2*i+1]
    cnt = [0]
    preorder(N)
    print('#{} {}'.format(test_case,cnt[0]))