# 2진수로 변환시킨 후 나머지 저장시키고 배열(arr1)의 한 요소마다 2차원 배열의 한 행 결정됨 
def solution(n, arr1, arr2):
    ans = '' # 여기에 '#' 누적하기
    result = []
    arr = [[0]*n]*n  # 2차원 배열 생성
    # arr1 처리
    for i in range(n):
        arr[i] = remainder(arr1[i],n)
    
    # arr2 처리
    for i in range(n):
        tmp = remainder(arr2[i],n)
        for j in range(n):
            if arr[i][j] == 1:
                continue
            else:
                arr[i][j] = tmp[j]
    
    for i in range(n):
        ans = ''
        for j in range(n):
            if arr[i][j] == 1:
                ans += '#'
            else:
                ans += " "
        result.append(ans)
    print(result)
    return result
    

def remainder(n,l):
    r = ''
    while n !=0:
        r += str(n % 2)
        n = n // 2

    for i in range(l-len(r)):
        r += '0'
    r = r[::-1] # 문자열 뒤집기
    r = [int(a) for a in r] # 문자열 -> 정수 리스트 변환
    return r


    # 더 나은 풀이
    # 비트연산자 사용한 풀이 
    def solution(n, arr1, arr2):
        answer = []
        for i,j in zip(arr1,arr2):
            a12 = str(bin(i|j)[2:])
            a12=a12.rjust(n,'0')
            a12=a12.replace('1','#')
            a12=a12.replace('0',' ')
            answer.append(a12)
    return answer