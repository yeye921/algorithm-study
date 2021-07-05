# 리스트의 정렬(sort, 내림차순) 이용
# 대소문자 구별 함수 이용(isupper,islower)
def solution(s):
    upp = []
    arr = []
    for i in range(len(s)):
        if s[i].islower() == True:
            arr.append(s[i])
        else:
            upp.append(s[i])
    upp.sort(reverse=True)
    arr.sort(reverse=True)
    arr += upp
    arr = "".join(arr) # 리스트를 문자열로 변환(join함수 이용)
    return arr


# 최적화 코드
# 대소문자 구별 필요없이 sort함수이용하면 알아서 정렬!(기억)
# for 정렬, 문자열이 가진 문자들을 하나씩 잘라 리스트에 저장한뒤 정렬하고 다시 문자열로 변경
# sorted쓰면 문자열이 자동으로 정렬된 리스트가 됨!
def solution(s):
    return ''.join(sorted(s,reverse=True))
  # return ''.join(list(s).sort(reverse=True)) 로 하면 오류남 
