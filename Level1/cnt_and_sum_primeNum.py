def cnt_prime(n): # 약수의 개수 반환하는 함수
    cnt = 0
    for i in range(2,int(n/2+1)):
        if n%i==0:
            cnt += 1
    if n==1:
        cnt += 1
    else:
        cnt += 2 # 1과 자기자신
    return cnt

def solution(left, right):
    result = 0
    for i in range(left,right+1):
        if cnt_prime(i) % 2==0:
            result += i
        else:
            result -= i
    return result
            

# 다른 풀이
# 제곱수는 약수의 개수가 홀수인 것을 이용(기억!) 
def solution(left,right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i

    return answer
