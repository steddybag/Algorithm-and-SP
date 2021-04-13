import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(1,T+1):
    N=int(input())
    cal = input()
    #cal 문자열 상태
    sign_stack = []
    num = []

    icp = {'*':2,'+':1,'(':0}

    for i in range(N):
        if cal[i].isdigit():
            num.append(int(cal[i]))
        else:
            #비어있는 경우
            if not sign_stack:
                sign_stack.append(cal[i])
            else:
                if cal[i] == ')':
                    while sign_stack[-1] != '(':
                        num.append(sign_stack.pop())
                    #(도 제거
                    sign_stack.pop()
                elif cal[i]=='(':
                    sign_stack.append(cal[i])
                elif icp[cal[i]] > icp[sign_stack[-1]]:
                    sign_stack.append(cal[i])
                else:
                    while icp[cal[i]] <= icp[sign_stack[-1]]:
                        num.append(sign_stack.pop())
                        if not sign_stack:
                            break
                    sign_stack.append(cal[i])
    if sign_stack:
       for i in sign_stack:
           num.append(i)

    val = []
    for i in num:
        if i == '*':
            a1 = val.pop()
            a2 = val.pop()
            val.append(a1*a2)
        elif i=='+':
            a1 = val.pop()
            a2 = val.pop()
            val.append(a1 + a2)
        else:
            val.append(i)
    print('#{} {}'.format(test_case,*val))


