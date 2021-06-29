# for, if문 이용
def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)): 
        if signs[i]:                # if문에서 boolean
            result += absolutes[i] 
        else: 
            result += absolutes[i] * -1
    return result


# 최적화 풀이(sum,zip함수)
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
