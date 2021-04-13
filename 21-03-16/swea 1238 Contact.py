import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    # 비상연락망 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
    # 탐색을 깊숙이 들어갔을 때 그 중 맥스값
    # 연락이 가능한 방향이 있다.
    N, start = map(int,input().split())
    #데이터 길이 N, 시작점 Start
    arr = list(map(int,input().split()))
    non_visit = []
    for i in range(N//2):
        non_visit.append([arr[2*i],arr[2*i+1]])
    non_visit.sort()
    move = 1
    last = [ start ]
    visit = [start]
    while non_visit:
        chk_list = non_visit[:]
        chk_last = []
        #print(chk_list)
        for t in last:
            #print(t)
            for i in chk_list:
                if i[0] == t:
                    if not i[1] in visit:
                        non_visit.remove(i)
                        #제거를 하고 chk_list에 추가
                        chk_last.append(i[1])
                        visit.append(i[1])

                #오름차순이므로 크면 break로 빠져나온다.
                if i[0] > t:
                    break
        #만족하는게 하나도 없다면
        if not chk_last:
            break
        #last 중복제거
        chk_last = list(set(chk_last))
        last = chk_last[:]
    print('#{} {}'.format(test_case,max(last)))

