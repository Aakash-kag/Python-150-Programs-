#Write a Python program to sort words in alphabetic Order.

my_str = input("Enter a string: ")

words = [word.capitalize() for word in my_str.split()]

words.sort()
print("The sorted words are: ")
for word in words:
    print(word)