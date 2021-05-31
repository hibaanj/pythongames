game = int(input("enter the game u want to play 1:snake   2:pingpng:"))
if game == 1:
    import snake
elif game == 2:
    import pong
else:
    print("invalid number")