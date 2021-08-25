# 게임 개발 문제

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0을 초기화 (포인트!)
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x,y좌표, 방향을 입력받기
x, y, dir = map(int,input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
arr = []
for i in range(n):
    arr.append(map(int,input().split()))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:   # 이 부분 이해안감!!!!!!!!!!!!!!!!!!!!!1
        dir = 3

# 시물레이션 시작
cnt = 1
turn_cnt = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
    else:
        turn_cnt += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x, y = nx, ny
        # 두기 바다로 막혀있는 경우
        else:
            break
        turn_cnt = 0

# 정답 출력
print(cnt)









