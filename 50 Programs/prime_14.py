#Write a Python program to Check Prime Number.
num = int(input("Enter a number: "))
flag = False
if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    #check for factors
    for i in range(2,num):
        flag = True
        break

if flag:
    print(f"{num}, is not a prime number")
else:
    print(f"{num},is a prime number")