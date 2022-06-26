n,m = map(int, input().split())
smallest_number_row = []

for i in range(n):
    data = list(map(int, input().split()))
    minforrow = min(data)
    smallest_number_row.append(minforrow)

result = max(smallest_number_row)
print(f"{smallest_number_row.index(result)}줄의 :",result)
