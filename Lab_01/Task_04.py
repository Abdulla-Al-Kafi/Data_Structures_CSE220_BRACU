def rotateRight(a,b):
  for i in range(0,b):
    temp=source[len(source)-1]
    for j in range(len(source)-1,0,-1):
      source[j]=source[j-1]
    source[0]=temp
  print(source)
source=[10,20,30,40,50,60]
rotateRight(source,3)