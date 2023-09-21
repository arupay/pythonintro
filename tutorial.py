name ="Jane"
name2 = "Jake"
num = 12


#In python we have lists
names = ["Jake", "Olivia", "Linda", "Peter"] 
names2 = ["Jose", "Maria", "Anna"] 

#How can we work with lists



#Prints from starting index to ending index (ENDING INDEX NOT INCLUDED)
print(names[0:3]) 


#Can concatenate with + sign. (Overloaded?)
# prints ['Jake', 'Olivia', 'Linda', 'Peter', 'Jose', 'Maria', 'Anna']
namesCombined = names + names2
print(namesCombined)


# can combine sliced versions, no first param defaults to zero. 
#['Jake', 'Jose']
namesCombined2 = names[:1] + names2[:1]
print(namesCombined2)

#can also set negative numbers (first param is first number, last param is limit FROM end)
#['Jake', 'Olivia', 'Linda']
print(names[0:-1])

#Multidimensional arrays
population1 = [["Chicago", 2.9], ["LA", 4.5], ["NYC", 8.1]]
population2 = [["Houston", 2.8], ["Miami", 0.5], ["Dallas", 1.2]]

#Can also slice in multidimensional arrays, no second param means to end. 
#prints [['LA', 4.5], ['NYC', 8.1], ['Miami', 0.5], ['Dallas', 1.2]]
combined_population = population1[1:] + population2[1:]
print(combined_population)

age = 51
if age > 50:
    print("You should not be asking this")
elif age > 21:
    print("You are allowed!")
else:
    print("Not allowed to drink")

#Note colons instead of brackets, note indentations are STRICT, note elif = else if 

age2=50
#if checking for multipel conditions we use keyword "and" (&&) 
#if checking for || we use keyword "or"

if age2 > 49 and age2 < 51:
    print("Age is 50!")

#loops in python s

num_list = [5,6,7,8,9,10]

#to loop through a numerical range, in this exmaple starts at 0 and ends at 5
for i in range(0,5):
    print(i)

#declared city as for each var in population1 list
for city in population1:
    print(city)

#objects (JSON format) in python
person = {"name": "Linda", "age" :45} 
#access entire obj
print(person)
#access value of key age  , CANNOT dot notation direct access (i.e. person.age)
print (person["name"])
#values that dont exist will result in errors

#tuples .  Cannot delete from tuples, but they otherwise function like lists.
water = ("clear", "high ph")

#deconstructing 

celebs = ["Gaga", "Katy", "Britney","Bey"]
a,b,c,d = celebs
print(a,b,c,d)
#Gaga Katy Britney
#If unpacking like above you must unpack ALL THE ELEMENTS, otherwise use asterisk

j,*k = celebs
print("Here J:", j,"K:", k)
#Here J: Gaga K: Katy Britney, Bey

#asteriks is all remaining characters unless specified such as below:
l, *m, n = celebs;
print("Here l:", l,"m:", m, "n:",n)
#Here l: Gaga m: ['Katy', 'Britney'] n: Bey

#you can also reassign variables in lists

sports = ["soccer", "football", "basket", "golf"]
sports[1:3]=["cricket", "dance" ]
print(sports)
#['soccer', 'cricket', 'dance', 'golf']

#we can also insert more than one variable in a single index, the remaining array will remain unchanged
sports[1:2]=["gymastics", "track", "bike"]
print(sports)
#1:2 is only one spot, remember the second value is up to but NOT including
#['soccer', 'gymastics', 'track', 'bike', 'dance', 'golf'] NEW LIST SIZE 5!!


#we can also "map", but instead we use GLOBAL map functions with a LAMBDA callback

sports_on_ice = list(map(lambda name : name + " on ice", sports))
print(sports_on_ice)
#['soccer on ice', 'gymastics on ice', 'track on ice', 'dance on ice', 'golf on ice']

#lets now try filter

