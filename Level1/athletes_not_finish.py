# collections 모듈의 Counter 클래스는 dictionary를 확장한 클래스로, 
# 데이터의 개수를 효과적으로 셀 수 있는 기능을 제공
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

''' Counter(participant)는 participant의 각 요소들과 그 개수를 짝지어서 가지고 있기 때문에,
Counter(completion)을 빼 주게 되면 겹치는 요소들의 개수를 빼서 결과적으로 answer에는 단 하나의 이름(key)과 1(value)만 남게 된다.
따라서 answer.keys()를 list로 만들어 주면 0번째 인덱스가 완주하지 못한 선수의 이름이다.'''



# 다른 풀이(hash이용)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
