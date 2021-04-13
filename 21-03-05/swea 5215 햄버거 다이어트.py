import sys
sys.stdin = open('input.txt','r')

def hamburger(cal,ingt):
    ing = ingt[:]
    if ing:
        tmp = ing.pop(0)
        if cal+tmp[1] > L:
            return hamburger(cal,ing)
        else:
            a1 = tmp[0]+hamburger(cal+tmp[1],ing)
            a2 = hamburger(cal,ing)
            return max(a1,a2)
    else:
        return 0

T = int(input())
for test_case in range(1,T+1):
# 햄버거 원하는 조합
# 재료에 대한 맛 점수
# 선호도 = 재료들의 맛 점수합
# 같은 재료 여러번 사용 X
# 칼로리만 제한
    N, L = map(int,input().split())
#N 재료수, L 칼로리 제한
    ingredient = [list(map(int,input().split())) for _ in range(N)]
    score = hamburger(0,ingredient)
    print('#{} {}'.format(test_case,score))


