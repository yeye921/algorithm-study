# 시각 문제
# 완전탐색 - 가능한 모든 경우의 수를 검사하는 탐색방법

h = input()
cnt = 0

for i in range(h+1):        # 시
    for j in range(60):     # 분
        for k in range(60): # 초
            # 시각을 문자열로 나타내서 '3'포함 여부 확인
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
