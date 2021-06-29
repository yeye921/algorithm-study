def solution(arr):
    result = 0
    for i in arr:
        result += i
    result = result/(len(arr))
    return result

// 더 간단한 방법 (단,배열의 길이가 1이상일 경우)
def solutin(list):
    return (sum(list)/len(list))

// sum(): Iterable인 list,tuple,dictionary의 합을 리턴하는 함수, 숫자만 가능
// sum(iterable): iterable의 합
// sum(iterable,start): start + iterable의 합
// +) sum(dict.values())
    
