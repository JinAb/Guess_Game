

        
n = 10
number_of_gusses = 1
print("Number Of Gusses Is Only 9\n Try Your Luck If You Can: ")
while (number_of_gusses<=9):
    Guess_number = int(input("Guess The Magical Number\n"))
    if Guess_number<10:
        print("Your Guess is Lesser Than of the Number")
        print("Hint")
        print("Guess Between 5 to 19")
    elif Guess_number>10:
        print("Your Guess is Greater than of the Number")
        print("Hint")
        print("Guess Between 5 to 19")
    else:
        print("WoW You Won the Game") 
        print(number_of_gusses, "NO. Of Gusses You Took To Win The Game.\n")
        break
    print(9-number_of_gusses, "NO. Of Gusses Left")
    number_of_gusses = number_of_gusses + 1

if(number_of_gusses>9):
    print("Game Over")

    


