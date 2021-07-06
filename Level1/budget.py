# 각 부서가 신청한 금액만큼을 모두 지원해야 함,최대한 많은 부서의 물품을 구매해주어야 함


# 정렬& 슬라이싱 이용해서 불필요한 연산 안함(순서가 앞일 수록 수가 작으니까)=> 0.01ms 걸림 
# 처음엔 조합을 이용하였으나 효율성 측면에서 x
def solution(d,budget):
    d.sort()
    for i in range(len(d),-1,-1):
        arr = d[:i]         # 맨 앞부터 차례로 뽑는 것만 체크함 for 시간단축
        if sum(arr) <= budget:
            return i        # 반환 값도 i


# 다른 풀이 (0.01~0.08ms)
def solution(d,budget):
    d.sort()
    while budget < sum(d): # 예산보다 더 크면 제일 큰 원소를 제거하는 방법 
        d.pop()
    return len(d)


# 다른 풀이2 (0.00ms)
def solution(d,budget):
    d.sort()
    cnt = 0
    for i in d:
        budget -= i     # d의 앞에서 부터 원소를 선택하는 방식 
        if budget < 0:  # 예산보다 더 클 경우 
            break
        cnt += 1
    answer = cnt
    return answer
