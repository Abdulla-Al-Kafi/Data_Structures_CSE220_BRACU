def removeAll(source, size, elements):
 
    ary_size=len(source)
    new_ary=[0]*ary_size
    k=0

    for i in source:
      if i==elements:
        continue
      else:
        new_ary[k]=i
      k+=1
    print(new_ary)



source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source, 7, 2)