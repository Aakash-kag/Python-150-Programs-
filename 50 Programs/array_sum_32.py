#Write a Python Program to find sum of array.

arr = [1,2,3]
ans = sum(arr)

# print("Sum of the array is: ",ans)



def sum_of_array(arr):
    total = 0
    
    for element in arr:
        total += element
    
    return total

array = [1,2,3]
result = sum_of_array(array)
print("Sum of the array: ",result)