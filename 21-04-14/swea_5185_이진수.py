import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    #N과 16진수
    N,M = input().split()
    res=''
    for i in M:
        res+=bin(int('0x'+i,16))[2:].zfill(4)
    print('#{} {}'.format(tc,res))