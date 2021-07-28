# 리스트에 n번째 피보나치 수들을 저장해 놓고 꺼내서, 1234567로 나눈 나머지를 리턴하는 방식
# 시간이 생각보다 오래 걸릴 수도 있음 (450ms)
def solution(n):
    a = [0,1]
    for i in range(2,n+1):
        a.append(a[-1] + a[-2])
    
    # a[n] 대신 a[-1] 사용가능(같은의미)
    if a[n] < 1234567:
        return a[n]
    else:
        return a[n] % 1234567

# 더 나은 풀이
# 장점: 리스트에 따로 저장하지 않아, 메모리를 적게 사용
def solution(n):
    a,b = 0,1
    for i in range(n): # a는 n번째 피보나치 수를 나타냄
        a,b = b,a+b
    
    if a <1234567: return a
    else: return a % 1234567
