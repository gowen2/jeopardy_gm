#Script to give random Jeopardy! question, record answer, and keep running money total
#George Owen, 2017-05-01

import csv, random, os

#Gets full path of jeopardy.py script (this script)
script_dir = os.path.abspath(os.path.dirname(__file__))

#Imports tot variable (running money total) with value from total_jep.py
from total_jep import *

#Initializes play variable to 1 (1 = play a rounds, 0 = exit) 
play=1

#Gets path to CSV file of question dataset
CSVpath = script_dir+"/JEOPARDY_CSV.csv"
#Gets number of lines/questions in CSV
with open(CSVpath, newline='', encoding="utf-8",errors='ignore') as csvfile:
    num_rows = sum(1 for line in csvfile)

while play == 1:
    with open(CSVpath,'rt', newline='', encoding="utf-8",errors='ignore') as csvfile:
        #Creates reader object for csv file and makes rows as list of arrays
        reader = csv.reader( csvfile, delimiter=',' )
        rows = list(reader)
        #Generates random int between 1 and number of rows/questions in csv
        rand = random.randint(1, num_rows-1)
#        for i, row in enumerate(reader):
#            if i == rand:
#                show_num, date, rnd, category, value, question, answer = row[:7]
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
            tot=tot+int(value)
            print ("Running Total: "+str(tot)+"\n")
     
        #Subtracts question value from total if no
        elif user_corr == "n" or user_corr == "no":
            tot=tot-int(value)
            print ("Running Total: "+str(tot)+"\n")
     
        #Leaves total unchanged if [return] or any input besides y/yes or n/no
        else:
            tot=tot
            print ("Question skipped!")
            print ("Running Total: "+str(tot)+"\n")

        #Overwrites new running total value to total_jep.py
        totfile = open(script_dir+'/total_jep.py', 'w')
        totfile.write("tot = "+str(tot))

        #Asks user if they want to play again and sets play value
        user_play = input("Play Again (y or n)?: ").lower()
        if user_play == "y" or user_play == "yes":
            play = 1
        else:
            play = 0
