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