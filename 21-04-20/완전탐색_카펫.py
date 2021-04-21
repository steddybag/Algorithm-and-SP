def solution(brown, yellow):
    num = brown + yellow
    for i in range(3,int(num**0.5)+1):
        # i는 세로 길이
        if num % i == 0:
            garo = num//i
            if 2*(garo+i) - 4 == brown:
                break
    answer=[garo,i]
    return answer