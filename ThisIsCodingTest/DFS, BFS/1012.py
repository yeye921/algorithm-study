from collections import deque

# 방향과 관련된 좌표 list 형태로 저장 [우, 좌, 상, 하]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 탐색을 시작할 좌표값과, 전제 땅 모양을 인자로 받는다
def dfs(start, ground):
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        # 확인한 구역은 0으로 바꿔주기
        ground[y][x] = 0
		
        # 상/하/좌/우 로 이동하면서 배추가 심어진 구역이 있는지 탐색한다.
        for move in dirs:
            move_y, move_x = y + move[0], x + move[1]
			
            # 배추를 심은 곳을 발견한다면, queue에 좌표값을 넣고, 그 지역을 중심으로 다시 탐색해본다
            if 0 <= move_y < N and 0 <= move_x < M and ground[move_y][move_x] == 1:
                queue.append((move_y, move_x))
                ground[move_y][move_x] = 0

# test case의 개수를 input 값으로 받기
test_num = int(input())


for i in range(test_num):
    M, N, K = map(int, input().split())
    # 땅을 나타내는 행렬을 0으로 초기화 시켜준다
    ground = [[0] * M for _ in range(N)]
    cnt = 0
    
    # 배추가 심어져 있는 구간을 입력받고, 해당하는 ground의 좌표를 1로 바꿔준다
    for j in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
	
    # ground의 모든 부분에 대하여 배추가 심어져 있는 구간이라면, 
    # dfs를 실행하여 인접한 배추가 있는지 확인한다.
    for w in range(M):
        for h in range(N):
            if ground[h][w] == 1:
                cnt += dfs((y, x), ground)

    print(cnt)