# x의 자릿수의 합 구하기 => 문자열로 바꿔서 슬라이싱 후, 정수형으로 결과값에 더함 
def solution(x):
    x = str(x)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    if int(x) % sum ==0:
        return True
    else: return False 


# 최적화 코드 
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0

