#Author: flynt100
#The main file for the Dungeon Generator App
import generatorMethods

# Current set up for calling the main set of generator methods held in the generator file and running the program.
# Takes input for n number of rooms and runs the methods n times
y = input("How many rooms would you like to generate? (type q to quit):  ")
if y == 'q':
    exit()

else:
    # Iterates through the functions and calls the generator functions
    for i in range(int(y)):
        x = generatorMethods.generateRoom()

        # Prints the results as a console string
        print('\n' + x + '\n')
