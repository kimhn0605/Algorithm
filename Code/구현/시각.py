# 시각

## 3이 포함되는 모든 경우의 수
# hour : 3시, 13시, 23시
# minute : 3분, 13분, 23분, 30-39분, 43분, 53분
# seconds : 3초, 13초, 23초, 30-39초, 43초, 53초

n = input()
result = 0

for hour in range(int(n)+1) :
  for minute in range(60) :
    for seconds in range(60) :
      if str(hour)[0] == '3' :
        result += 1
      elif len(str(hour)) == 2 and str(hour)[1] == '3' :
        result += 1
      elif minute // 10 == 3 or minute % 10 == 3 :
        result += 1
      elif seconds // 10 == 3 or seconds % 10 == 3 :
        result += 1
        print(hour, minute, seconds)
        
print(result)

## 실패 원인
# 14, 16번째 줄 : str() 결과물은 문자열 -> 3 (x) '3' (o)
# 16, 18, 20번째 줄 : if 아니고 elif -> 해당 시각에 3 이 몇 번 들어갔는지는 상관없이 1 개라도 있으면 (result += 1) 하고 다음 시각으로 넘겨야 함