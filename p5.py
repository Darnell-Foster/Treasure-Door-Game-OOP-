#Darnell Foster 101229310
import random
"""
You must  not  use  any  global  variablesin  this  program  but  you  can  use  global  constants  if needed. 
Recall that a global variable is declared outside of any function on the top level of the program  that  is  available  to  the  entire  program  and  its  value canbe changed. 
And  global variables  should  always  be  avoided  if  possible. Whereas, a  global  constant  is also declared outside of any function on the top level of the programthat is available to the entire program but its value must notbe changed.
You can use this simple rule to determine the parameters/returnvalues for anyfunction.
If you want to access some data (variable/data structure/object) inside of a function, instead of using a global variable you must pass thatas a parameterto thefunction. 
Similarly, if your function createsor updates somevalue(s)that you want to make available to some other partsofyour program, your function should return thatvalue(s). 
In this way,the calling function should be able to use that value.
"""
#global Constants
MAX_LEVEL = 3

class Door():
    """
     has  at  least  three  attributes: door  number  (int),  treasure  value  (int/float),and selected (bool). 
     The ‘selected’attribute is initially‘False’.
     If a player selects this door at any level, this attribute changes to True for that level.
     You may want to write a method for this process.
    """
    def __init__(self, door_number,treasure_value):
        self.door_number = door_number
        self.treasure_value = treasure_value
        self.selected = False
    


class Token():
    """
    has at least two attributes: name(string) of this token, i,e., ‘silver’/‘gold’/‘diamond’and a list of the doorobjects (or the doornumbers) that this tokencan open. 
    This class also has a method that takes a door object (or a door number) and returns True if this tokencan open that door, Otherwise, it returns False.
    It will be useful in the game to determine if the player’s token can open a particular door.
    """
    
    token_name = ""
    door_numbers = []

    def __init__(self, token_name, door1, door2, door3):
        self.token_name = token_name
        if(self.token_name == "diamond"):
            self.door_numbers = [door1,door2,door3]
        elif(self.token_name == "gold"):
            self.door_numbers = [door1,door2]
        elif(self.token_name == "silver"):
            self.door_numbers = [door1]
    

        return False
    

class Game():
    """
    has  at  least  three  attributes:  the  name (string) of  the  player,  
    a  list  of values (int/float) won/lost by the player at each level, and a bool attribute named finished, 
    which is initially False and only changes to True when the player decides to quit the game or completes all three levels of the game.
    This will be useful to determine when to end the loop/game.
    """
    player_name = ""
    earnings = [0,0,0] #for 3 levels
    finshed = False

    def __init__(self, player_name):
        self.player_name = player_name

    def total_earnings(self, current_level, selected_door, Win):
        """Adds up the game earnings
        """
        if Win == True:
            self.earnings[current_level-1] = selected_door.treasure_value
        else:
            self.earnings[current_level-1] = (selected_door.treasure_value)*-1

        total = 0
        for i in range(3):
            total += self.earnings[i]
        print("Your current total is $" + "{:.2f}".format(total))
        print()
         


def intro():
    """Shows the intro screen 
    Returns the user name"""
    name = input("Welcome what is your name?\n")
    print("Welcome " + name + " Want to find some secret treasures? Let's begin.\n")
    print("You can choose a door to get the treasures hidden behind it.")
    print("But you must also collect a token from the magic wheel to open that door.")
    print("Check how much you can win and the token you need to open a door.")
    return name

def show_menu(cur_level, doors):
    """Shows the selection menu for the game, Takes in the int current level
    Returns nothing"""
    print("Level-" + str(cur_level))
    print("----------------------------------------------------------------------")
    print("Doors         Treasures' value         Token type")
    print("[1] Door-1            $" + "{:.2f}".format(doors[0].treasure_value) +"              Silver ")
    print("[2] Door-2            $" + "{:.2f}".format(doors[1].treasure_value) +"              Gold ")
    print("[3] Door-3            $" + "{:.2f}".format(doors[2].treasure_value) +"              Diamond")

