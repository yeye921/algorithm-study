# 나의 풀이 (틀림) 
# 문자열을 리스트로 변환 후 일 수행한 다음 join이용하여 다시 문자열로 변환하는 방식

def solution(s, n): 
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # 1. 배열을 직접 수정하는 방식  2. 새배열에 append하는 방식 3.새 문자열에 +하는 방식
    s = list(s)
    l_s = len(s)
    ans = [0] * l_s
    print(s)
    for i in range(l_s):
        l = len(s[i])
        if s[i] in lower_list:
            idx = lower_list.find(s[i][0])
            print(idx)
        elif s[i] in upper_list:
            print(s[i])
            print(s[i][0])
            idx = upper_list.find(s[i][0])
            print(idx)
        else: # 공백일 경우
            ans[i] = ' '
            
                    
    
    
            
# 더 나은 풀이 - 아스키 코드 사용
# chr(): 아스키코드 -> 문자, ord(): 문자 -> 아스키코드 
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
 
    return "".join(s)




# 다른 풀이
def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ind = low.find(char)+n # low 문자열에서 찾은 해당 알파벳 인덱스 + n
            answer += low[ind%26] # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능
        elif char in up:
            ind = up.find(char)+n
            answer += up[ind%26]
        else: # 공백일 경우도 고려
            answer += " "
    return answer
     

    
 
