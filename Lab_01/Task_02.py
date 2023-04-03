def RotateLeft(a,b):
  for i in range(0,b):
    temp=source[0]
    for j in range(0,len(source)-1):
      source[j]=source[j+1]
    source[len(source)-1]=temp
  print(source)
  
source=[10,20,30,40,50,60]
RotateLeft(source,3)