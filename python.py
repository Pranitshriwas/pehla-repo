'''
name =  "leo"
age = 23
price = 45.93

print(name)
print(type(name))


age_2 = age
print(age_2)
print(type(price))

a = True
b = None
print(type(a))
print(type(b))


#Add two numbers.
n1 = 34
n2 = 23
sum = n1+n2
print(sum)


#swapping of two numbers.
a = 34
b = 11
a,b = b,a
print("After Swapping")
print("a" , a)
print("b" , b)

 
x,y,z = 'lion', 'tiger', 'cat'
print(x)
print(y)
print(z)
'''
'''
#global variable:

x = 14

def number():
        x = 13
        print("print the number",  x)

number()
print("print the number",  x)

x = 5

def update():
    global x
    x = x + 1  # This will give an error!
    print(x)

update()

print(not False)
print(not True)


# even and odd number. 
a = int(input("enter the number as you wish : "))
if (a % 2 == 0):
      print("the number is even: ", a)
else:
      print("the number is odd:" , a)

# prime number :
def is_prime(n):
    if n <= 1:
        return False  # Not prime

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Not prime
    return True  # Prime

print(is_prime(34))
print(is_prime(2))

n = 23
print(int(n ** 0.5))

def prime_num(n):
    if n <= 1 :
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

print(prime_num(15))
print(prime_num(11))


# a = float(input("enter 1st num.:"  ))
# b = float(input("enter 2nd num.:"))
# print(a >= b)
# print("avg = ",(a+b)/2)
'''
'''
str = "long life cover"
# print(type(str))
# print(len(str))

# print(str[4:len(str)])

# different types of functions : 
print(str.count("l"))
print(str.endswith("ver"))
print(str.replace("l",'s'))
print(str.find("life"))
print(str.capitalize())

str1 = "this is the string. \nwe are creating in python"
print(str1)


# concatination : 
str2 = "today is " + "wednesday"
print(str2)


# indexing with negative slicing:
str3 = "i'm working in neosoft company."
print(len(str3))
print(str3[-28:]) ## Negative slicing work from left to right..


# Write a Python program that asks the user to enter a number.
# If the number is positive, print "The number is positive".
# If the number is zero, print "The number is zero".
# If the number is negative, print "The number is negative".

# n = int(input("user - please enter the number : "))

# if (n == 0):
#     print("the number is zero")
# elif(n > 0):
#     print("the number is positive")
# else:
#     print("the number is negative")
    

# Check Whether a Character is a Vowel or Consonant

word = input('user - please enter the character :')

# checking the input is alphabet or not: 
if word.isalpha() and len(word)==1:
    word = word.lower()

    if word in 'aeiou':
      print("it is vowel")   
    else:
      print("it is consonant")   

else:
   print("enter the valid character") 
'''

   # grade based on marks:

# mark  = int(input("enter the mark of the student :"))

# if mark >= 90:
#    print("grade A")
# elif mark >= 80 and mark < 90:
#    print("grade B")
# elif mark >= 70 and mark < 80:
#    print("grade C")
# else:
#    print("grade D")



# a = int(input("enter the 1st number : "))
# b = int(input("enter the 2nd number : "))
# c = int(input("enter the 3rd number : "))

# if a > b and a > c:
#     print("a is greater than b and c")
# elif b > a and b > c:
#     print("b is greater than a and c")
# else : 
#     print("c is greater than a and b")


## list and tupples in python:

# mark = [23,24,43]
# print(mark[1])

# a = ["leo",43.4,56]
# print(a)
# print(a.sort())
# b = [1,4,2,5]
# print(b.insert(2,3))
# b.pop(4)
# print(b)
# print(b.sort())
# print(b)
# print(b.sort(reverse=True))
# print(b)

# a = [1,0,5,0,30,0,0]
# print(a.count(0))
# print(a)

    # wrt the python to enter name of the 3fav. movie & store in the list.
'''
u1 = input("enter your favourite movie 1 : ") 
u2 = input("enter your favourite movie 2 : ") 
u3 = input("enter your favourite movie 3 : ") 

fav_movie = [u1, u2 , u3]
print(fav_movie)'''


    #  Dictionary and sets :
dict_ = {
    "name" : "pranit",
    "learning" : "coding",
    "age" : 23,
    "is_adult" : True
}

print(dict_)

dict_ ["surname"] = "shrivas"
print(dict_)

## nested dictionary

student = {
    'name' : "arvind",
    "subject" : {"phy" : 54 , "math" : 76 , "chem" : 74} 
}

print(student)

print(student ['name'])
print(student["subject"]["math"])

print(student.values())