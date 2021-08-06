def solution(numbers):
    #0. key point
    numbers_str = [str(num) for num in numbers]              #1. 사전 값으로 정렬하기
    numbers_str.sort(key=lambda num: num*3, reverse=True)    #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    return str(int(''.join(numbers_str)))
    # 만약 numbers=[0,0,0,0] 이라면 0 이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.

# 다른 풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer