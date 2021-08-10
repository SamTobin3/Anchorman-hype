
import random
ronfile = open( "AnchormanQuotes.txt", "r" )
quotes = ronfile.readlines()
ronfile.close()

while True:

    a = input("press r to see quotes")

    if a == "r" :
        dice = random.randint(0,len("AnchormanQuotes.txt"))
        print(quotes[dice])

    else:
        break