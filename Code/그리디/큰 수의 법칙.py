### 큰 수의 법칙

## 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주함.

n, m, k = map(int, input().split())     # n, m, k 입력받기
arr = list(map(int, input().split()))   # n 개의 숫자 입력받기
arr.sort()        # sort() 함수 사용 시 변수에 할당 x (None 반환)

result = 0        # 큰 수의 법칙에 따른 출력 결과 
count = 0         # 현재까지의 연산 횟수 (m 과 동일해지면 종료)
                  
while (True) :  
  if (m - count) == 0 :     # m-count : 남은 연산횟수가 0이라면 
    break                   # while 문 탈출
  
  a = (m - count) // k      # a : 남은 연산횟수 // 최대 반복 횟수
  
  if a >= 1:                # a 값이 1 이상이라면
    result += arr[-1] * k   # 가장 큰 숫자를 k 번 만큼 곱해서 한꺼번에 더해주기
    count += k              # 현재까지의 연산 횟수 업데이트 (k 만큼 증가)
    
  if (m - count) > 0 :      # 남은 연산 횟수가 0 이 아니라면
    result += arr[-2]       # 두 번째로 큰 수 1번 더해주기
    count += 1              # 현재까지의 연산 횟수 업데이트 (1 증가)
    
print(result)

