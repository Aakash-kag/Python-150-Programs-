#Write a Python program to Convert Decimal to Binary,Octal and Hexadecimal.

dec_num = int(input("Enter a decimal Number: "))

print("The decimal value of",dec_num, " is: ")
print(bin(dec_num),"in binary.")
print(oct(dec_num),"in octal.")
print(hex(dec_num)," in hexadecimal.")