import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    #자성체들 존재
    #같은속도로 한칸씩 이동하여 충돌하면 종료
    #충돌이 이러나지 않는 경우 사라집니다.
    #S극을 시작으로 파란색 찾기
    #N극을 기준으로 빨간색 찾기
    dummy = int(input()) #100이라는 쓰레기값
    arr = [list(map(int,input().split())) for _ in range(100)]
    # 교착상태의 개수만 반환
    # 1은 N극 2는 S극 기준으로 둘 중 하나를 기준
    # N을 기준으로 할 예정
    cnt = 0
    for col in range(100):
        N_chk = 0
        for row in range(100):
            if arr[row][col] == 2: 
                if N_chk == 1:
                    cnt+=1
                    N_chk = 0
            elif arr[row][col] == 1:
                N_chk = 1
    print('#{} {}'.format(test_case ,cnt))


