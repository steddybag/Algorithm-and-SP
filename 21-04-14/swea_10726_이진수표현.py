import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    #N,M일때 M의 이진수 표현의 마지막 N비트가 모두 1인지 확인
    N,M = map(int,input().split())
    tmp = '1'*N
    chk = bin(M)[2:]
    n_chk = len(chk)
    if n_chk >= N:
        if chk[n_chk-N:] == tmp:
            res = 'ON'
        else:
            res = 'OFF'
    else:
        res='OFF'
    print('#{} {}'.format(tc,res))