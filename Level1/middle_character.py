# //연산자이용, 문자열 슬라이싱
def solution(s):
    a = len(s)//2 # 가운데 글자 찾는데 이용,소수점 버리기
    if len(s)%2 ==0 :
        return s[a-1:a+1]
    else: return s[a]

# 최적화 풀이
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]  # 짝수,홀수case 나눌 필요없이 계
