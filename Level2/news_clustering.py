# 문자열 자카드 유사도 => 교집합 크기 / 합집합 크기
# 영문자로 된 글자 쌍만 유효, 기타 공백,숫자,특수문자 => 글자쌍 버림
# 대문자와 소문자는 같게 취급
# 두 집합 모두 공집합일 경우 1로 정의
def solution(str1, str2):
    cnt = 0
    s1 = []
    s2 = []
    x = []
    y = []
    str1 = str1.lower()
    str2 = str2.lower()
    # str1 처리
    for i in range(len(str1)-1):
        if str1[i].isalpha() == False or str1[i+1].isalpha() == False: pass
        else: s1.append(str1[i]+str1[i+1])
    # str2 처리
    for i in range(len(str2)-1):
        if str2[i].isalpha() == False or str2[i+1].isalpha() == False: pass
        else: s2.append(str2[i]+str2[i+1])
    
    l1 = len(s1)
    l2 = len(s2)

    # 결과 계산
    if l1 > l2:
        x = s2
        y = s1
    elif l1 == l2: 
        x = s2 
        y = s1
    else: 
        x = s1
        y = s2
    for i in range(len(x)):
        if x[i] in y:
            y.remove(x[i])
            cnt += 1
    if s1 == [] and s2 == []:
        d = 1
    else: d = cnt / (l1+l2-cnt)
    return int(d * 65536)


# 더 나은 풀이 1
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    # 중복을 제거하고 값의 개수를 세는 방식
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

# 2
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536