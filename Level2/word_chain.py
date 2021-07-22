# 중복확인: 한 명 말할 때 마다 not in으로 확인하고 배열에 넣는 방식
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어 말해야 함 & 한 글자 단어는 인정x
def solution(n, words):
    arr = []
    l = len(words)
    
    if len(words[0])>1:        # 첫번째 단어는 길이만 체크하고 그냥넣음
        arr.append(words[0])
    
    for i in range(1,l):
        if (words[i][0] == words[i-1][-1]) and (words[i] not in arr):
            arr.append(words[i])
            if i == l-1:        # 배열의 끝까지 탈락자가 생기지 않는 경우
                return [0,0]
        else:
            return [(i%n)+1,(i//n)+1]


# 더 나은 풀이
# 굳이 새배열에 append하면서 확인할 필요 없이, 규칙을 만족하지 않은 조건 & 기존배열에 슬라이싱 이용
# 내 방식대로 하면 탈락자가 생기지 않는 경우를 위해 길이까지 체크해야 하는데
# 아래처럼 규칙을 만족하지 않는 조건을 if문에 넣으면 그럴 필요 없음
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: 
            return [(p%n)+1, (p//n)+1]
    else:               # for문 끝까지 다 돌고 if문을 만족하지 않으면
        return [0,0]