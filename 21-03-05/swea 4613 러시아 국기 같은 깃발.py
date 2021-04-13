import sys
sys.stdin = open('input.txt','r')

# 러시아 국기를 만든다
# 깃발 N행 M열
# 흰색 파란색 빨간색 중 하나 W B R
# 위에서 최소 한줄
# 흰색 파란색 빨간색 순
# 첫줄 흰색으로 하고 생각 나머지
def change_color(row, color):
    num_w = flag[row].count('W')
    num_r = flag[row].count('R')
    num_b = flag[row].count('B')
    if row == N-1:
        if color == 'R':
            return num_w+num_b
        elif color == 'W':
            return 9999
        elif color == 'B':
            return 9999
    elif color == 'W':
        return num_r + num_b + min(change_color(row+1,'W'),change_color(row+1,'B'))
    elif color == 'B':
        return num_w + num_r + min(change_color(row+1,'B'),change_color(row+1,'R'))
    elif color == 'R':
        return num_b+ num_w + change_color(row+1,'R')

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    cnt = change_color(0,'W')

    print('#{} {}'.format(test_case,cnt))

