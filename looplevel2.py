# !1️⃣ Ask for 5 numbers and print the largest one.
# num1=int(input("enter the 1st num"))
# num2=int(input("enter the 2st num"))
# num3=int(input("enter the 3st num"))
# num4=int(input("enter the 4st num"))
# num5=int(input("enter the 5st num"))

# if num1>num2 and num1>num3 and num1>num4 and num1>num5:
#     print("num1 is largest")
# elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
#     print("num2 is largest")
# elif num3>num2 and num3>num1 and num3>num4 and num3>num5:
#     print("num3 is largest")
# elif num4>num2 and num4>num1 and num4>num1 and num4>num5:
#     print("num4 is largest")
# else:
#     print("num 5 is greatest")


# nums = []

# for i in range(5):
#     n = int(input(f"Enter number {i+1}: "))
#     nums.append(n)

# print("The largest number is:", max(nums))


# nums=[]

# for i in range (5):
#     n=int(input(f"enter the {i+1} number"))
#     nums.append(n)
# print("the largest number is",max(nums))

#!Count how many vowels (a, e, i, o, u) are in a word.

# vowels=["a","e","i","o","u"]
# count=0

# word=input("enter the word")

# for char in word.lower():
#     if char in vowels:
#         count+=1
# print(count)

#!Reverse a string using a loop.
# st = input("Enter a string: ")

# rev = ""

# for char in st:
#     rev = char + rev    # add character to the front

# print("Reversed string:", rev)

# name="ram"
# rev=""

# for i in name:
#     rev= i + rev

# print(rev)


#!Count how many even numbers are in 1 to 50.

# count=0

# for i in range(1,51):
#     if i%2==0:
#         count+=1
# print(count)

#!5️⃣ Ask user for 10 numbers → print sum and average.


# num=[]
# sum=0

# for i in range (10):
#     numbers=int(input(f"enter the{i+1} numbers"))
#     num.append(numbers)

#     sum=sum +num[i]
    

# print(f"the sum is {sum}")
# avg=sum/10
# print(f"the avg is {avg}")


#! Print this pattern:
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)

#! 7️⃣ Print this pattern:
# *****
# ****
# ***
# **
# *

# i=5
# while i>=1:
#     print("*"*i)
#     i-=1

# for i in range (5,0,-1):
#     print("*"*i)


#!Ask for a number and check if it is prime.
# num=int(input("enter the number"))

# if num<=1:
#     print("not a prime num")

# else:
#     is_prime=True

#     for i in range(2,num):
#         if(num%i==0):
#             is_prime= False
#             break
            
#     if is_prime:
#         print("prime num")
#     else:
#         print("not prime num")

#!Print the factorial of a number.
# fact=1
# n=6
# for i in range(1,n+1):
#     fact=fact*i

# print(fact)    

#!🔟 Ask for a number → print all numbers divisible by 4 up to that number.

# n=int(input("enter the number"))

# for i in range(1,n+1):
#     if i%4==0:
#         print (i)



# for i in range(1,6):
#     print("*"*i)
# for i in range(5,0,-1):
#     print("*"*i)