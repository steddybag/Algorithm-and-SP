import sys
sys.stdin = open("input.txt", "r")

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x] # 다시 전부 설정

def union(x,y):
    c1 = find_set(x)
    c2 = find_set(y)
    if c1>c2:
        p[c1] = c2
    else:
        p[c2] = c1

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    # M 관계수, 사람 1부터 시작
    p = [i for i in range(N+1)]
    rank = [0] *(N+1)
    for i in range(M):
        st, end = map(int,input().split())
        union(st,end)

    for i in range(N+1):
        find_set(i)

    print('#{} {}'.format(test_case,len(set(p))-1))