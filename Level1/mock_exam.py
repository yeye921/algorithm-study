def solution(answers):
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    cnt_A,cnt_B,cnt_C = 0,0,0

    for i in range(len(answers)):
        # 반복되는 배열의 인덱스 표현 방식
        a = i%5
        b = i%8
        c = i%10

        if A[a] == answers[i]:
            cnt_A += 1
        if B[b] == answers[i]:
            cnt_B += 1
        if C[c] == answers[i]:
            cnt_C += 1

    k = max(cnt_A,cnt_B,cnt_C)
    answer = []

    if k == cnt_A:
        answer.append(1)
    if k == cnt_B:
        answer.append(2)
    if k == cnt_C:
        answer.append(3)

    return answer



# 다른 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for i in range(len(answers)):
        if answers[i] == pattern1[i%len(pattern1)]: # 이전 코드와 동일한 방식 
            score[0] += 1
        if answers[i] == pattern2[i%len(pattern2)]:
            score[1] += 1
        if answers[i] == pattern3[i%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
