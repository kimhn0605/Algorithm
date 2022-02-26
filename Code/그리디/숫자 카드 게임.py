### 숫자 카드 게임

n, m = map(int, input().split())    # n, m 입력받기     
minimums = []    # 각 행의 최솟값 담을 배열 (함수 이름과 동일한 변수 사용 x)  

for i in range(n) :                              # 입력받은 행 개수만큼 반복하여
  numbers = list(map(int, input().split()))      # 행별로 numbers 변수에 저장
  
  mini = min(numbers)           # 각 행의 최솟값을 구해서 
  minimums.append(mini)         # minimums 배열에 추가            
  
print(max(minimums))            # minimums 배열 중 최댓값 출력


# 각 행에서 가장 작은 수를 찾은 다음 그 수 중에서 가장 큰 수 찾기