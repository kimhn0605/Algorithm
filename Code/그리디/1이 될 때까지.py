### 1이 될 때까지

n, k = map(int, input().split())  # n, k 입력받기
count = 0    # 실행 횟수

while (n != 1) :    # n 이 1 될 때까지 반복
  if n % k == 0 :   # 일단 n 이 k 로 나누어떨어지는 지 확인 
    n //= k      # 나누어 떨어지면 2번 과정 수행하고 count+1
    count += 1
  else :            # 나누어 떨어지지 않는다면
    n -= 1          # 1번 과정 수행하고 count+1
    count += 1
print(count)

# K 로 최대한 많이 나눌 수 있도록 하는 것이 최적의 해를 보장
# N 의 범위가 100억 이상의 큰 수라면 