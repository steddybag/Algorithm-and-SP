import sys
sys.stdin = open('input.txt','r')

def dfs(i,s):
    if s+sum(arr[i:]) < B:
        return
    elif s>=B:
        global gap
        gap = min(gap,s-B)
    else:
        dfs(i+1,s+arr[i])
        dfs(i+1,s)

T = int(input())
for test_case in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    gap = B
    dfs(0,0)
    print('#{} {}'.format(test_case,gap))