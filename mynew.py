#----Input----
# name= input('What is your name? ')
# Fav_color= input('What is your favorite color? ')
# print(name  + ' likes ' +  Fav_color)

# weight_lb= input('weight: ')
# weight_kg= float(weight_lb) * .45
# print(weight_kg)

#----String-----
# my= '''
# Hello sir,
# we are trying our best to learn python.
# thank you,sir
# on behalf of
# Group_1 thesis group
# '''
# print(my)
# print(my[17])
# print(my[-17])
# print(my[0:17])

# name='jennifer'
# print(name[1:-1])

# it_hot=True
# if it_hot:
#     print('drink water')
# else:
#     print('run')

# price=1000
# credit=True
# if credit:
#     down_payment=price*10
# else:
#     down_payment=price*0.1
# print(down_payment)

# -------- Weight Calculation---------
# weight= input('Your weight: ')
# unit= input('(L)bs or (Kg)s: ')
# if unit == 'L':
#     w= (int(weight) * 0.45)
#     print(f"Your {w} kilos ")
# else:
#     w= (int(weight)/0.45)
#     print(f"Your {w} pounds ")

#----------Guessing Game--------
# sec_num = 19
# guess_count=0
# guess_limit=3
# while (guess_count < guess_limit):
#     guess= int(input('Guess your number: '))
#     guess_count+=1
#     if guess == sec_num:
#         print('Your Guess is Correct!')
#     else:
#         print('Your Guess is Incorrect!')

# ---------Car Game--------
# command=" "
# while command != quit:
#     command = input("Type your command: ").lower()
#     if command == "start":
#         print(" Car starts")
#     elif command == "stop":
#         print(" Car stops")
#     elif command == "help":
#         print("""
#         start - start the car
#         stop - stop the car
#         quit - quit the game
#
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Invalid command")
#         break

#----------Nested Loop------

# num= (5,2,5,2,2)
# for item in num:
#     print( '*' * item )
# or
# num= (5,2,5,2,2)
# for item in num:
#     output=' '
#     for count in range(item):
#         output+= '$'
#     print(output)

# num= (2,2,2,2,5)
# for item in num:
#     output=' '
#     for count in range(item):
#         output+= '$'
#     print(output)

#----Max Number-----
# num=[5,11,96,23,55,41]
# max =num[0]
# for item in num:
#     if item > max:
#         max = item
#
# print(max)

#---------Dictionaries--------
# phone= input('Enter phone number: ')
# digits={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
#     "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"eight",
#     "9":"nine",
#     "0":"zero",
# }
# output=" "
# for digit in phone:
#     output+= digits.get(digit) + " "
# print(output)


# --------Function------
# def hello():
#     print("hello world")
#
#
# hello()














