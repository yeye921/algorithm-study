# 문자열이 숫자로만 구성돼있는지 확인 => isdigit()함수 이용 (문자열이 양의 정수인지 확인)
# 조건식에서 괄호 중요
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit()== True:
        return True
    else:
        return False   

# 최적화 코드
def solution(s):
    return s.isdigit() and (len(s)==4 or len(s)==6)

# 다른 풀이
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s)==4 or len(s)==6
