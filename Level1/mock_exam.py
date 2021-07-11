def solution(answers):
    A = [1,2,3,4,5]
    B = [2,1,2,3,2,4,2,5]
    C = [3,3,1,1,2,2,4,4,5,5]
    cnt_A,cnt_B.cnt_C = 0

    for i in range(len(answers)):
        a = i%5
        b = i%8
        c = i%10

        if A[a] == answers[i]:
            cnt_A += 1
        if B[b] == answers[i]:
            cnt_B += 1
        if C[c] == answers[i]:
            cnt_C += 1

    max = max(cnt_A,cnt_B,cnt_C)
    answer = []

    if max == cnt_A:
        answer.append(1)
    if max == cnt_B:
        answer.append(2)
    if max == cnt_C:
        answer.append(3)

    return answer
