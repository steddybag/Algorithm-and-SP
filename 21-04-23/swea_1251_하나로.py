import sys
sys.stdin = open("input.txt", "r")

def find_get(x):
    if p[x] != x:
        p[x] = find_get(p[x])
    return p[x]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    V = [(x[i],y[i]) for i in range(N)]
    E = float(input())

    p = [ i for i in range(N)]

    edge = []
    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = V[i]
            x2,y2 = V[j]
            L2 = (x1-x2)**2+(y1-y2)**2
            edge.append((i,j,E*L2))
    edge.sort(key=lambda x : x[2],reverse=True) #처리시간을 빠르게.. pop(0) = O(n)

    res = 0
    while edge:
        # 짧은 것 부터 선택
        st, en, w = edge.pop()
        a1 = find_get(st)
        a2 = find_get(en)
        if not a1 == a2:
            # 다른 cloud라면 = cycle이 없다면
            if a1>a2:
                p[a1] = a2
            else:
                p[a2] = a1
            res += w

    print('#{} {}'.format(test_case, round(res)))

