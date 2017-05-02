#Script to give random Jeopardy! question, record answer, and keep running money total
#George Owen, 2017-05-01

#THIS IS ONLY COMPATIBLE WITH PYTHON 3.*+

import csv, random, os, codecs, sys, configparser

CONFIG_LOCATION = 'config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_LOCATION)

#Initializes play variable to 1 (1 = play a rounds, 0 = exit) 
play=1
tot = int(config['Save']['RunningTotal'])

#Gets number of lines/questions in CSV
with open(config['Options']['CSVPath'], newline='',errors='ignore') as csvfile:
    #Creates reader object for csv file and makes rows as list of arrays
    reader = csv.reader( csvfile, delimiter=',' )
    rows = list(reader)
    num_rows = len(rows)

while play == 1:
    os.system("clear")
    #Generates random int between 1 and number of rows/questions in csv
    rand = random.randint(1, num_rows-1)
    show_num, date, rnd, category, value, question, answer = rows[rand][:7]
     
    print ("-------------------------------------------")
    print ("                 JEOPARDY!")
    print ("-------------------------------------------")
    print ("show number: "+show_num+", date: "+date+"\n")
    print ("round: "+rnd)
    print ("category: "+category)
    print ("value: "+value,"\n")
    print ("Question:\n\n"+question)
    user_ans = input("\nYour Answer: ").lower()
    print ("Correct Answer: "+answer+"\n\n")

    #<Did not implement logic check yet due to issues where user>
    #<  misspelling or only putting last name instead of full   >
    #<  name (e.g. Obama, not Barack Obama) are counted as wrong>

    #Asks user if answer was same as displayed correct answer
    user_corr = input("Was your answer right? (y or n, press enter to skip): ").lower()
     
    #Adds question value to total if yes
    if user_corr == "y" or user_corr == "yes":
        tot += int(value)
    #Subtracts question value from total if no
    elif user_corr == "n" or user_corr == "no":
        tot -= int(value)
    #Leaves total unchanged if [return] or any input besides y/yes or n/no
    else:
        print ("Question skipped!")
    print ("Running Total: "+str(tot)+"\n")

    # Saves running total to config file
    config['Save']['RunningTotal'] = str(tot)
    with open(CONFIG_LOCATION, 'w') as configfile:
        config.write(configfile)

    #Asks user if they want to play again and sets play value
    user_play = input("Play Again (y or n)?: ").lower()
    if user_play == "y" or user_play == "yes":
        play = 1
    else:
        play = 0
