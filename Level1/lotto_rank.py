# 순서와 상관없이 일치하는 번호가 있으면 맞은걸로 인정!
# 일치번호 카운팅 & 0개수 카운팅하는 방식이용

def solution(lottos, win_nums):
    zero, cnt = 0,0 
    
    for i in range(6):
        if lottos[i] == 0:
            zero += 1       # 알 수 없는 번호(0)의 개수
        else:
            if lottos[i] in win_nums: 
                cnt += 1
    
    arr = [cnt+zero,cnt]    # [최고순위,최저순위]

    for i in range(2):
        if arr[i] == 6:
            arr[i] = 1
        elif arr[i] == 5:
            arr[i] = 2
        elif arr[i] == 4:
            arr[i] = 3
        elif arr[i] == 3:
            arr[i] = 4
        elif arr[i] == 2:
            arr[i] = 5
        elif arr[i] <= 1:
            arr[i] = 6
            
    return arr


# 더 나은 풀이
def solution(lottos,win_nums):
    rank = [6,6,5,4,3,2,1] # rank를 리스트로 만든게 포인트!
    
    cnt = 0
    cntz = lottos.count(0) # 0의 개수 카운팅
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    return rank[cnt+cntz],rank[cnt] # rank 리스트에 맞춘개수를 인덱스로 넣어 [최고순위,최저순위]로 만듬




# 다른 풀이
def solution(lottos,win_nums):
    rank = {
        0:6,
        1:6,
        2:5,
        3:4,
        4:3,
        5:2,
        6:1
        }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
