import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    # 컨테이너 수 N, 트럭 수 M
    container = list(map(int,input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse = True)
    truck.sort(reverse = True)
    res = 0
    for i in range(N):
        j = 0
        while j < M:
            if truck[j] >= container[i]:
                truck[j] = 0
                res += container[i]
                break
            j += 1
    print('#{} {}'.format(test_case,res))