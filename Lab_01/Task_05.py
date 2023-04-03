def remove(a,b,c):
  for i in range(c,len(source)-1):
      
    source[i]=source[i+1]
  source[len(source)-1]=0
    

  print(source)
  
source=[10,20,30,40,50,0,0]
remove(source,5,2)