# ! Ask for a number → print whether it is a perfect square.
# import math

# num=int(input("enter a number"))

# root=math.sqrt(num)


# if root.is_integer:
#     print("square")
# else:
#     print("not square")

#!2️⃣ Ask for a word → check if it is a palindrome (same forward & backward).

# word=input("enter the word")

# rev=word[::-1]

# if word==rev:
#     print("palendron")
# else:
#     print("not palendron")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# largest = a     # assume a is largest

# if b > largest:
#     largest = b

# if c > largest:
#     largest = c

# print("Largest number is:", largest)

#!4️⃣ Print Fibonacci series up to N:

# n = int(input("Enter how many terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

#!Ask for a number → count how many digits it has.
# n = int(input("Enter numbers: "))
# b=str(n)
# count=0

# for i in b:
#     count+=1
    
# print(count)

# print(len(b))

#!6️⃣ Ask for a number → print sum of its digits.
# n = int(input("Enter numbers: "))
# b=str(n)
# sum_digits=0

# for digit in b:
#     sum_digits += int(digit)

# print(sum_digits)

#!7️⃣ Guessing game:
# import math
# import random

# computer=random.choice([1,2,3,4])

# player=int(input("enter the number"))

# print(computer)

# if player==computer:
#     print("guessed right")
# else:
#     print("try again")

#!8️⃣ Print all prime numbers from 1 to 100.
# for num in range (2,101):
#     is_prime= True

#     for i in range (2,num):
#         if num%i==0:
#             is_prime=False
#             break

#     if is_prime:
#         print(num)


#! 9️⃣ Print this multiplication grid:
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# ...

# for i in range(1, 6):        # rows 1 to 5
#     for j in range(1, 6):    # columns 1 to 5
#         print(i * j, end=" ")
#     print()   # move to next line


#🔟 Ask for starting number → keep subtracting 3 until you reach 0 or negative.

num=int(input("enter the number"))

while num>0:
    num=num-3
    

print(num)