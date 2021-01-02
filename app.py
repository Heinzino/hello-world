DRY = "Don't repeat yourself!"

Quick tests using python interpreter cmd >python 3
float() int() str()
bool()
strings = "Plain text captured in quotation marks"
numbers = 50.132414
bulian__value = False
phrase = "string"
sting_index= 01234
print(phrase + "is cool")
print(phrase.upper())
print(len(phrase))
print(phrase{0}) #this shows a specific character in the string starting from 0 and counting onwards
print(phrase.index("s")) #called "passing a parameter", long word tells where it starts
print(phrase.replace("Plain", "Full"))
print(10 % 3) #modulist operator, 10 mod 3, shows remainder
print(str(my_num) + "my favourite number") #changes number to string, good w/ coupling w/ string
print(abs(my_num)) #absolute value
print(pow(3,2)) #put number and power you want to take the number to
print(max(4,6)) #tells which one is larger print(min
print(round)
#formatted strings
f'{first} + [{last}] is a coder]'
#/ divides w/ float || //divdes with int

from math import* #importing math functions
print(ceil()) #round number up no matter print(floor
print(sqrt())

name = input("Enter your name:") print("Hello" + name + "!")
result= float(num1) + int(num2) print(result) #basic calc, float includes dec int is integers
color = input("Enter a color:") print("Roses are " + color ) #madlibs game, extendable
kill  = ["Kevin", "Karen", "Mike", "Hawk"] #lists are storing variable print(kill[0]) to access index, negatives work backwards -1 is hawk -2 mike... go after specific [1:] 1:3
kill[1] = "Oscar" #changes element
kill.extend(list) #extends both list so you can print em all out
kill.append("name") kill.remove("Kevin") #adds an element to the end of a# list, removes element from list
friends.insert(1,"Kelly") friends.clear() #adds an element at a certain index | empty list
kill.pop() print(friends.index("Name")) #removes last element from the list #checks the index of a name
print(friends.count("Kelly")) #tells how many times an element appears on the list
friends.sort() #sorts list alphabetically  numbers in ascending order
friends.reverse() #lists from back to front/ used in conjuction w/ the .sort
friends2 = friends.copy()
print("Kelly" in friends2) #another way to check  for index
#tuples (), lists [], tuples are inutiable lists of tuples coordinates = [ (5,9), (6,7), (5,12)]
coordinates = (4,5) #inutiable tuples can't be changed or modified,

def sayhi(): #creating function, any code inside funciton needs to be indented. to run the function sayhi() outside function
    def sayhi(name): print("Hello " + name) sayhi("Mike") # you can give it a variable for it to function, these variables are called parameters can do more than one, age
return num*num*num #telss it to give a value back to whatvever the function called, can't put code after the return statement

if statements # specifying conditions if conditions are true do certain things if false we can do other things/check other conditions
    is_male = True
if is_male or is_tall:  #if it fits into either criteria | and means both have to be true in order to function
        print("You are a male")
elif is_male and not(is_tall): #means else if | not function negates what ever is in the brackets
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are a tall woman")
else:
    print("You are not a male") # if statement is executed when condition is true

#COMPARASIONS
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: #comparasion, >= is a comparasion operator how we want to compare the values
        return num1
    elif num2 >= num1 and num2>= num3: # == means two values are equal | != means not equal | > greater than | < less than| >= greater than or equal to | <= less than or equal to
        return num2
    else:
        return num3
print(max_num(3, 4, 5))

#BETTER CALC
num1 = float(input("Enter first number:"))
op= input("Enter operator:")
num2 = float(input("Enter second number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

    #DICTIONARY
monthConversions = { #key value pairs
     "Jan": "January",
    2: "February"
 } #NO INDENTS/ SPACES
print(monthConversions["Jan"]) #get also extracts from the dicitonary { are dictionary can go as long as you want
print(monthConversions.get("Luv", "Not a valid key")) #second message is what it gets defaulted to, if not just prints out none

number_converter = {
    "1" : "One ",
    "2" : "Two ",
    "3" : "Three ",
    "4" : "Four ",
}
phone = input("Phone:")
output = ""
for ch in phone:
    output += number_converter.get(ch, "!")
print(output)

message = input(">")
words = message.split(' ') #creates a space/element for every word and stores inside a list
# windows semicolon
emoji = {
    ":)" : "😀",
    ":(" : "😔"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)


WHILE LOOPs
#while structure that let's us loop through and  exceute a block of code multiple times
#condition is while condition or loop guard, keep looping as long as the condition is true
# i += 1 adding one to the i
#after every execution of the loop python comes back up and checks it again
i = 1
while i<= 10:
    print(i)
    i += 1

print("Done with loop")

Guessing game = true

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit: #still have guesses left
        print("Animal") #hint
        guess = input("Enter guess:")
        guess_count += 1
        break
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose")
else:
    print("You win!")

    menu = ""
    started = False

    while True:
        menu = input(">").lower()
        if menu == "help":
            print('''start - to start the car
    stop - to stop the car
    quit- to exit the game''')
        elif menu == "start":
            if started:
                print("Car is already started")
            else:
                started = True
                print("Car started...ready to go!")
        elif menu == "stop":
            if not started:
                print("Car is already stopped dummy")
            else:
                started = False
                print("Car stopped.")
        elif menu == "quit":
            break
        else:
            print("Sorry, I don't understand that!")

FOR LOOPS

for letter in "Find your dreams come true":#for every letter inside " " i want to ....
    print(letter)  #variable changes for every loop

friends = ["Jim", "Karen", "Steven"]
len(friends) #how much elements inside
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friend[index])

numbers = [5,2,44,13,451]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
#removing duplicates
A = [5,3,1,2,1,4]
uniques = []
for number in A:
    if A not in uniques:
        uniques.append(A)
print(uniques)

numbers = [5,2,5,2,2]

for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

for index in range(3, 10, 2 ) #prints b/t 3 and not including 10 goes up by 2
    print(index)
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

prices = [10, 20, 30]
Sum = 0
for item in prices:
    Sum += item

print(Sum)


Exponenet Funciton
#normally is 2**3 for 2^3
def raise_to_power(base_num, pow_num):
    result= 1
    for index in range(pow_num): #loops through power number of times
        result = result * base_num
    return result
print(raise_to_power(56, 30))

#2d lists and nested loops (for inside for)

for x in range(4): #so runs x to 4
    for y in range(3): #keeps going 0,1 0,2 etc. till it compeltes then goes back to the other line and finishes x
        for z in range (2):
            print(f'({x}, {y}, {z})')
            
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][1]) #row number (horizantal) then column number (vertical)
#don't forget commas after every element and list!

