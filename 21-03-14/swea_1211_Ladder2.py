import sys
sys.stdin = open('input.txt','r')

T = 1 # 문제에서 1개로 제한
for test_case in range(1,T+1):
    _ = int(input())
    #위의 Test case 쓰레기값 입력
    ladder = [ list(map(int,input().split())) for _ in  range(100)]

    min_cnt = 9999
    x_value = 0

    start_list = [i for i in range(99,-1,-1) if ladder[0][i]]
    #ladder 0의 행이 1이라면,,, 추가
    for start in start_list:
        y = 0
        x = start
        #초기값은 y 1행 start후보값을 시작

        cnt = 0
        move = 0 #초기값 down으로 시작
        #많이 생각하지마라 상식으로 시작하는게 맞다
        down = 0
        left = 1
        right = 2
        while y<99: # 99이상일 경우 종료
            if (move==down or move==left) and x>0 and ladder[y][x-1]:#index 위배 조건때문
                x-=1
                move=left
                #왼쪽으로 이동해오거나 아래쪽으로 내려왔을 때 방향이 left로 설정
                #꼭 교차점에서만 확인할 필요 없다.
            elif (move==down or move==right) and x<99 and ladder[y][x+1]:#index 위배 조건때문
                x+=1
                move=right
            elif ladder[y+1][x]: #아래가 경로라면 즉 교차점이 없다면,
                y+=1
                move = down #방향설정
            
            cnt+=1
        
        if min_cnt > cnt:
            min_cnt = cnt
            x_value = start
    print('#{} {}'.format(test_case,x_value))
