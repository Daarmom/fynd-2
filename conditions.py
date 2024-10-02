# CLASS 4
# # condition statement
# a=3
# b=7
# if a==b:
#     print("A is equal to B")
# elif b>a:
#     print ("B is greater")
# else:
#     print("A is greater")

# marks = 77
# if marks>90:
#     print("You'll get a bike")
# elif marks> 70:
#     print("You'll get a cycle")
# elif marks> 50:
#     print("You'll get a pencil box")
# else:
#     print("NO GIFT!")

# if True:
#     print("Inside 1st if")
#     if True:
#         print("If inside if")
#     else:
#         print("Else inside if")
# else:
#     print("Inside 1st else condition")

# # Loops in python
# list1 = list(range(10))
# list2 = list(range(3, 10))

# for var1 in list2:
#     print("Hello World", var1)

# arr1 = ["Apple", "Banana", "Cherry", "Mango"]
# for i in arr1:
#     print(i)
# for var1 in range(len(arr1)):
#     print(var1, arr1[var1])

# count = 0
# for i in range(100):
#     if i%3 == 0:
#         print(i, " is Divisible by 3")
#         count += 1      
# print(count)

# i=1
# while i<10:
#     print("Hello", i)
#     i+=2
# print("Outside Loop")

# i=100
# while i>10:
#     print("Hello", i)
#     i-=5
# print("Outside Loop")

# i=20
# while i>0:
#     if i%2==0:
#         print(i, " is Divisible by 2")
#     i -= 1

# # multiple conditions
# if 4>3 and 8>3:
#     print("Both true")
# else:
#     print("false")

# if 4>6 or 8>3:
#     print("either is true")
# else:
#     print("false")

# i=0
# while i<10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i += 1

# for i in range(5):
#     for j in range(3):
#         print("*", end = " ")
#     print("")

# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print("*", end = " ")
#     print("")

# for i in range(5):
#     for j in range(i+1):
#         print("*", end = " ")
#     print("")

# for i in range(5):
#     for j in range(5):
#         if j>=i:
#             print("*", end = " ")
#     print("")

# for i in range(1,6):
#     for j in range(5-i+1):
#         print("*", end="")
#     print("")

# for i in range(1, 6):
#     for j in range(6-i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print("")

# for i in range(5):
#     for l in range(5-i):
#         print(" ", end=" ")
#     for l in range(i):
#         print("*", end=" ")
#     for r in range(i-1):
#         print("*", end=" ")
#     print("")

for i in range(5):
    if i==4:
        break
    print("Hello", i)
else:
    print("Loop ended")

# Step in list
x = list(range(2, 10, 2))
print(x)
x = list(range(10, -7, -2))
print(x)

help(range)
help(max)
help(print)
