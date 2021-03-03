#!/usr/bin/env python
# coding: utf-8

# # Question1:
# 1) Inputs from the user.
# 
# 2) str1+str2concatenating and checking the equality with str3 in first if.
# 
# 3) str2+str1concatenating and checking the equality with str3 in second elif.
# 
# 4) else for every other case strings not equal.
# 
# 5) prints String equal when 1st two condition are true otherwise false.

# In[1]:


# Inputs from the user
str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
str3 = input('Enter the third string: ')

# nested if condition to check whether strings are equivalent or not.  
if str3 == str1+str2:
    print('Strings are equal')
elif str3 == str2+str1:
    print('Strings are equal')
else:
    print('Strings are not equal')


# Question 2:
# 1) initialize empty array to store input
# 
# 2) read input from user
# 
# 3) validate input 
# 
# 4) calculate average sum/number of observation
# 
# 5) calculate min number by loping over the array and comparing
# 
# 6) same as step 5 but check for max number
# 
# 7) calculate median by checking if even no. or odd no. then accordingly calculate median.
# 

# In[33]:


import math
from statistics import median
# empty array
arr = []
# Prompting user to select number from the given integers
num_of_int = int(input("Choose a integer between '3' or '4': "))
# To check if user has inputted correct integer only
while num_of_int!=3 and num_of_int!=4:
    num_of_int = int(input("Please! Choose a integer between '3' or '4': "))

#append input number to array according to the num_of_int value 
if num_of_int == 3:
    arr.append(int(input("Enter the 1st integer value: ")))
    arr.append(int(input("Enter the 2nd integer value: ")))
    arr.append(int(input("Enter the 3rd integer value: ")))
else:
    arr.append(int(input("Enter the 1st integer value: ")))
    arr.append(int(input("Enter the 2nd integer value: ")))
    arr.append(int(input("Enter the 3rd integer value: ")))
    arr.append(int(input("Enter the 4th integer value: ")))

#  Initialising the fields with 0 and None
avg_of_nums = 0
max_of_nums = None
min_of_nums = None
median_of_nums = 0
add = 0
#  for looping into array to add the elements and take average of them
for i in range(len(arr)):
    add += arr[i]
avg_of_nums = add/len(arr)
# for looping into array to find minimum from them
for i in arr:
    if min_of_nums==None:
        min_of_nums = i
    elif min_of_nums>i:
        min_of_nums = i
# for looping into array to find maximum from them
for i in arr:
    if max_of_nums==None:
        max_of_nums = i
    elif max_of_nums<i:
        max_of_nums = i
if num_of_int == 3:
    print("The average of {0},{1} and {2}:".format(*arr),avg_of_nums)
    print("The minimum of three numbers:", min_of_nums)
    print("The maximum of three numbers:".format(*arr),max_of_nums)
else:
    print("The average of {0},{1},{2} and {3}:".format(*arr),avg_of_nums)
    print("The minimum of four numbers:", min_of_nums)
    print("The maximum of four numbers:", max_of_nums)
# Sorting and finding median of the arr
arr.sort()
if num_of_int%2 == 0:
    median_1 = arr[num_of_int//2]
    median_2 = arr[num_of_int//2-1]
    median_of_nums = (median_1+median_2)/2
    print("The median of four numbers:", median_of_nums)
else:
    median_of_nums = arr[num_of_int//2]
    print("The median of three numbers:", median_of_nums)


# Question 3:
# 
# 1) input from the user
# 
# 2) try except block to handle number negative and non integer number.
# 
# 3) check input num is greater than 1 in try block
# 
# 4) loop over to find factor of given number and if factor found then composite otherwise prime
# 
# 5) and if number is 0 or 1 then print not prime and composite
# 
# 

# In[57]:


# input from the user
num = input("Enter a positive integer: ")
# try except block for error handling
try:
    num = int(num)
#     prime numbers are greater than 1
    if num>1:
#         looping over to find factors
        for i in range(2,num):
            if(num%i) == 0:
                print('It is a composite number')
                break
        else:
            print('It is prime number')
    elif num == 0 or num == 1:
        print("Neither prime nor composite")
#  for invalid input
except:
    print("Error: You did not enter a positive integer")
    


# Question 4:
# 
# 1) two functions defined 
# 
# 2) first func for calculating the simple interest using formula
# 
# 3) second func for handling inputs and calling the function by passing the inputs
# 
# 4) input from user in float and int respective of the field
# 
# 5) try catch block to handle errors

# In[1]:


# func for simpleInterest formula: priciple*interest*year/100
def simpleInterest(principle,interest,year):
    return ((principle*interest*year)/100)


# In[6]:


# function calling main function
def main():
#    for input and error checking
    try:
        
        principle_amount = float(input("Enter the principle amount: "))
        while principle_amount<0:
            principle_amount = float(input("Enter the principle amount correcntly: "))
        interest_rate = float(input("Enter the interest rate between (0-100): "))
        while interest_rate<0 or interest_rate>100:
            interest_rate = float(input("Enter the interest rate between (0-100): "))
        year = int(input("Enter the Year: "))
        while year<0:
            year = int(input("Enter the Year: "))
        result = simpleInterest(principle_amount,interest_rate,year)
        print("Simple Interest amount is:" , result)
    except:
        print("Error: Invalid input")


# In[7]:


main()


# Question 5:
# 
# 1) Two function defined 
# 
# 2) checkrect func takes in the input and computes wheter the points lie in the coordinate or not
# 
# 3) main func handles the calling and further continuing the recheck based on the user inputs
# 
# 4) return result as boolean value

# In[73]:


def checkRectangle():
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        xCheck = float(input("Enter x: "))
        yCheck = float(input("Enter y: "))

        return x1< xCheck < x2 and y1<yCheck<y2  #if any of x or y cordinate doest lie in range [x1,x2],[y1,y2] then it falls outside rectange
    except:
        print('Error: string found')
        


# In[76]:


def main():
    print(checkRectangle())
    x = 'Y'
    while x == 'Y' or x == 'y':
        x = input("Do you want to continue? Y on N: ")
        if x == 'Y' or x == 'y':
            print(rec())
    print("Goodbye!")


# In[77]:


main()


# In[ ]:




