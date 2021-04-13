import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    #N개의 숫자를 M맨뒤로 pop과 append queue반복
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        arr.append(arr.pop(0))
    tmp = arr.pop(0)
    print('#{} {}'.format(test_case,tmp))