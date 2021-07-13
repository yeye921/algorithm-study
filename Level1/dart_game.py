# 점수 & 보너스 처리한 다음에 배열에 넣음, 옵션은 배열안의 원소에 처리

def solution(dart):
    n = ''    # n이 문자열이어야 10일 경우 +로 처리가능해짐
    score = []
    for i in dart:
        if i.isdigit():
            n += i
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n == int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n == int(n)**3
            score.append(n)
            n = ''
        elif i == '#':
            score[-1] *= -1
        elif i == '*':
            if len(score)>1:
                score[-1] *= 2
                score[-2] *= 2
            else:
                score[-1] *= 2

    return sum(score)
        
