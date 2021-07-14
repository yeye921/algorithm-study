# 바로 앞번호/뒷번호 학생에게만 빌려줄 수 있음
# 예외처리(여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다) -> 이 학생은 빌려줄 수 x
# 최대한 많은 학생이 체육수업을 듣게 함
# result에서 1이면 빌려줄 수 있는 애, 0이면 수업가능, -1이면 도난으로 수업불가로 설정
def solution(n, lost, reserve):
    result = [0] * n
    cnt = 0
    
    for i in range(n):
        if i+1 in lost:
            result[i] -= 1
        if i+1 in reserve:
            result[i] += 1
        # 둘다 아니면 알아서 0임
    
    if result[0] == 1 and result[1] == -1:
        result[0] -= 1
        result[1] += 1
    elif result[n-1] == 1 and result[n-2] == -1:
        result[n-1] -= 1
        result[n-2] += 1

    for i in range(1,n-1):
        if result[i] == 1 and (result[i-1] == -1 or result[i+1] == -1):
            if result[i-1] == -1 and result[i+1] == -1:
                result[i] -= 1
                result[i-1] += 1
            elif result[i-1] == -1:
                result[i] -= 1
                result[i-1] += 1
            elif result[i+1] == -1:
                result[i] -= 1
                result[i+1] += 1

    for i in result:
        if i>=0:
            cnt += 1
    return cnt          # result에서 0의 개수가 수업들을 수 있는 최대 인원임


# 더 나은 풀이
# 전체 인원수에서 체육복 없는 인원수 빼주는 방식 
def solution(n,lost,reserve):
    _lost = [i for i in lost if i not in reserve] 
    _reserve = [i for i in reserve if i not in lost]
    # 여벌o and 도난o 인 학생은 두 곳에서 모두 제외 
    
    for i in _reserve:
        l = i - 1
        r = i + 1
        if l in _lost:
            _lost.remove(l)
        elif r in _lost:
            _lost.remove(r)
            
    return n-len(_lost)
