### 모험가 길드 

arr = list(map(int, input().split()))       # 입력받기
arr.sort(reverse=True)            # 내림차순 정렬 (큰 수 ~ 작은 수)
groups = 0                        # 그룹 수

while (True) :   
  if len(arr) == 0 :      # arr 배열의 길이가 0 이 되면 
    break                 # → While 문 탈출
  del arr[:arr[0]]        # 현재 arr 배열에서 가장 큰 숫자 개수만큼 요소 삭제 
  groups += 1             # → 그룹 하나 생성
  
print(groups)