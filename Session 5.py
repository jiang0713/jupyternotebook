import csv
import random

guesser_name = input('What is your full name?')
file_handle = open("C:/Users/jiang/Downloads/Python/Countries.csv")
reader = csv.DictReader(file_handle) # load the files into the reader
countries = list(reader) # convert the reader into a list
file_handle.close() # close the file

randomcountry = random.choice(countries) # choose a random country from the new list



guess = ""   
attempts = 0
unmatched = False   # initiate some variables

print(randomcountry) # cheat and see the randomly selected country

logg = open("C:/Users/jiang/Downloads/log.txt", "w") 

while guess != randomcountry['country'] and attempts < 10:
    guess = input('What country am I? ').casefold()
    attempts += 1
    print(guess)
    logg.writelines(str(guess) + '\n')
    if guess == randomcountry['country'].casefold():
        print('Well done! You have successfully indentified the country.')
        logg.writelines('Well done! You have successfully indentified the country.\n')
        break
    if attempts >= 10:
        print('You are fresh out of guesses.')
        logg.writelines('You are fresh out of guesses. \n')
        break
    for country in countries:
        if guess.casefold() == country['country'].casefold():
            if float(randomcountry['lat']) > float(country['lat']):
                print('I am located north of '+ guess)
                logg.writelines('I am located north of '+ str(guess) + '\n')
            else:
                print('I am located south of '+guess)
                logg.writelines('I am located south of '+ str(guess) + '\n')
            
            if float(randomcountry['long']) > float(country['long']):
                print('I am located east of ' + guess)
                logg.writelines('I am located east of ' + str(guess) + '\n')
            else:
                print('I am located west of ' + guess)
                logg.writelines('I am located west of ' +str(guess) + '\n')
logg.close()
