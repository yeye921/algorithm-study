# 바이러스 문제

from collections import deque

n = int(input()) # 컴퓨터(노드)의 개수
m = int(input()) # 간선의 개수
v = 1            # 시작 노드 번호
cnt = 0

graph = [[0]*(n+1) for _ in range(n+1)] # 그래프 생성
visited = [False] * (n+1) # 방문 처리 리스트

# 노드 연결
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(v):
    global cnt
    visited[v] = True # 노드 방문 처리
    for i in range(n+1):
        if graph[v][i] == 1 and visited[i] == False: # 노드 1과 연결된 노드이고 방문하지 않았으면
            cnt += 1
            dfs(i)
def bfs(v):
    global cnt
    queue = deque() # 큐 생성
    queue.append(v)
    visited[v] = True # 포인트 - 1 (큐에 넣고 방문처리)
    
    while queue: # 큐가 빌 때 까지
        v = queue.popleft() # 최 상단 노드 꺼냄
        for i in range(n+1):
            if graph[v][i] == 1 and visited[i] == False:
                cnt += 1
                queue.append(i)
                visited[i] = True  # 포인트 - 2


bfs(1)
print(cnt) # bfs 수행했을 때 결과

# 초기화
cnt = 0
visited = [False] * (n+1)

dfs(1) # dfs 수행했을 때 결과
print(cnt) # 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수