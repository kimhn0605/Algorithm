### 만들 수 없는 금액

n = int(input())
coins = list(map(int, input().split()))
coins.sort()              # 화폐 단위 오름차순 정렬

result = 1                # 양수 금액 중 최소 금액 -> 1원

for coin in coins :       # 화폐 단위 하나씩 순회
  if result < coin :      # result 값이 해당 화폐 단위보다 작다면
    break                 # 만들 수 없는 양의 정수 금액 중 최솟값은 그대로 result 니까 반복문 종료
  else :                  # result 값이 해당 화폐 단위보다 같거나 크다면
    result += coin        # 기존 result 값 + 해당 화폐 단위
    
print(result)

# result 값 미만까지는 화폐 단위로 만들 수 있는 금액