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

#Starting variables
yourBlock = ""
x = 1
y = 1
allowed = "N"
Victory = 0

print("You can travel: (N)orth.")
input_dir = str(input("Direction: "))
input_dir = input_dir.upper()

while Victory == 0:
    while 0 < x < 4 and 0 < y < 4 and input_dir in allowed:#Checking for "allowed" movements
    
    #Moving from your current block to your new block
        if input_dir == "N":
            y = y + 1
        elif input_dir == "S":
            y = y - 1
        elif input_dir == "E":
            x = x + 1
        elif input_dir == "W":
            x = x - 1


    #Locating your new block
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
            print("Victory!")
            Victory = 1
            break
        elif x == 3 and y == 2:
            yourBlock = middleright
        elif x == 3 and y == 3:
            yourBlock = topright
        
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

        print("You can travel:", directionoptions)
        input_dir = str(input("Direction: "))
        input_dir = input_dir.upper()        
    

    else:
        print("Not a valid direction!")
        input_dir = str(input("Direction: "))
        input_dir = input_dir.upper()        
    