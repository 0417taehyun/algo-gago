"""
구현07. 럭키 스트레이트
문제 : 점수 N이 럭키 스트레이트를 사용할 수 있는 상태인지 여부 출력
입력 : 점수 N      출력 : 럭키스트레이트 사용여부(LUCKY, READY)
럭키스트레이트를 사용할 수 있는 경우 :
점수 N을 자릿수를 기준으로 반으로 나누고, 각각 왼쪽의 수들의 합과 오른쪽의 수들의 합이 같으면 가능
"""
#입력 
#점수 N은 정수이지만, 자릿수를 기준으로 반으로 나누기 위해 리스트 형태로 저장되는 문자열타입을 그대로 사용
score = input()

#풀이1. 자릿수를 기준으로 N을 구분
#각각 왼쪽의 수와 오른쪽의 수를 구분하기 위한 리스트 left, right를 생성하고,
#점수문자열의 길이만큼 반복하되 길이의 절반이전과 이후로 나누어 각각 left, right에 대입
left = []
right = []
for i in range(len(score)):
  if i <= len(score)//2:
    left.append(score[i])
  else:
    right.append(score[i-len(score)//2])

#풀이2. 구분한 왼쪽 수의 합과 오른쪽 수의 합을 도출
#현재 문자열로 저장된 상태이기 때문에 int형으로 형변환을 해준 후 연산
sumL,sumR = 0,0
for i in range(len(left)):
  sumL += int(left[i])
  sumR += int(right[i])

#출력
if sumL == sumR:
  print("LUCKY")
else:
  print("READY")