for row in number_grid:
    for col in row: #each element inside the array inside the grid
        print(col)

#Tuples are unchangable lists w/ () over []

coordinates = (1,2,3)
#stores x as index 0 of tuple, y as index 1, and z as index 3
x,y,z = coordinates #can use in lists as well
print(x * y * z)
#fucntion is just an organized code that you can call repeadetly
#parameteres in side functions to recieve certain info, arguements are the actual piecess of info supplied
greet("Smith", first_name = "John") #keyword arguement position changes to fit the keyword, usually numberical to improve readability, use keyword after positional arguement
#smith is positonal arguement

#functions shouldn't worry about recieveing input and outputing them eg. input(">) and print(output) just focus on the code and FUNCTION of the code
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:")))



def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ":)" : "😀",
        ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))


'''
 This is another way of making comments 
 on multiple lines
 Comment comment out code
'''

try:
    number =  int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err: #good practice to catch specific errors
    print(err) #prints out specific error "division by zero"
except ValueError:
    print("Invalid input ")

'''
 "r" is just reading not modifying
 "w" write new info
 "a" append info, add new info
 "r+" read and write
'''

employee_file = open("employees.txt", "r") #name of file and mode
    for employee in employee_file.readlines():
        print(employee) #prints all employees
    print(employee_file.readable()) #bullian value
    print(employee_file.read())#all info in file
    print(employee_file.readline())  #first line
    print(employee_file.readline()) #then moves to second
    print(employee_file.readlines()) #puts them all in a list
    print(employee_file.readlines()[1]) #prints out 1
employee_file.close() #good practice to close file

employee_file = open("employees.txt", "a")

employee_file.write("\nKelly-Customer Service")  #appends in a new line

employee_file.close()

employee_file = open("index.html", "w") #w overwrite everything on the existing file, can create a new file

employee_file.write("<p>This is Html</p>")

employee_file.close()

import name_of_file #able to use all the functions
#pip uninstall module name
print(name_of_file.(function)) #normall in libs folder (external libraries), if 3rd party download in lib/site packages



#capatalize variables on functions, EmailClient.
class Point:

    def draw(self):
        print("draw")
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

class Student:

    def __init__(self, name, major, gpa, is_on_probation): #parameters after self. called a constructor
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    #name of student major would be the major we passed in etc.. Self is referring to the actual object then it store the
    #attributes assigned to it

    # Classes create your own date type
    # class is the template, object is the actual student
    # file          #class
    from student import Student

    student1 = Student("Jim", "Business", 3.1, False)
    student1 = Student("Joey", "Acting", 0.1, False)
    print(student1.name)

lass Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John")
print(john.name)
john.talk()

#MULTIPLE CHOICE TEST

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Greed\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow \n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)

from student import Student

student1 = Student("Joey", "Acting", 0.5)
student2 = Student("Ross", "Paleontology", 3.8)


def on_honor_roll(self):
    if self.gpa >= 3.5:
        return True
    else:
        return False

print(student1.on_honor_roll())

from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.makes_special()

class Chef:

    def makes_steak(self):
        print("The chef makes steak!")
    def make_salad(self):
        print("The chef makes a salad!")
    def makes_special(self):
        print("The chef makes empanadas!")

from Chef import Chef
#inside ChineseChef they will be able to use all the function of Chef, over ride inheritance by writing another function
class ChineseChef(Chef): #paranthesis then mother class inherits functions, if you just want to inherit the functions put pass after so puthon ignores
    def makes_special(self):
        print("The chef makes ginger beef")
    def make_fried_rice(self):
        print("The chef made fried rice!")

class Cook(Chef):
    pass

from utils import find_max

numbers = [314,35312,53243,45,43]

max = find_max(numbers)
print(max)

#Contrl + slash to make a line a comment

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

# when importing from packages do from package name import python file or from packagename.python file import function

import random

members = ['John', "Mary", 'Bob', 'Mosh']
print(random.choice(members))

for i in range(3):
    print(random.randint(10, 20))

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

from pathlib import Path
#Absolute path c:/program file/ microsoft
# Relative path
            #directory
path = Path(#put in directory "hello")
print(path.mkdir())
for file in path.glob('*'): #checks all files *, and .py to specify
    print(file)


