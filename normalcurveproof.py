from random import *

count = 0
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"
ten = "10"
eleven = "11"
twelve = "12"
thirteen = "13"
fourteen = "14"
fifteen = "15"
sixteen = "16"
seventeen = "17"
eighteen = "18"
nineteen = "19" 
twenty = "20"
twentyone = "21"
twentytwo = "22"
twentythree = "23"
twentyfour = "24"
twentyfive = "25"
twentysix = "26"
twentyseven = "27"
twentyeight = "28"
twentynine = "29"
thirty = "30"
while not count == 750:
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    die3 = randint(1, 6)
    die4 = randint(1, 6)
    die5 = randint(1, 6)
    sum = die1 + die2 + die3 + die4 + die5
    if sum == 5:
        five = five + "."
    elif sum == 6:
        six = six + "."
    elif sum == 7:
        seven = seven + "."
    elif sum == 8:
        eight = eight + "."
    elif sum == 9:
        nine = nine + "."
    elif sum == 10:
        ten = ten + "."
    elif sum == 11:
        eleven = eleven + "."
    elif sum == 12:
        twelve = twelve + "."
    elif sum == 13:
        thirteen = thirteen + "."
    elif sum == 14:
        fourteen = fourteen + "."
    elif sum == 15:
        fifteen = fifteen + "."
    elif sum == 16:
        sixteen = sixteen + "."
    elif sum == 17:
        seventeen = seventeen + "."
    elif sum == 18:
        eighteen = eighteen + "."
    elif sum == 19:
        nineteen = nineteen + "."
    elif sum == 20:
        twenty = twenty + "."
    elif sum == 21:
        twentyone = twentyone + "."
    elif sum == 22:
        twentytwo = twentytwo + "."
    elif sum == 23:
        twentythree = twentythree + "."
    elif sum == 24:
        twentyfour = twentyfour + "."
    elif sum == 25:
        twentyfive = twentyfive + "."
    elif sum == 26:
        twentysix = twentysix + "."
    elif sum == 27:
        twentyseven = twentyseven + "."
    elif sum == 28:
        twentyeight = twentyeight + "."
    elif sum == 29:
        twentynine = twentynine + "."
    elif sum == 30:
        thirty = thirty + "."
    count = count + 1
print(five)
print(six)
print(seven)
print(eight)
print(nine)
print(ten)
print(eleven)
print(twelve)
print(thirteen)
print(fourteen)
print(fifteen)
print(sixteen)
print(seventeen)
print(eighteen)
print(nineteen)
print(twenty)
print(twentyone)
print(twentytwo)
print(twentythree)
print(twentyfour)
print(twentyfive)
print(twentysix)
print(twentyseven)
print(twentyeight)
print(twentynine)
print(thirty)
