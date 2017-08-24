#randomly import list of numbers
#check if #13 is in that list

#import random
#randomList = []
#for counter in range (10):
    #randomList.append (random.randint (0, 20))
#print (randomList)
#for item in randomList :
    #if (item == 13):
        #print ("Thirteen was found")
    #elif (item != 13) :
        #print ("Thirteen was not found")


import random
randomList = []
numberFound = False
for counter in range (10):
    randomList.append (random.randint (0, 20))
person = int(input ("Please pick a number between 0 and 20"))
print (randomList)
for item in randomList :
    if (item == person):
        numberFound = True
        print ("number was found")
if (numberFound == False) :
    print ("number not found")
