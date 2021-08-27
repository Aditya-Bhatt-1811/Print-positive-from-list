###########POSITIVE NUMBER ON LIST##############
a = list(map(int,input().split()))
temp = []

for i in range(len(a)):
  if a[i]>=0:
    temp.append(a[i])

print(temp)
