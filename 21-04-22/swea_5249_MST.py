import sys
sys.stdin = open("input.txt", "r")

def get_set(x):
    if p[x] != x:
        p[x] = get_set(p[x])
    return p[x]

def chk_cloud(x,y):
    return get_set(x) == get_set(y)

def union(x,y):
    c1 = get_set(x)
    c2 = get_set(y)
    if c1>c2:
        p[c1] = c2
        #작은 걸로 맞춘다.
    else:
        p[c2] = c1

T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    # 크루스칼 알고리즘 이용
    p = [i for i in range(V+1)] #V는 마지막 노드번호 이므로,
    weight = []
    for i in range(E):
        weight.append(list(map(int,input().split())))
    weight.sort(key = lambda x : x[2],reverse=True)
    res = 0
    while weight:
        #짧은 것 부터 선택
        st, en, w = weight.pop()
        if not chk_cloud(st,en):
            #다른 cloud라면 = cycle이 없다면
            union(st,en)
            res+=w
    print('#{} {}'.format(test_case,res))