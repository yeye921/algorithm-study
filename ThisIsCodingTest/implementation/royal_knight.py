# 왕실의 나이트 문제

# 내 풀이
str = input()
cnt = 0
col = str[0]
row = str[1]
steps = [(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] # 나이트가 이동할 수 있는 방향
s = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}             # 영어 -> 숫자로 변환
col = s[str[0]]

for s in steps: # 방향의 개수만큼 반복
    (next_col, next_row) = (col, row) + s
    if 1 <= next_col <= 8 and 1 <= next_row <= 8: # 이동한 위치가 체스판 내이면 +1
        cnt += 1

print(cnt)



# 다른 풀이
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자 -> 아스키 코드 값 -> 정수로 변환 (열의 시작이 1이므로 +1 해줌)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
