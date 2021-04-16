import sys
sys.stdin = open('input.txt','r')

def dfs(x,y,s):
    global res
    if x<0 or x>3 or y<0 or y>3:
        return

    if len(s) == 7:
        tmp = int(s)
        if tmp not in res:
            res.append(tmp)
    else:
        s += str(arr[x][y])
        dfs(x + 1, y ,s)
        dfs(x - 1, y, s)
        dfs(x , y + 1, s)
        dfs(x , y - 1, s)

T = int(input())
for test_case in range(1,T+1):
    # 격자판 중복 이동 가능
    # 벗어나는 경우 X
    arr = [list(input().split()) for _ in range(4)]
    # print(int('00017'))
    res = []
    for x in range(4):
        for y in range(4):
            dfs(x,y,'')

    print('#{} {}'.format(test_case,len(res)))