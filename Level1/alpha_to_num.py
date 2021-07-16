''' 숫자면 문자열(ans)에 누적해서 더하고 영어면 다른 문자열(a)에 누적해서 더하고
함수를 통해 a가 숫자 영단어인지 확인하는 방식 '''

def solution(s):
    num = ['0','1','2','3','4','5','6','7','8','9']
    ans = ''
    x = ''
    
    for i in range(len(s)):
        if s[i] in num:
            ans += s[i]
            print(s[i],ans)
        else:
            x += s[i]
            a = alpha(x)
            if a in num:
                ans += a
                x = ''

    return int(ans)
            
def alpha(s):
    if s == "zero": return '0'
    elif s == "one": return '1'
    elif s == "two": return '2'
    elif s == "three": return '3'
    elif s == "four": return '4'
    elif s == "five": return '5'
    elif s == "six": return '6'
    elif s == "seven": return '7'
    elif s == "eight": return '8'
    elif s == "nine": return '9'





''' 세 가지 풀이 모두 숫자 영단어를 리스트나 딕셔너리에 저장해놓고 그것의 요소들이 주어진 문자열(s)에 존재하면
replace함수를 이용하여 숫자로 바꾸는 방식 이용 '''

# 더 나은 풀이 1
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        s = s.replace(key, value)
    return int(s)


# 2
def solution(s):
    d = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for k in d:
        s = s.replace(k, str(d[k]))

    return int(s)


# 3
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
