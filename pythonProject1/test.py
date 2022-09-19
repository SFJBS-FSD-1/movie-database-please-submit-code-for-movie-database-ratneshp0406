#print('hello world')
#number1 = int(input("Enternumber1:"))
#number2 = int(input("Enternumber2:"))
#print('The sum', (number2 + number1))

#num = int(input("Enter your age "))
#if num>18:
#    print("Eligible for driving liscence")
#elif num<18:
#    print("not eligible for driving liscnece")
#else:
#    print("You are 18 yr old")

#user enter year and write program to tell is it leap year
#year = int(input("Enter year"))
#if year % 4 != 0:
#    print("Not a leap year")
#else:
#    if year % 100 != 0:
#        print("year is leap year")
#    else:
#        if year % 400 != 0:
#            print("not leap year")
#        else:
#            print("year is leap year")

#looping
#count = 0
#while True:
#    count = count + 1
#    print("Hello world")
 #   if count == 5:
 #       break

#count = 0
#while True:
#     count = count +1
#     print(count,end=" ")
#     if count>=10:
#         break

#user will enter a number and you need to print it's multiplcation table

#num = int(input("Enter a number"))
#count = 0
#while True:
#    print(num*count)
#    count = count + 1
#    if count>10:
#        break

#num = int(input("Enter number"))
#for i in range(1,11):
#    print(num*i, end=" ")

# 1,4,7,10,13....20 terms
#count = 1
#for i in range(20):
#    print(count, end=" ")
#    count= count+3

#find sum of 1st 100 natural number

#count = 0
#for i in range(1,101):
#    count = count + i
#    print(count, end=" ")

#user will enter a number and u need to identifiy if it's prime or composite

#num = int(input("Enter a number"))
#for i in range(2, num):
#        if (num%i == 0):
#            print("num is a composite num")
#            break
#else:
#    print("Number is prime")


#num = int(input("Enter your number"))
#count = 0
#for i in range(1, num+1):
#    if (num%i == 0):
#        count = count + 1
#if count == 2:
#    print("prime")
#elif count>2:
#    print("composite")
#else:
#    print("neither of them")


#def add(a,b):
#    c=a+b
#    return c

#result=add(2,5)
#print((result))




#def sum(a,*args):
#    z=(a*b)+c
#    return z
#print(sum(b=1,c=10,a=9))


#Write a program to find all factors of a number

#num = int(input("Enter the number"))
#for i in range(1,num+1):
#    if num%i == 0:
#        print(i)

# Challenge 2 : Using while loop Write a program to find  factorial 10

# n = int(input("Enter the number"))
# num = 1
# while n > 1:
#     num = num*n
#     n = n -1
# print(num)

# Challenge 3 : print all prime numbers between 1 and 100

# for i in range(2,101):
#     for j in range(3, i):
#         if i%j == 0:
#             break
#     else:
#         print(i)
# Challenge 4 : Write a function that can calculate HCF of 2 numbers
# Challenge 5 : write a function that can find total digits in a natural number

#write code to find largest element in list
# mylist = [12,90,77,23,8]
#
# for i in mylist:
# max = mylist[0]
# for i in mylist:
#     if mylist[i]>max:
#         max =
#     max =

# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)
#
# list = [1,2,3,[4,5,6]]
# print(list[3])


# list = [1,9,99,30,22,10,85]
# even = []
# odd = []
# for i in list:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# list = [1,9,99,85,85,30,22,10]
# list2 = [85, 44]
# count = 0
# for i in list:
#     for j in list2:
#         if i == j:
#             count = count + 1
#
# print(count)

# list1=["India","Lanka","Nepal"]
# list2=["Delhi","Colombo","Kathmandu"]
# mydict = {}
# for key in list1:
#     for value in list2:
#         mydict[key] = value
# print(dict)

# x= lambda a : a + 10
# print(x(5))
#
# y = lambda  a,b : a*b
# print(y(3,4))

# z = lambda  a : a*2
# print(z(3))

# animals = ['dog', 'cat', 'parrot', 'rabbit','rhinoceros']
# result = map(lambda x : len(x), animals)
# print(list(result))
# from functools import  reduce
# seq = [2,4,6,3,5]
# def greater(num1,num2):
#     if num1>num2:
#         return  num1
#     else:
#         return num2
#
# result = (reduce(greater,seq))
# print(result)
list = [12,3,4,5,5]
def findinmax(list):
    max = list[0]
    for i in list:
        if i>max:
            max=i
    return  max
print(findinmax(list))

