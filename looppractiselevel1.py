# level 1 
#!Print numbers from 10 to 1 (reverse order).
# num= 10

# while num>=1:
#     print(num)
#     num-=1
    

# for i in range (10,0,-1):
#     print(i)

#!Print the sum of numbers from 1 to 50.


# total = 0

# for i in range(1, 51):
#     total = total + i   # or total += i

# print(total)

#!Print all odd numbers from 1 to 30.

# for i in range (1,31,2):
#     print(i)
    

# for i in range (1,31):
#     if i%2 !=0:
#         print(i)
    

#!4️⃣ Ask for a number and print whether it is even or odd.

# num=int(input("enter the num"))

# if num%2==0:
#     print("even")
# else:
#     print("odd")

#!5️⃣ Ask for a number and print its square.
# num=int(input("enter the num"))

# square= num**2

# print(f"the square of {num} is: {square}" )

#!6️⃣ Ask for a string and count how many characters it has.

# st=input("enter string")

# print(len(st))

#!8Print all multiples of 3 between 1 and 30.

# for i in range(1,31):
#     if i%3==0:
#         print(i)

#!9️⃣ Ask the user for a name. Print each letter on a new line.
# nam=input("enter name")

# for i in nam:
#     print(i)

# nam = input("Enter name: ")

# for i in range(len(nam)):
#     print(f"{i+1}: {nam[i]}")

#!🔟 Ask for a number and print the table up to 20.

num=int(input("enter num"))

for i in range(1,21):
    mul= num*i
    print(f"{num} * {i} = {mul} ")