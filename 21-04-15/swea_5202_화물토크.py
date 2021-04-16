import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = []
    res = []
    for i in range(N):
        s, e = map(int,input().split())
        arr.append((s,e))
    arr = sorted(arr,key=lambda a: a[1])
    # 종료시간을 기준으로 정렬

    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i])
            #상관없다 1 3 / 2 3 중 아무거나 들어가도 맨 앞에 것이므로 대신 최소사용시간일 경우 달라진다.
        elif res[-1][1]<=arr[i][0]:
            res.append(arr[i])
    print('#{} {}'.format(test_case,len(res)))