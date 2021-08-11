import csv
import random

file_handle = open("C:/Users/jiang/Downloads/Countries.csv")
reader = csv.DictReader(file_handle) # load the files into the reader
countries = list(reader) # convert the reader into a list

file_handle.close() # close the file

randomcountry = random.choice(countries) # choose a random country from the new list

guess = ""   
attempts = 0
unmatched = False   # initiate some variables

print(randomcountry) # cheat and see the randomly selected country

while guess != randomcountry['country'] and attempts < 10:
    guess = random.choice(countries)
    guess1 = guess['country']
    guess2 = guess1.casefold()
    attempts += 1
    print(guess2)
    if guess2 == randomcountry['country'].casefold():
        print('Well done! You have successfully indentified the country.')
        break
    if attempts >= 10:
        print('You are fresh out of guesses.')
        break
    for country in countries:

        if guess2.casefold() == country['country'].casefold():
            if randomcountry['lat'] > country['lat']:
                print('I am located north of '+ guess2)
            else:
                print('I am located south of '+guess2)
            
            if randomcountry['long'] > country['long']:
                print('I am located east of ' + guess2)
            else:
                print('I am located west of ' + guess2)