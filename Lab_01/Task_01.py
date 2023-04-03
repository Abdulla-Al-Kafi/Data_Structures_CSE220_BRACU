def shiftLeft(a,b):
  for j in range(3):
    #print(j)
    for i in range(0,len(source)-1):
      # print(i)
      source[i]=source[i+1]
    source[len(source)-1]=0
    

  print(source)
  
source=[10,20,30,40,50,60]
shiftLeft(source,3)