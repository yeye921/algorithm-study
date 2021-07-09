# 문자열 내 마음대로 정렬하기

# n번째 수를 글자 앞에 붙인 뒤, 정렬 후 원상복귀 
def solution(strings,n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]

    strings.sort()

    for j in range(len(strings)):
        answer.append(strings[j][1:])

    return answer



# 다른 풀이
def solution(strings,n):
    return sorted(sorted(strings),key=lamda x: x[n])
