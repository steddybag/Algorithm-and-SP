import sys
sys.stdin = open('input.txt','r')

T = 1
for t in range(T):
    test = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    min_count = 10000
    
    return_x = 0
    start_list = [i for i in range(99, -1, -1) if ladder[0][i]]
    #뒤로 해야 중복일 때 큰걸 선택
    
    for start in start_list:
       
        d_y = 0
        d_x = start
        #현재 사다리의 이동칸수를 저장하기 위한 변수
        count = 0
        #좌우이동을 방지하기 위한 변수
        move = 0

        #99라면 제일 밑이므로 더이상 계산할 필요가 없다.
        down = 0
        left = 1
        right = 2
        while d_y < 99:
            #밑으로 내려갔거나 왼쪽으로 이동했었다면
            #왼쪽으로 갈때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            if (move == down or move == left) and d_x > 0 and ladder[d_y][d_x-1]:
                #위의 조건을 통과했다면 왼쪽으로 이동후
                #이동했던 행동을 left로 기록한다.
                d_x -= 1
                move = left
            #밑으로 내려갔거나 오른쪽으로 이동했었다면
            #오른쪽으로 갈때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            elif (move == down or move == right) and d_x < 99 and ladder[d_y][d_x+1]:
                #위의 조건을 통과했다면 오른쪽으로 이동후
                #이동했던 행동을 right로 기록한다.
                d_x += 1
                move = right
            #왼쪽도 오른쪽도 못간다면 아래로 내려간다.
            #내려갈수있는지 체크했지만 그냥 else로 적어도 무방하다.
            elif ladder[d_y + 1][d_x]:
                #아래로 이동하고 행동을 down으로 바꾼다.
                d_y += 1
                move = down
            #이동을 할때마다 count를 기록해준다.
            count +=1
            #이동행동을 체크하는 이유는
            ##오른쪽으로 이동후 왼쪽과 오른쪽이 1인경우가 생긴다.###
            #그때 무한루프가 아닌단방향으로 이동

        #최종 계산값 확인(후보)
        if min_count > count:
            min_count = count
            return_x = start
        #중복되어도 위부터 계산했으므로 상관없다.

    print("#{} {}".format(test, return_x))

