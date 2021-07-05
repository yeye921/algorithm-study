# while, cnt 이용
# 500번일 경우 처리 => if문 
def solution(num):
    cnt = 0
    while num !=1:
        if(num)%2 ==0:
            num /= 2
            cnt += 1
        else: 
            num = num*3+1
            cnt += 1
        if cnt == 500:
            return -1
    return cnt
        
            
        
