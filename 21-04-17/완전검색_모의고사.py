def solution(answers):
    answer = []
    score = [0] * 3
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        #1
        if ans_1[i%5] == answers[i]:
            score[0] +=1
        #2
        if ans_2[i%8] == answers[i]:
            score[1] +=1
        #3
        if ans_3[i%10] == answers[i]:
            score[2] +=1
        
    for j in range(3):
        if score[j] == max(score):
            answer.append(j+1)
    return answer