import sys
sys.stdin = open("input.txt", "r")

T = int(input())
code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
#맨뒤에 항상 1이 있다.
for test_case in range(1, T + 1):
    #암호코드 규칙
    #(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드
    N, M = map(int,input().split())
    #N 세로크기 M 가로크기
    #세로 50 가로 100
    arr = []
    idx = 0
    for i in range(N):
        arr.append(list(input()))
        if idx==0 and '1' in arr[i]:
            idx = i
            #불필요하게 in 함수 사용 금지
    tmp = arr[idx] #해당 tmp만 판단
    #맨뒤에 1이 있는걸 이용하면
    for i in range(M-1,-1,-1):
        if tmp[i] == '1':
            end = i+1
            break
    #총 8자리
    sum = 0
    num = 0
    for i in range(8):
        chk = ''.join(tmp[end-7:end])
        #list 문자열로 변환
        end = end - 7
        if i == 0: #첫번째 자리 일때,
            sum += code[chk]
            num += code[chk]
        elif i%2 == 1:
            #홀수 자리
            sum += code[chk]*3
            num += code[chk]
        else:
            #짝수 자리
            sum += code[chk]
            num += code[chk]
    if sum%10 != 0:
        num = 0

    print('#{} {}'.format(test_case,num))