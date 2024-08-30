#Write a Python program for array rotation.

def rotate_array(arr, d):
    n = len(arr)

    if d < 0 or d >= n:
        return "Invalid rotation value"
    
    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    return rotated_arr
# Input array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Number of positions to rotate
d = 2
# Call the rotate_array function
result = rotate_array(arr, d)
# Print the rotated array
print("Original Array:", arr)
print("Rotated Array:", result)