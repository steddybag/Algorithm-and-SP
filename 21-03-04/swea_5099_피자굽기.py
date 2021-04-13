import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    #N개의 피자 규격 총 M개의 피자
    # 치즈의양 C는 C//2 한바퀴동안 큐방식 0이되면 꺼내고 남은피자 넣는다.
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    #마지막까지 남아있는 피자 번호
    pizza = [arr.pop(0) for i in range(N)]
    ind = [j for j in range(1,N+1)]
    j = N
    while 1:
        tmp = pizza.pop(0)
        tmp //= 2
        if tmp == 0:
            if arr:
                pizza.append(arr.pop(0))
                ind.pop(0)
                j += 1
                ind.append(j)
            else:
                ind.pop(0)
        else:
            pizza.append(tmp)
            ind.append(ind.pop(0))
            #index도 반영

        if len(pizza) == 1:
            break
    print('#{} {}'.format(test_case,*ind))
