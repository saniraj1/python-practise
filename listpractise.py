# fruits=["apple","banana","pineapple","papaya","kiwi"]
# print(fruits[1], fruits[-1])


# if "ball" not in fruits:
#     fruits.append("ball")

# print(fruits)

# !Make a new list containing squares of 1–10.
# square=[i*i for i in range(1,11)]
# print(square)

# square=[]

# for i in range (1,11):
#     square.append(i*i)

# print(square)

#!1. Ask the user for 5 numbers → store in a list → print the largest and smallest.
# num=[]

# for i in range(1,6):
#     user=int(input(f"enter {i} number"))
#     num.append(user)

# print("largest",max(num))
# print("largest",min(num))

# largest=num[0]
# smallest=num[0]

# for n in num:
#     if n> largest:
#         largest=n
#     if n< smallest:
#         smallest=n


# print("largest",largest)
# print("smallest",smallest)


2#!. Given a list of numbers, create a new list containing ONLY the even numbers.
# numbers= [1, 2, 3, 4, 5, 6]
# even=[]

# for i in numbers:
#     if (i%2==0):
#         even.append(i)

# print(even)

#! 3. Ask user for 5 words → store → print only the words with length > 3.

# words=[]


# for i in range(1,6):
#     user=input(f"enter {i} word")
#     words.append(user)
# print(words)

# for item in words:
#     if (len(item)>3):
#         print(item)

#!4. Reverse a list WITHOUT using [::-1] or .reverse().
# input= [10,20,30,40]

# output=[]


# for item in input:
#     output.insert(0,item)

# print(output)

#! 5️⃣ Remove duplicates from a list (keep only unique values)
num=[1, 2, 2, 3, 3, 3, 4]
real=[]

for i in num:
    if i not in real:
        real.append(i)
print(real)