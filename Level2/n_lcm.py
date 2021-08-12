def lcs(a, b):
    if a % b == 0: return b 
    else: return lcs(b, (a % b))

def solution(arr):
    answer = 1 
    for i in arr: answer = (answer * i) / lcs(answer, i)
    return answer

# 더 나은 풀이
from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer