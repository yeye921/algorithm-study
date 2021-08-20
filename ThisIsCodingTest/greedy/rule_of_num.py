# 내 풀이
cnt = 0
res = 0
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
data.sort(reverse = True)

# m만큼 반복 수행
for i in range(m):
    if cnt < k: # cnt를 이용하여 k번을 초과하여 더해질 수 없도록 처리
        cnt += 1
        res += data[0]
    else:
        cnt = 0
        res += data[1]
print(res)


# 반복되는 수열의 특성을 이용한 풀이
n, m, k = map(int,input().split())
data = list(map(int,input().split()))
data.sort() # 입력받은 수 정렬

first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k 
count += m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기 (가장큰 수 * 가장 큰 수가 나오는 횟수)
result += (m-count) * second  # 두 번째로 큰 수 더하기

print(result) 