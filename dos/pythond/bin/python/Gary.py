
def scene_1():
    print("Gary is a man on his computer when he hears his fire alarm go off do you check the scene or ignore it?")
    choice = input("Do you want to check the scene or ignore it? ").lower()

    if choice == "check":
        print("Gary exits the room and sees that his food is burning.")
        scene_2()
    elif choice == "ignore":
        print("Gary stays in his room for some reason until the fire department comes.")
        scene_2()
    else:
        print("Invalid choice. Try again.")
        scene_1()

def scene_2():
    print("After putting out the fire gary then finds a cook book to help him cook should gary buy or pirate this book?")
    direction = input("Do you want to buy or pirate it? ").lower()
    
    if direction == "buy":
        print("Gary decides to buy the book")
        scene_3()
    elif direction == "pirate":
        print("Gary gets a virus good job retard")
        scene_4()
    else:
        print("Invalid choice. Try again.")
        scene_2()

def scene_3():
    print("Gary decides to buy the book but thinks a digital version would be better because it would save to his computer making him more likely to read it gary likes his computer")
    direction = input("Do you want to a buy digital or physical copy? ").lower()
    
    if direction == "digital":
        print("Gary bought it on google books")
        scene_5()
    elif direction == "physical":
        print("Gary goes to a book store & buys the book")
        scene_5()
    else:
        print("Invalid choice. Try again.")
        scene_2()

def scene_4():
    print("Gary needs a new computer he decides on a asus gaming computer anyways did you pirate this game?")
    choice = input("the question is above did you pirate this game?").lower()

    if choice == "yes":
        print("It's a free game😭")
        scene_3()
    elif choice == "no":
        print("Trick question💀")
        scene_3()
    else:
        print("Invalid choice. Try again.")
        scene_4()

def scene_5():
    print("Gary after having bought the book has to decide on what to cook")
    choice = input("Should Gary cook Popeyes Spicy Chicken Sandwich Combo or Oreo Chocolate Sandwich Cookie? ").lower()

    if choice == "chicken sandwich":
        print("He made Popeyes Spicy Chicken Sandwich Combo")
        scene_6()
    elif choice == "oreo":
        print("He made Oreo Chocolate Sandwich Cookie")
        scene_6()
    else:
        print("Invalid choice. Try again.")
        scene_5()

def scene_6():
    print("Gary ate but then got thirsty & went to find out he's out of MTN DEW Baja Blast")
    choice = input("Which store does he go to walmart or target? ").lower()

    if choice == "walmart":
        print("Gary got fukin stabbed lol")
        scene_11()
    elif choice == "target":
        print("Gary gets his Baja blast & goes home")
        scene_7()
    else:
        print("Invalid choice. Try again.")
        scene_6()

def scene_7():
    print("Gary decides to after drinking 24 oz of MTN DEW Baja Blast watch a little bit of the footy wif fa lads(I hate british people)")
    choice = input("Does he? ").lower()

    if choice == "yes":
        print("he did that & went to sleep")
        scene_8()
    elif choice == "no":
        print("He decided he's too tired")
        scene_8()
    else:
        print("Invalid choice. Try again.")
        scene_7()

def scene_8():
    print("He then woke up to see his toilet now has a head")
    choice = input("goon? ").lower()

    if choice == "yes":
        print("Gary proceeded to goon for several hours")
        scene_9()
    elif choice == "no":
        print("Gary decided that the beauty was too much to bear & decided to burn it with his flammenwerfer")
        scene_9()
    else:
        print("Invalid choice. Try again.")
        scene_8()

def scene_9():
    print("After having done that he went to go get a coffee from yeah")
    choice = input("What did Gary buy? ").lower()

    if choice == "coffee":
        print("Good job")
        scene_11()
    elif choice == "meth":
        print("The truth came out")
        scene_10()
    else:
        print("Invalid choice. Try again.")
        scene_9()

def scene_10():
    print("Good job or bad job depending on what you chose")
    choice = input("What did the Devil give Adam? ").lower()

    if choice == "choice":
        scene_12()
    else:
        print("It was never real")
        scene_10()

def scene_11():
    print("Good job or bad job depending on what you chose")
    choice = input("restart?" ).lower()

    if choice == "yes":
        print("okay")
        scene_1()
    elif choice == "no":
        quit()
    else:
        print("Invalid choice. Try again.")
        scene_11()

def scene_12():
    choice = input("restart? ").lower()

    if choice == "yes":
        print("okay")
        scene_1()
    elif choice == "no":
        quit()
    else:
        print("Stop")
        scene_12()

# Start the game
print("Hi, welcome to my [Python-based text game].")
scene_1()
