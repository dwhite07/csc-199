#Setting a score variable to an integer value that the user will input
score = int(input('Enter a score greater than 1: '))

#Setting Variables
touchdown = 0
fieldgoal = 0
safety = 0

#Starting a while loop and ensuring that any number inputted less than or equal to 1 will not count
while (score <= 1) :
       score = int(input('Enter a score greater than 1: '))

#Only performing this step if 7 divides into the score with a remainder of 0
#This step calculates the value of touchdowns
if (score % 7 == 0):
    touchdown = score / 7

#Only performing this step if 3 divides into the score with a remainder of 0
#This step calculates the value of fieldgoals
elif (score % 3 == 0):
    fieldgoal = score / 3

#Only performing this step if 2 divides into the score with a remainder of 0
#This step calculates the value of safeties
elif (score % 2 == 0):
    safety = score / 2

#If no football points divide into the score with a remainder of 0 then this step will be performed
#Since there are no possible combinations of points the user is told "No possible combinations" and then the program is ended.
else:
    print("No possible combinations")
    raise SystemExit
    exit

#Print a combination of points they could have gotten
print("One posssible combination of points you earned is this many touchdowns: " , touchdown , ", this many fieldgoals: " , fieldgoal , ", and this many safeties: " , safety)

#Calculating what the greatest number of touchdowns can be
"""This is done by setting the remainder after possible touchdowns are taken in, then subtracting the remainder from the score
After this touchdown variable is reset to 7 since a touchdown is 7 points.
Finally, the most amount of touchdowns possible is calculated by dividing the new score without the remainder by the amount of touchdowns to get a whole number.
Then the most amount of touchdowns possible is printed."""
remainder = score % 7
score -= remainder
touchdown = 7
most_touchdowns = score / touchdown
print("The greatest number of touchdowns scored possible is: ", most_touchdowns)
