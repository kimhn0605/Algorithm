### 럭키 스트레이트

n = list(input())
split = int(len(n) / 2)
front = n[:split]
back = n[split:]
front_sum, back_sum = 0,0

for i in range(split) :
  front_sum += int(front[i])
  back_sum += int(back[i])
if front_sum == back_sum :
  print("LUCKY")
else :
  print("READY")