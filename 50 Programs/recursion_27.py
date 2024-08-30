#Write a Python Program to Display Fibonacci Using Recursion
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    

nterms = int(input("Enter the number of terms (greater than 0): "))

if nterms <= 0:
    print("please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(recur_fibo(i))