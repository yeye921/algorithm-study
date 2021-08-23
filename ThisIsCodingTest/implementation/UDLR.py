# 상하좌우 문제
# 내 풀이
n = int(input())
str = input().split()
x, y = 1, 1

# 방향에 따른 좌표 dictionary로 나타냄
dir = {"L":(0,-1), "R":(0,1),"U":(-1,0), "D":(1,0)}
for s in str:
    nx = x + dir[s][0] # 행
    ny = y + dir[s][1] # 열
    if 1<=nx<=n and 1<=ny<=n:
        x, y = nx, ny
print(x, y)


# 다른 풀이
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1] # 열을 나타냄
dy = [-1, 1, 0, 0] # 행을 나타냄
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)  