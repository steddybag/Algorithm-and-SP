import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    N = float(input())
    #이진수 변화
    #소수점 아래 13자리 이상 필요하면 overflow
    res = ''
    while N != 0.0:
        res += str(int(2*N))
        N = N*2 - float(int(N*2))
        if len(res) > 12 :
            res = 'overflow'
            break
        # len가 시간이 오래걸리면 cnt라는 변수 이용 가능
    print('#{} {}'.format(tc,res))