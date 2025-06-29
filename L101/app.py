### https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=7587s
# print("Lets Try")
# print('U' + 'k' * 2 + 'e')
# price = 10
# rating = 0.9
# print(price * rating)

# name = 'John'
# age=20
# new_patient = True

# Name = input("What is Patient Name - ")
# print("Hi "+Name)
# Age = input("what is Age of " + Name + " - ")
# print (Name+" age is "+ Age)
# Birth_Year = input('Birth Year of '+Name+' - ')
# print(Birth_Year)
# calc_age = (2025-int(Birth_Year))
# print('calculated age - '+ str(calc_age))

### print statements with ", ' ###
# course = "Python's course for Beginners"
# print(course)
# course = 'Python course for "Beginners"'
# print(course)
# course = '''Python's course for "Beginners"'''
# print(course)

### Strings index ###
# course = '''Python course for Beginners'''
# print(course[1:-1])
# another=course[:]
# print(another)

### Formatted Strings ###
# f_nm = 'John'
# l_nm = 'Smith'
# msg = f'{f_nm} [{l_nm}] is a coder'
# print(msg)

### String Methods ###
# course = '''Python course for Beginners
# covers fundamentals.'''
# print(course)
# # print(len(course))
# # print(course.lower())
# # print(course.find('B'))
# # print(course.replace('Beginners','the Beginners'))
# # print(course.replace('P','X'))
# # print(course.replace('Begi','Sin'))
# # print('Python' in course)
# print(course.title())

### Arithmetic Operations
# print(10/3)
# print(10//3)
# print(20%3)
# print(10*3)
# print(10**3)
# x=10
# x = x + 3
# print(x)
# x=10
# x+= 3
# print(x)
# x=10
# x-= 3
# print(x)

### Operator Precedence
### Exponentiation, Multiplication or division, add/sub
# x = 10 + 3 * 2
# print(x)
# x = 10 + 3 * 2 **3
# print(x)
# x = (2+3) * 10-3
# print(x)
# x = 2+3 * 10-3
# print(x)

### Math Functions
# x=1.5
# print(round(x))
# print(abs(-1.499))

# import math as m
# ceil = m.ceil(2.9)
# print(ceil)
# floor = m.floor(2.9)
# print(floor )


### If Syntax ###
# price=1000000
# credit=True
# print('Home Price = ' + str(price))
# if credit:
#      print('Good Credit. Down Payment = 10%')
#      percent_value= price * 10/100
#      print(f'Down Payment required = ${percent_value}')
# else:
#     print('Bad Credit. Down Payment = 20%')
#     percent_value = price * 20 / 100
#     print(f'Down Payment required = ${percent_value}' )
#     print('End')

 ### Logical Operators - AND OR NOT
# has_good_credit = True
# has_high_income = False
# has_criminal_record = False
# if (has_good_credit or has_high_income) and not has_criminal_record :
#      print("Eligible")
# else :
#      print("not eligible")

### Comparison operators > , <, == , !=
# name = input("Enter the name - ")
# length = len(name)
# print('Length = '+ str(length))
# if length < 3:
#     print('Length of Name should be atlease 3 chars')
# elif length > 50:
#     print('Length of name cannot be more than 50 chars')
# else:
#     print('Name looks good')

### Weight comparison
# Weight = input('Enter Weight : ')
# Units = input('(L)bs or (K)g : ')
# if Units.upper() == 'L':
#     conv = int(Weight) * 0.45
#     print(f'You are {conv} Kgs')
# elif Units.upper() == 'K':
#     conv = int(Weight)*2.20462
#     print(f'You are {conv} Lbs')
# else:
#     print('Enter either L or K')

### WHILE Loops
## Guess game
# sec_num = 9
# guess_cnt = 0
# guess_limit = 3
# while guess_cnt < guess_limit :
#     num = int(input('Guess the Number : '))
#     guess_cnt = guess_cnt + 1
#     if num == sec_num:
#         print('You win!!')
#         break
# else:
#     print('You Failed!!')
# print('Game Over !!')

