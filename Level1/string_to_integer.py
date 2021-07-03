# 문자열의 슬라이싱 이용후, 정수로 변환
def solution(s):
    result = 0
    if s[0] == '+' :
        result = int(s[1:])
    elif s[0] == '-' :
        result -= int(s[1:])
    else:
        result = int(s[0:])
    return result

# int()함수이용하여 문자열->정수로 변환 (+,-는 알아서 양,음의 기호로 인식)
def solution(s):
    result = int(s)
    return result


        
