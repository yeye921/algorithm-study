# 나의 풀이 (틀림) 
# 문자열을 리스트로 변환 후 일 수행한 다음 join이용하여 다시 문자열로 변환하는 방식
# 리스트 원소를 탐색하면서 0이 나올때마다 이전 것을 처리하는 방식으로 함
def solution(s, n): 
    lower_list = "abcdefghijklmnopqrstuvwxyz" 
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    
    # 1. 배열을 직접 수정하는 방식  2. 새배열에 append하는 방식 3.새 문자열에 +하는 방식
    
    # split을 이용해서 리스트에 저장하는 방식 이용
    # 나중에 join이용해서 문자열로 바꿀 때 공백으로 연결
    s = s.split()
    print(s)
    
    for i in range(len(s)):
        print(s[i])
        l_s = len(s[i])
        if s[i].islower() ==  True:
            idx = lower_list.find(s[i][0])
            s[i] = lower_list[(idx + n) % 26: (idx + n + l_s) % 26]
            # 문제가 되는 부분 [25:3] or [3:28(2)]일 경우 자르기가 힘들어짐... 그럼 어떻게 하지??
            # [2:29]일 경우도 [2:3]으로 변환되어 문제 발생함
            # 다른 방식 사용해야될 듯 

        elif s[i].isupper() == True:
            idx = upper_list.find(s[i][0])
            s[i] = upper_list[(idx + n) % 26: (idx + n + l_s) % 26]
    
       

    s = " ".join(s)
    return s
    
            
            
            
        
    
    
            
            

    
 
    
            
            
            
        
    
                   
    
    
            
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
     

    
 
