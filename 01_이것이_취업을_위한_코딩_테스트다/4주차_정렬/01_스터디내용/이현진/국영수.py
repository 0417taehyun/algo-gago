#입력
n = int(input())
array = []
for i in range(n):
  name,kor,eng,mat = input().split()
  array.append([name,int(kor),int(eng),int(mat)])

#정렬
def setting(data):
  return data[1]

array.sort(reverse=True, key=setting) #1st 기준

for i in range(len(array)):
  if array[i][1] == array[i+1][1]:
    if array[i][2] > array[i+1][2]:
      array[i], array[i+1] = array[i+1], array[i]
    elif array[i][2] == array[i+1][2]:
      if array[i][3] < array[i+1][3]:
        array[i], array[i+1] = array[i+1], array[i]
      elif array[i][3] == array[i+1][3] and ord(array[i][0]) > ord(array[i+1][0]):         
        array[i], array[i+1] = array[i+1], array[i]

#출력
for a in array:
  print(a[0])