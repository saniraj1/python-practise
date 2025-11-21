# for loop 

# for i in range(5):
#     print(i)

# printing 1 to 10 using for loop
# for i in range(1,11):
#     print(i)

# while loop 

# i=1
# while i<=5:
#     print(i)
#     i +=1

# i=1
# while i<=5:
#     print(i)
#     i+= 1
# i=5
# while i>=1:
#     print(i)
#     i-= 1


# control statement
#  break 
# for i in range(10):
#     if i==9:
#         break
#     print(i)

# continue 
# for i in range(10):
#     if i==4:
#         continue
# #     print(i)
# # for i in range(11):
# #     if i==5:
# #         continue
# #     print(i)


# # nested loop

# for i in range(3):
#     for j in range(4):
#         print("*",end="")
#     print()


# practise 
# for i in range(3):
#     for j in range(3):
#         print(j+1,end="")
#     print()

# Print all even numbers from 1 to 20.

# for i in range (1,21):
#     if(i%2==0):
#         print(i)


# Ask user for a number and print its multiplication table (1 to 10). 
num=int(input("enter the number"))
for i in range (1,11):
    mul=num*i
    print(f"{num} * {i}= {mul} ")