#lets filter out any sports that are dance 
#see now name is a string, and we are checking if the string ENDS (name[-1]) with the letter e
#returns all sports that end with "e"
#['bike', 'dance']
sports_that_end_with_e = list(filter(lambda name : name[-1]=="e", sports))
print(sports_that_end_with_e)


#using list comprehension to map
#['soccer on water', 'gymastics on water', 'track on water', 'bike on water', 'dance on water', 'golf on water']
lc_sports_on_water = [name + " on water" for name in sports]
print(lc_sports_on_water)

#list comprehension to filter
#['bike', 'dance']
lc_filter_sports = [name for name in sports if name[-1] =="e"]
print(lc_filter_sports)

#Core Data Types

#INT, FLOAT, STRING, BOOL
#INT is any number without a decimal
#FLOAT any number with a decimal even, if its 30.0
#STRING is any surrounded by single or double quotes, sequence of chars or nums
#BOOL is a true or false

#PRINTING
#print(item to print)
#BY DEFAULT PRINT , as separate statements will print ona new line.


#Getting user input (think cin (c++)) . You can get multiple user inputs

# user_name = input("Name: ")

# user_age = input("Age: ")

# print("Your name is", user_name, "and you are", user_age, "years old")

#Arithmetic Operators

x1= 9
y1= 3
result = x1+ y1
print(result)
#12

#We can also add integers and floats
#9 + 3.5  = 12.5


word1="hello"
# weird_result = x1 + word1
# print(weird_result)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'


#EXPONENTS
print(x1 ** y1) 
#9 to the third power

#MODULO, is still % , same function as JS
#Order of operations can be still be used with brackets 
#BEDMAS (Brackets, exponents, division, multiplication, modulo, addition, subtraction)

#int() in python converts a stirng to a num variable
#below ill print 5 if the input is 10

# num = input('Number: ')
# print(int(num) -5)

# #float() will conver tto decimal point value

# print(float(num) -5)
#prints 5.0

#type() will print the class type of the variable

#METHODS ON STRINGS

hello = 'hello'.upper()
print(hello)
#prints HELLO

hello_lower = 'HELLO'.lower()
print(hello_lower)
#prints hello

#count will count the occurrences of a substring in a string

print(hello.count('ll')) #0
print(hello.count('LL')) #1

#we can repeat strings by multiplying string with number, string MUST be on left side

dive = 'dive'
three = 3

print(dive * 3)
#prints divedivedive


#we can compare strings with > or < as well
#is a > Z ? This is because of ASCII code, we can access ORDINAL values 

#below will print TRUE lower case ASCII are higher on chart the uppercase ASCII
print('a'>'A')

#to get ascii value we can use ORD
#this will print 97
print(ord('a')) 

#not keyword
#Below will prin TRUE
print(not False)


# condition_name = input('Name: ')
# if condition_name == 'Tony':
#     print("You are great", condition_name)
# elif condition_name == 'Joe':
#     print('Oh hey', condition_name)
# else:
#     print("You are not tony")


#LIST FUNCTIONS

three_items =[1,2,3]
print(len(three_items))
#prints 3

#append (ADD SINGLE ITEM)
three_items.append(4)
print(three_items)

#cannot save append to new variable, IT DOES NOT RETURN ANYTHING, it MODIFIES EXISTING LIST

three_items.extend([5,6,7,8])
print(three_items)
#[1, 2, 3, 4, 5, 6, 7, 8]

extended = three_items.extend([5,6,7,8])
print(extended)
#NONE --- CANNOT SAVE EXTEND TO VARIABLE IT RETURNS NONE, IT MODIFIES EXISTING LIST

#other methods like by default remove last elmeent pop(), we can also pop an index by giving pop a value 

#TUPLES ARE IMMUTABLE

test_tuple = (0,0,2,2)
print(test_tuple)
#(0, 0, 2, 2)

# x[0] = 5
#ERROR!!!


