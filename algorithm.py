gwc = ["Heaven", "Kyla", "Elaine", "Dani", "Fatou", "Nayeli", "Angela", "Mia", "Jaycee"]
nameFound = False
person = input ("what is your name ")
for item in gwc :
    if (person == item): #needs to be item and not gwc because it needs to be one part of the list and not the entire list
        nameFound = True
        print ("You made the cut and are on the list")
if (nameFound == False) :
        print ("Nope can't enter the party guest list only")
