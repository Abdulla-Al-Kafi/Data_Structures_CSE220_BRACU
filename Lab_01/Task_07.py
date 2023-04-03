def splittingArray(a):
    total_sum = 0
    left_sum = 0
    right_sum = 0
    for number in a:
        total_sum+= number
    for number in a:
        left_sum+= number
        right_sum = total_sum-left_sum
        if (left_sum ==right_sum):
            return True
    return False
a=[10, 3, 1, 2, 10]
print(splittingArray(a)) 