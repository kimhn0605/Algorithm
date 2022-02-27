### 문자열 재정렬

values = list(input())    
values.sort()      # 입력 받은 값 모두 오름차순 -> 숫자, 알파벳 순서대로 정렬됨
sum = 0            # 숫자 누적 합계

for i in range(len(values)) :       # 입력받은 길이만큼 반복
  if ord(values[i]) <= 57 :         # 아스키코드로 변환했을 때 57 이하라면 숫자라는 의미니까 
    sum += int(values[i])           # 정수형으로 변환 후 합계 누적
  else :                            # 숫자가 아니라면 알파벳이라는 의미니까
    print(values[i], end='')        # 하나씩 그대로 출력 (이미 정렬 O)
    
print(sum, end='')                  # 마지막에 누적 합계 출력

# ord() : 문자열을 아스키코드로 반환하는 함수
# ord('0') : 48, ord('9') : 57, ord('A') : 65,  ord('Z') : 90
