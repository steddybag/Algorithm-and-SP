import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N, B = map(int,input().split())
    #서점 abs(B-가질수있는합)의 최소값 산출
    arr = list(map(int,input().split()))
    #비트연산으로 부분집합 도출
    subset = []
    min_val = 9999
    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j):
                subset.append(arr[j])
        #print(subset)
        if min_val > (sum(subset)-B) >= 0:
            min_val = sum(subset)-B
        if min_val == 0:
            break
        subset = []
    print('#{} {}'.format(test_case,min_val))


