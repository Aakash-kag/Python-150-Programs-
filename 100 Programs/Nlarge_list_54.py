#Write a Python program to find N largest elements from a list.
def find_n_largest_element(lst,n):
    sorted_lst = sorted(lst,reverse = True)

    largest_elements = sorted_lst[:n]

    return largest_elements

numbers = [30,10,45,4,20,50,15,3,345,54,67,87,98,100,34,42]

N = int(input("N = "))

result = find_n_largest_element(numbers,N)

print(f"The {N} largest elements in the list are: ",result)