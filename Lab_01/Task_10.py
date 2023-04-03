def repetition(a):
    count=0
    new_array=[0]*10
    for i in range(len(new_array)):
        for j in a:
            if i == j:
                count+=1
        new_array[i]=count
        count=0
    for i in range(len(new_array)-1):
        for j in range(len(new_array)-i-1):
            if new_array[j]>new_array[j+1]:
                temp=new_array[j]
                new_array[j]=new_array[j+1]
                new_array[j+1]=temp
    for i in range(len(new_array)-1):
        if new_array[i]>1:
            if new_array[i]==new_array[i+1]:
                return True
    return False       
a=[4,5,6,6,4,3,6,4]
print(repetition(a)) 