#FOR LOOPS
#FOR RANGE LOOP PRINTS FROM 0 TO END , it creates a collection of numbers based on the input
#the input is the start, stop, step. 
#if we only have one number, it is the STOP (non-inclusive)
#if we have 2 inputs, we have START, STOP
#if we have 3, it is START STOP STEP

for i in range(5):
    print(i)
#0,1,2,3,4
print("------")


for i in range(5,0,-1):
    print(i)
#5,4,3,2,1
print("------")


for i in range(-5,-1):
    print(i)
#PRINTS -5,-4,-3,-2
print("------")


for i in [3,2,1]:
    print(i)
#prints 3,2,1


print("------")
#WHILE LOOP
j = 0
while j<3:
    print("j is", j)
    j+=1
# j is 0
# j is 1
# j is 2

cities = ["NYC", "CHICAGO", "BOSTON", "PHILI", "AUSITN", "SANFRAN"]
presidents = ["BUSH", "JFK", "OBAMA"]
clown = 'TRUMP'

sliced_one = cities[2:]
print(sliced_one)
#['BOSTON', 'PHILI', 'AUSITN', 'SANFRAN']

#REVERSING A LIST
sliced_reverse = cities[::-1]
print(sliced_reverse)
#['SANFRAN', 'AUSITN', 'PHILI', 'BOSTON', 'CHICAGO', 'NYC']

#SETS (O1)
# to create a set you must use set(), if you use {} you canont create an empty set and will instead
#be creating a dicitonary!

set_one = set()
print(type(set_one))
#prints <class 'set>

set_one.add(10)
print(set_one) 

#we can also do unions, intersections and symmetric differences in sets!!


#DICTIONARYS, hash tables or maps key value pairs

x = {'key': [1,2,3]}
print(x['key'])
#prints [1,2,3]

#adding keys
x['key2'] = 5
print(x)

print('key' in x)
#prints TRUE

print(x.values())
#usually when you do this you want to create a list of of it so print(list(x.values()))

#DELETING

del x['key']
print(x)
#{'key2': 5}

#ACCESS BOTH VALUES DECONSTRUCTED

for key, value in x.items():
    print(key, value)

#OR

for key in x:
    print(key, x[key])

#COMPREHENSIONS!!!
#ONE LINE INITIALIZATION OF A LIST

print("FUNCTIONS---------------")
 #functions
def func(x,y):
    return x*y

print(func(5,4)) 
#20

#we can also return tuples in functions

def func2(x,y):
    return x*y, x+y

print(func2(3,2))
#(6,5)

#destructuring function values
r1,r2 = func2(10,11)
print(r1,r2)
#110 21

def func3(x):
    def func2():
        print(x)
          
    return func2

print(func3(3)())
#will print 3 and None, none because there is no console value to func2() that is returned, 



def funcs_args(*args, **kwargs):
    pass

x = [4,5,1,3,4,9,10,33]

print(x) #PRINTS LIST
print(*x) #UNPACK ELEMENTS IN LIST


#In dictionaries we can unpack with **{'x':2, 'y':5}


#Exceptions (Throw)

# raise Exception('bad')

#TRY /Except/Block Python blocks

try: 
    x=7/0
except Exception as e:
    print(e)
#prints division by zero

try:
    y=10/0
except Exception as e:
    print(e)
finally:
    print('finally')

#Lambda is a ONELINE ANONYMOSU FUNCTION!
x11 = lambda x, y:  x+y
x22 = lambda x: x +1

print(x11(2,31))
#33 
print(x22(5))
#6

#f strings are template literals

eff_string = f'hi {1+2}'
print(eff_string)
#hi 3


#Ternary in python

is_raining = True
if is_raining:
    weather_message = "It is raining!"
else:
    weather_message = "It is not raining enjoy your day"
print(weather_message)

is_hailing = True

weather_message_two = "It is hailing" if is_hailing else "It is not hailing"
print(weather_message_two)