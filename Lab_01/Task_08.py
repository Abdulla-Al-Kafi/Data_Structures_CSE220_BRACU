def arraySeries(n):
  len_of_array=n*n
  array=[0]*len_of_array
  idx=len(array)-1

  for i in range(0,n):
    for j in range(0,n-i):
      array[idx]=j+1
      idx=idx-1
    idx=idx-i
  return array
user_input=int(input("N: "))
print(arraySeries(user_input))