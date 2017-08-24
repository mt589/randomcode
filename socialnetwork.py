import random
key = random.randint (1345, 154202424)
person = input ("what is your name?")
class User:
    #  Define the fields and methods for your object here.
    #makes the account
    def __init__ (self, name, iden):
        self.name = name
        self.connections = []  #does not have to go into the parameters because has a set value
        self.iden = iden
        self.myusers = []
        self.myusers2 = []
    def add_connection (self, name):
        self.connections.append(name)
#make connections between the account
def signUp (self, name, network):
    self.name = input ("what is your name?")
class Network:
#  Define the fields and methods for your object here.
    def __init__ (self):
        self.usernames = []
    def add_users (self, users):
        self.myusers.append (users)
        self.myusers2.append (users)
def main():
#  Define the program flow for your user interface here.

    myNetwork = Network()
    myuser = User(person, key)
    myuser2 = User(person, key)
    myuser.add_connection (myuser.name)
    myuser2.add_connection (myuser.name)
    myNetwork.add_users (myuser)
    myNetwork.add_users (myuser2)
print (person, key)

#  Runs your program.
###if   __name__ ==   '__main__':
    ###main():
