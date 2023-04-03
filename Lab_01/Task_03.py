def shiftRight(a,b):
  for j in range(b):
    for i in range(len(source)-1,0,-1):
      source[i]=source[i-1]
    source[0]=0
  print(source)

source=[10,20,30,40,50,60]
shiftRight(source,3)