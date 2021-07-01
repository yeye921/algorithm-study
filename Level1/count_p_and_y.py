# count 함수 이용, 'p','y'가 하나도 없는 경우 처리
# 파이썬 논리 연산자(and,or)
# 개수 비교할 때 대/소문자 구별x(중요!)
def solution(s):
    s = s.lower()
    a = s.count('p')
    b = s.count('y')
    if a==0 and b==0:
        return True
    elif (a!=0 and b!=0) and (a==b):
        return True          
    else:
        return False
    
