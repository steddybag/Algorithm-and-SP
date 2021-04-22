a = [1,2,3,4,5]
for i in a:
    i = 2
print(a)

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
        p[c1]=c2
    else:
        p[c2]=c1