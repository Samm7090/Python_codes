gender=input("Enter your gender male/female ")
game_type=input("Enter the type of game indoor/outdoor ")
if(gender=="male"):
    if(game_type=="indoor" or game_type=="Indoor"):
        print("You are ",gender,"You have chossen the ",game_type, "game")
    else:
        print("You are ", gender, "You have chossen the ", game_type, "game")
elif(gender=="female"):
    if(game_type=="indoor" or game_type=="Indoor"):
        print("You are ",gender,"You have chossen the ",game_type, "game")
    else:
        print("You are ", gender, "You have chossen the ", game_type, "game")
else:
    print("kuch samje aesa likho")