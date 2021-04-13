import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    arr = input().split()
    # 탐색하다가 숫자면 stack에 대입
    # 연산자면 계산후 stack에 추가
    cal = ['+','-','*','/']
    num = []
    res = 'error'
    for i in arr:
        if i == '.':
            if len(num) == 1:
                res = num[0]
            break
        elif i in cal:
            if len(num) >=2:
                a2 = num.pop(-1)
                a1 = num.pop(-1)
                #순서 중요
                if i == '*':
                    num.append(a1*a2)
                elif i == '+':
                    num.append(a1+a2)
                elif i == '/':
                    num.append(a1/a2)
                elif i == '-':
                    num.append(a1-a2)
            else:
                break
        else:
            num.append(int(i))
    print('#{} {}'.format(test_case,res))