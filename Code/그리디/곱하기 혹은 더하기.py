### 곱하기 혹은 더하기

values  = list(input())       

for value in values :       # 입력받은 문자를 하나씩 순회하면서
  if value == '0' :         # 0 이 존재하면 해당 '0' 제거 
    values.remove('0')      # -> 리스트에서 모든 '0' 이 제거됨. (remove 는 최초의 값만 삭제)
    
result = int(values[0])     # 초기값을 리스트의 첫 번째 요소로 지정

for i in range(1, len(values)) :      # 리스트 두 번째 요소부터 순회 
  if values[i] == '1' :               # 요소값이 1 이라면 (기존값 + 1)
    result += 1                       
  else :                              # 1 이 아닌 다른 숫자라면 (기존값 * 해당 숫자)
    result *= int(values[i])        
    
print(result)

# 0 나오면 어차피 +0 만 할 수 있으니까 처음부터 0 제거하고 시작
    