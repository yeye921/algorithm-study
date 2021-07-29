# 문제 설명 추가
# 공백이 첫문자에 올 수도, 반복되어 나올 수도 있음 (공백은 문자로 치지 않음) - 중요


# 내 틀린 풀이
# 첫 문자가 영문인지/아닌지 확인, 모두 소문자로 변환 후 맨 앞글자만 대문자로 변경
# 문자 사이에 공백 개수 세서 그 개수대로 띄어서 합치기 <= 어떻게 하지? 
def solution(s):
    s = s.split() # < = 잘못된 부분
    for i in range(len(s)):
        if s[i][0].isalpha() == False:
            s[i] = s[i].lower() # 이어지는 영문을 소문자로 씀
        else:
            s[i] = s[i].lower() # 먼저 소문자로 변환 후, 맨 앞글자만 대문자로 바꿔줌
            s[i] = s[i].replace(s[i][0],s[i][0].upper(),1) # replace 쓸 때, 꼭 대입해줘야 함!
    
    print(" ".join(s))
    return " ".join(s)


# 더 나은 풀이 1
def solution(s):
    s = s.lower()  # 모두 소문자로 변환
    L=s.split(" ") # 공백 1개를 기준으로 나눔 (중요!!)
    print(L)
    answer = ""
    for i in L:
        i= i.capitalize() # 단어별로 앞글자만 대문자화해주는 capitalize함수를 사용
        answer+= i+" "    # 단어 사이에는 공백이 하나만 있다고 가정한 풀이
        print(i,answer)
    return answer[:-1]    # 맨 끝에 붙는 공백은 제거

# 2
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])