# ## CAR game
# val=''
# started = False
# while True:
#     val = input('> ').upper()
#     if val == 'HELP':
#         print('''
# start  - to start
# stop - to stop
# quit - to exit
#     ''')
#     elif val == 'START':
#         if started:
#             print('Car already started!!')
#         else:
#             started = True
#             print('Car started--- Ready to go!')
#     elif val == 'STOP':
#         if not started:
#             print('Car already stopped!!')
#         else:
#             started = False
#             print('Car stopped!')
#     elif val == 'QUIT':
#         print('End!!')
#         break
#     else:
#         print('I dont understand that...')
#     prev_val = val

## Nested Loops
# numbers = [2,2,2,2,8]
# for x_cnt in numbers:
#     output = ''
#     for count in range(0,x_cnt):
#         output += 'x'
#     print(output)

## LIST find largest num in list
# num_list = [1,9,2,7,4]
# max = num_list[0]
# for i in num_list:
#     if i > max:
#         max = i
# print(max)


#### 2D list
# matrix = [
#     [1,2,3],
#     [10,20,30]
# ]
# print(matrix[0][2])
# matrix[0][2]=100
# print(matrix)

# for row in matrix:
#     print(row)
#     for val in row:
#         print(val)

### LIST METHODS
# num_list = [1,9,2,7,4]
# print(num_list)
# num_list.insert(0,3)
# print(num_list)
# num_list.remove(9)
# print(num_list)
# num_list.pop(2)
# print(num_list)
# num_list.pop()
# print(num_list)
# num_list.clear()
# print(num_list)

## Remove duplicates in a list
# n_list = [1,3,2,2,6,7,7,4]
# print(n_list)
# print(n_list.__len__())
# n_list.sort()
# print(n_list)
# unique = []
# for x in n_list:
#     if x not in unique:
#         unique.append(x)
# n_list = unique.copy()
# print(n_list)

####### TUPLES
# Tuples is a list which cannot be modified
# n_tup = (1,1,12,3,4,5)
# print(n_tup.count(1))
# n_tup[1] = 10 ## NOT POSSIBLE to change value
# print(n_tup) # error

## UNPACKING
# n_tup = (1,3,12)
# x,y,z = n_tup
# print(z)
# n_list = [1,3,2] # same applies for list
# x,y,z = n_list
# print(z)

#### DICTIONARIES
# Print phone number in words
# phone = input('Enter Phone Number - ')
# print(phone)
# numbers = {
#     '1':'One',
#     '2':'Two',
#     '3':'Three'
# }
# output = ''
# for char in phone:
#     output += numbers.get(char,'!') + ' '
# print(output)

# Emoji
# import emoji
# msg = input('>')
# words = msg.split(' ')
# print(words)
# emojis = {
#     ":)" : emoji.emojize(":grinning_face:"),
#     ":(" : emoji.emojize(":slightly_frowning_face:")
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

### FUNCTIONS
# import emoji
# def print_emoji(message):
#     words = message.split(' ')
#     emojis = {
#         ":)" : emoji.emojize(":grinning_face:"),
#         ":(" : emoji.emojize(":slightly_frowning_face:")
#         }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# input = input('>')
# print(print_emoji(input))

#### EXCEPTIONS  try, except
# try:
#     num = int(input('Enter a number - '))
#     print(num)
#     print(10/num)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Invalid Input')
# else:
#     print('No Exception')
# finally:
#     print('This will run no matter what')

#### CLASS
# class Point:
#     def move(self):
#         print('Move')
#
#
#     def draw(self):
#         print('Draw')
#
# point1 = Point()
# point1.draw()
# point1.move()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# print(point1.y)
#
# point2 = Point()
# point2.x = 30
# point2.draw()
# print(point2.x)

#### CONSTRUCTOR
# class Point:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def draw(self):
#         print('Draw')
#
# point1 = Point(10,20)
# print(point1.a)
# point1.a=300
# print(point1.a)
# point1.draw()

# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def talk(self):
#         print(f"{self.name} can talk")
#
# per = Person("John")
# per.talk()
#
# per2 = Person("Jane")
# per2.talk()

### INHERITANCE
# class Office:
#     def chair(self):
#         print('Chair')
#
# class Work(Office):
#     def table(self):
#         print('Table')
#
# emp1 = Work()
# emp1.chair()
# emp1.table()

### MODULES
# import utils
# nlist = [1,2,3,4,5]
# max_n = utils.find_max(nlist)
# print(max_n)

### PACKAGES
# from ecommerca import shipping
# shipping.calc_shipping()
# from ecommerca.shipping import calc_shipping
# calc_shipping()

