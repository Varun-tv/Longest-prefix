# c = ["light","live","liver"]
#c =  ["light","racecar","car"]
c = ["flower","flow","flight"]
def min_list(c):
  min = c[0]
  for i in c:
    if len(i) < len(min):
      min = i
  return min
min = min_list(c)
pre = []
for j in range(0,len(c)):
  for i in range(0,len(min)):
    if min[i] != c[j][i]:
      pre.append(min[:i])

print(min_list(pre))
