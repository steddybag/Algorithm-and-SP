import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    i = 0
    while 1:
        for j in range(1,6):
        #1씩 증가하면서 감소, 0보다 작아지므로 0으로 유지
            tmp = arr.pop(0)
            tmp -=j
            if tmp <= 0 :
                arr.append(0)
                break
            arr.append(tmp)
        if tmp <= 0:
            break
    print('#{} '.format(test_case),end='')
    print(*arr)