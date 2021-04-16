import sys
sys.stdin = open('input.txt','r')

T = int(input())
don = [50000,10000,5000,1000,500,100,50,10]
for test_case in range(1,T+1):
    money = int(input())
    res = [0] * 8
    for i in range(8):
        res[i] = money//don[i]
        money %= don[i]
    print('#{}'.format(test_case))
    print(*res)