"""
문제 :
- 주어진 문자열 s를 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 압축
- 압축할 때, 반복되는 문자의 개수단위는 가변적이며 가장 짧게 압축해내도록 한다
풀이 :
1) 압축할 단위 구하기
- 기준점을 잡아 바로 다음 동일한 문자를 찾은 후, 해당 문자들로부터 오른쪽의 문자가 몇개까지 동일한지 찾는다
  이를 토대로 기준점을 '키'로 갖고 동일한 문자의 개수를 '값'으로 가지는 사전을 만든다
- 만들어진 사전의 값을 뽑아내어 크기순으로 정렬하고, 해당 값이 문자열을 정확히 나눌 수 있는지 확인한다
  위의 과정을 모두 만족시키는 값이 해당 문자열을 "압축할 단위"이다
2) 단위대로 압축하기
- 비교연산을 위한 임시리스트를 생성하여 단위대로 구분한 문자열을 저장한다
  이후 저장해둔 임시 리스트들을 서로 비교하여 일치하면 개수를 증가시킨다
- 더이상 같은 문자열이 반복되지 않으면 다시 개수를 초기화하고 위의 과정을 반복한다
"""
def compact(s):
  alpha = dict()

  for i in range(len(s)-1):
    for j in range(i,len(s)):
      if s[j] == s[j+1]:
        alpha[s[j]] += 1

  values = alpha.values().sort()
  max = 0
  
  for i in values:
    if len(s)%i == 0:
      max = i
      break

  temp = ""
  result = ""
  count = 0

  for i in range(2,len(s)):
    for j in range(max):
      temp[i] += s[j+i]
      if temp[i] == temp[i-1]:
        count += 1
      else:
        result += str(count)
        result += temp[i]
        count = 0
  
  return count(result)