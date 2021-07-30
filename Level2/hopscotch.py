# 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없다
# 마지막 행까지 내려왔을 때 얻을 수 있는 점수의 최대 값을 리턴
# 아래 두가지 풀이 모두 자기 자신의 열을 뺀 나머지 중 최대값을 밑으로 계속 더해주는 방식

def solution(land):

    for i in range(1,len(land)):
        for j in range(4):# 이전 행에서 같은 열을 제외한 것 중, 가장 큰 수 구해서 더함
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:]) 
                          
    return max(land[-1]) # 마지막 행(모두 누적해서 더해진 것)에서 가장 큰 수 


# 내 풀이 (틀림)- 그리디로 품
def solution(land):
    a = [] # 최대 값들을 담는 리스트
    c = [] # 밟은 열들을 담는 리스트
    n = len(land) # 행 개수
    #m = len(land[0]) # 열 개수
    
    for i in range(n):
        m = max(land[i])
        ind = land[i].index(m)
        if i == 0:
            a.append(m)
            c.append(ind)
        else:
            if ind == c[-1]:
                land[i][ind] = 0 # 최솟값으로 설정해서 제외시킴
                a.append(max(land[i]))
                c.append(land[i].index(max(land[i])))
            else:
                a.append(m)
                c.append(ind)
                        
    return sum(a)