# s에서 0을 제외한 길이를 2진법으로 나타내기(s가 1이 될 때까지 반복)
# [이진변환 횟수, 제거된 0의 개수]
def solution(s):
    cnt_z = 0
    cnt_b = 0
    
    while s != "1":
        cnt_z += s.count("0")
        s = s.replace("0","")
        s = binary(len(s))
        cnt_b += 1
    return [cnt_b,cnt_z]
        
def binary(l):
    r = ''
    while l != 1:
        r += str(l % 2)
        l = l // 2
    r = r + '1'
    r = r[::-1]
    return r
        
# 더 나은 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]