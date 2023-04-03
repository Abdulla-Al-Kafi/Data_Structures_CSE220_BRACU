def maxBunchCount(a):
  count=1
  max=0
  for i in range(len(a)-1):
    if a[i]==a[i+1]:
      count+=1
    else:
      max=count
      count=1
    if count>max:
      max=count
  return max

a= [1, 2, 2, 3, 4, 4, 4] 
print(maxBunchCount(a)) 