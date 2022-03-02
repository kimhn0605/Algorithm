### 상하좌우

# U 명령이 무시되는 경우 -> x값이 1일 때
# D 명령이 무시되는 경우 -> x값이 n일 때
# L 명령이 무시되는 경우 -> y값이 1일 때
# R 명령이 무시되는 경우 -> y값이 n일 때

n = int(input())       # n 입력받기
plan = list(map(str, input().split()))    # plan 입력받아서 리스트로 저장
x, y = 1, 1            # 현재 x, y 좌표

while(True) :
  if len(plan) == 0 :       # 리스트에 더 이상 요소가 없으면 
    break                   # while 문 탈출
  elif plan[0] == 'U' :     # U 명령이고 x값이 1이 아니라면 x좌표-1
    if x != 1 :
      x -= 1          
    plan.pop(0)             # 명령이 끝난 요소 제거
  elif plan[0] == 'D' :     # D 명령이고 x값이 n이 아니라면 x좌표+1
    if x != n :
      x += 1
    plan.pop(0)             # 명령이 끝난 요소 제거
  elif plan[0] == 'L' :     # L 명령이고 y값이 1이 아니라면 y좌표-1
    if y != 1 :
      y -= 1
    plan.pop(0)             # 명령이 끝난 요소 제거
  elif plan[0] == 'R' :     # R 명령이고 y값이 n이 아니라면 y좌표+1
    if y != n :
      y += 1
    plan.pop(0)             # 명령이 끝난 요소 제거
    
print(x, y)