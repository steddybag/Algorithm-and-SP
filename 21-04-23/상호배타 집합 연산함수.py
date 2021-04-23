# p[x] : 노드 x의 부모 저장
# rank[x] : 루트 노드가 x인 트리의 랭크 값 저장

def Make_Set(x):
    p[x] = x
    rank[x] = 0

def Find_Set(x):
    if x!=p[x]:
        p[x] = Find_Set(p[x]) # Path Compression
    return p[x]

def Union(x,y):
    Link(Find_Set(x),Find_Set(y))

def Link(x,y):
    if rank[x] > rank[y]:
        p[y] =x
    else:
        p[x] = y

    if rank[x] == rank[y]:
        rank[y] += 1