### 음료수 얼려 먹기

# n, m 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n) :
  graph.append(list(map(int, input())))

# DFS 로 특정 노드 방문한 뒤에 연결된 모든 노드들도 방문 (깊이 우선 탐색)
def dfs(x, y) :
  # print(x, y) -> 아래 예시에서 출력 결과 참고
  
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m :
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0 :
    # 해당 노드 방문 처리
    graph[x][y] = 1

    # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False

# 아이스크림 개수 구하기
result = 0

for i in range(n) :
  for j in range(m) :
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True :
      # print("음료수!!!!!!!") -> 아래 예시에서 출력 결과 참고
      result += 1

print(result)

## 예시 (3 x 3) 
# 0 0 1
# 0 1 0 
# 1 0 1

## 출력 결과
# 0 0
# -1 0
# 1 0
# 0 0
# 2 0
# 1 -1
# 1 1
# 0 -1
# 0 1
# -1 1
# 1 1
# 0 0
# 0 2
# 음료수!!!!!!!
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 0 2
# 2 2
# 1 1
# 1 3
# 음료수!!!!!!!
# 2 0
# 2 1
# 1 1
# 3 1
# 2 0
# 2 2
# 음료수!!!!!!!
# 2 2
# 3