def select_door(doors):
    error = "Error, that is not an option."
    doorChoosen = False
    changeMind = False

    while(not doorChoosen or changeMind): #while you have not choosen a door OR you still want to change your mind(change mind is true till you say no)
        door = input("Which door do you want to choose? Type [1, 2, or 3]. To quit the game enter 'q'.\n")

        if (door.lower() == "q"): #if q quit, else validate input
            print("You've decided to quit..")
            print("Thanks for playing")
            quit()
        else:
            if (door.isdigit()):
                if(int(door) == 1 or int(door) == 2 or int(door) == 3):
                    doorChoosen = True
                else:print(error)
            else:print(error)
        
        if (doorChoosen == True):  #once you have choosen a door deicde if you want to change your mind
            hasConfirmedChoice = False # makes sure the loop below runs, until door has been choosen

            while(not hasConfirmedChoice): #while you haven't picked anything(input validation)
                chooseAgain = input("Do you want to change your decision and choose another door? Enter \'Yes\'/\'No\'. ")
                if(chooseAgain.lower() == "yes"): #if you do want to choose again change door from already choose to false and confirmed choice to true
                    hasConfirmedChoice = True
                    doorChoosen = False
                elif(chooseAgain.lower() == "no"): #if you don't want to choose again change "changeMind" to false and "confirmedChoice" to true
                    changeMind = False
                    hasConfirmedChoice = True
                else: print(error)
                print("you have selected Door-" + door + ". Please spin the magic wheel to collect your token.")
    door = int(door)
    
    for i in range(3):
        if door == doors[i].door_number:
            doors[i].selected = True

def get_token():
    """ Generates a random number(percentage) between 0-1 and assigns a token name based on value
    return Str token"""

    generateToken = random.random() #Generates random float from 0-1
    generateToken = round(100* generateToken,1) #converts floart to a percentage

    if(generateToken <= 0): #Assings a key based on the value of "generateToken"
        token = "silver"
    elif(generateToken <= 90):
        token = "gold"
    else:
        token = "diamond"

    print("...... (drum roll) .... you've got a " + token + " token (" + str(generateToken) + "%).")
    return token

def update_amount(token,selected_door,game,level):
    win = False
    for elem in token.door_numbers:
        if selected_door == elem:
            win = True
  

    
    if(win == True): #Checks the door and token to see if you can open it, if yes awards cash, if not takes cash away
            print("Congrats!! You've won the hidden treasure worth $" + "{:.2f}".format(selected_door.treasure_value) + ".")
    else:
        print("Bad luck... you lost $"+ "{:.2f}".format(selected_door.treasure_value) + ".")

    game.total_earnings(level,selected_door,win) 
    return


def main():
    cur_level = 1
    
    name = intro()
    g1 = Game(name) #Creates game object with name inputed by user
    while(cur_level <= MAX_LEVEL and g1.finshed == False):
        
        d1 = Door(1, 100*cur_level)
        d2 = Door(2, 200*cur_level)
        d3 = Door(3, 300*cur_level)
        doors = [d1,d2,d3]
        show_menu(cur_level,doors)
        
        select_door(doors)

        token_name = get_token()
        t1 = Token(token_name,d1, d2, d3)
        
        for i in range(3):
            if doors[i].selected == True:
                update_amount(t1,doors[i],g1,cur_level)

        

        cur_level += 1
        if cur_level > 3:
            g1.finshed = True
        else:
            while(True):
                user = input("Do you want to play the next level (Level-" + str(cur_level) + ") (enter 'Yes'/'No')? ")
                if user.isalpha():
                    if user.lower() == "yes":  
                        break
                    elif user.lower() == "no":
                        g1.finshed = True
                        break


if __name__ == "__main__":
    main()
