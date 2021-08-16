# 구명보트가 몇개 팔요한지만 구하면 됨!
def solution(people,limit):
    ans = 0
    people.sort()

    a = 0
    b = len(people) - 1

    # 인덱스를 양옆에서 좁혀오면서 확인
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            ans += 1
        b = -1
    return len(people) - ans # 포인트

# 다른 풀이
def solution(people,limit):
    ans = 0 # 필요한 보트의 개수
    poo = sorted(people)
    while poo:
        # 보트에 1명씩 탈 2가지 경우
        if len(poo) == 1:
            ans += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            ans += 1
        
        # 보트에 2명씩 탈 경우
        else:
            poo.pop(0)
            poo.pop()
            ans += 1
    return ans
            