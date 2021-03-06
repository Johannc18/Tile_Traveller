#List of blocks where w is Wall, and e is Exit
bottomleft = "weww"
middleleft = "weee"
topleft = "wwee"
bottomcenter = "weww"
middlecenter = "ewwe"
topcenter = "ewew"
bottomright = "weww"
middleright = "wewe"
topright = "ewwe"

def newDirectionFunc(input_dir,x,y):
    #Move from your current block to your new block

    if input_dir == "N":
        y = y + 1
        return x, y
    elif input_dir == "S":
        y = y - 1
        return x,y
    elif input_dir == "E":
        x = x + 1
        return x,y
    elif input_dir == "W":
        x = x - 1
        return x,y
    else:
        return x,y   

def findyourBlock(x,y):
    #Locating your new block

    Victory = 0
    if x == 1 and y == 1:
        yourBlock = bottomleft
    elif x == 1 and y == 2:
        yourBlock = middleleft
    elif x == 1 and y == 3:
        yourBlock = topleft
    elif x == 2 and y == 1:
        yourBlock = bottomcenter
    elif x == 2 and y == 2:
        yourBlock = middlecenter
    elif x == 2 and y == 3:
        yourBlock = topcenter
    elif x == 3 and y == 1:
        yourBlock = bottomright
        print("Victory!")
        Victory = 1
              
    elif x == 3 and y == 2:
        yourBlock = middleright
    elif x == 3 and y == 3:
        yourBlock = topright
    return yourBlock,Victory

def youcantravel(yourBlock):
    #Clean slate/refresh your option variables
    allowed = ""
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""

    #Here you find the allowed directions you can travel, by checking walls and exits, then print them.
    for index,option in enumerate(yourBlock):
        if option == "e":
            if index == 0:
                option1 += "(W)est "
                allowed += "W"
            elif index == 1:
                option2 += "(N)orth "
                allowed += "N"
            elif index == 2:
                option3 += "(E)ast "
                allowed += "E"
            elif index == 3:
                option4 += "(S)outh "
                allowed += "S"
    directionoptions = option2 + option3 + option4 + option1 + "."
    directionoptions = directionoptions.replace(" ", " or ")
    directionoptions = directionoptions.replace(" or .",".")
    return directionoptions, allowed      

def main():
    #Main function's starting variables
    yourBlock = ""
    allowed = "N"
    print("You can travel: (N)orth.")
    input_dir = str(input("Direction: "))
    input_dir = input_dir.upper()
    x = 1
    y = 1

    while True:
               
        while input_dir in allowed: #Checking for "allowed" movements
    
            new_x,new_y = (newDirectionFunc(input_dir,x,y))
            yourBlock,youWin = findyourBlock(new_x,new_y)
            x,y = new_x,new_y
            dirop,allowed = youcantravel(yourBlock)
            if youWin == 1:
                return False
                #end the program for winning
            print("You can travel:", dirop)
            input_dir = str(input("Direction: "))
            input_dir = input_dir.upper()
                            
        else:
            print("Not a valid direction!")
            input_dir = str(input("Direction: "))
            input_dir = input_dir.upper()    

main()

#https://github.com/Johannc18/Tile_Traveller
