import generatorMethods

y = input("How many rooms would you like to generate? (type q to quit):  ")
if y == 'q':
    exit()

else:
    for i in range(int(y)):
        x = generatorMethods.generateRoom()

        print('\n' + x + '\n')