print('Welcome to our game')
name = input("Please Enter Your Name: ")
print("Hi",name)
print ('Your Target is Getting Gold in this game ')
print("It's very Adventure, lets go... :) ")
print (" -------------------------------------------------------------------------------------------------------------- ")

ans = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if ans == "left":
    q1 = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if q1 == "swim":
        print("You swam acrross and were eaten by an alligator. ")
    elif q1 == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else :
        print ("Sorry, not a valid option.bye")

elif ans == 'right':
    q2 = input ("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if q2 == "back":
        print("you go back and lose ")
    elif q2 == "cross":
        q3 = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if q3 == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif q3 == "no":
            print("You ignore the stranger and they are offended and you lose. ")
        else :
            print("try again.")
            exit()
    else:
        print ("sorry,not valid option :( . ")    
else :
    print("Sorry,not valid option :( .")

print("Thank you for trying",name )

