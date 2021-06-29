# 문자열 곱셈, 슬라이싱 이용
def solution(phone_number):
    answer = '*' * (len(phone_number)-4)
    answer = answer +  phone_number[-4:]  # answer + 전화번호의 뒷 4자리
    return answer

# 최적화 코드
def solution(s):
    return "*"*(len(s)-4) + s[-4:]
