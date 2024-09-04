#Write a python program to Cloning or Copying a list.
original_list = [1,2,3,4,5]

cloned_list = original_list[:]
print(cloned_list)


original_list2 = [1,2,3,4,5]

copying_list = list(original_list)
print(copying_list)


original_list3 = [1,2,3,4,5]

cloned_list2 = [item for item in original_list3]
print(cloned_list2)