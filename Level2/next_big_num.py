# 2개 이하로 다른 비트 문제와 유사
# n을 1씩 증가시키면서 1의 개수 같을 때 반복문 탈출
def solution(n):
    i = n
    a = bin(n)[2:]
    i += 1
    b = bin(i)[2:]
    while a.count("1") != b.count("1"):
        i += 1
        b = bin(i)[2:]
    return int(b,2)  # 2진수로 표현된 문자열 b를 10진수 정수로 변환

# 다른 풀이
def solution(n):
    num1 = bin(n).count("1")  # 추후에 n이 변하므로 새 변수에 저장해 둠
    while True:
        n += 1
        if num1 == bin(n).count("1"):
           break
    return n 