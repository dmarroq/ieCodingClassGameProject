# codingFinalProject_v4.py
#
# Notes: Whew! That was fun! Long though. We found out during the creation of the actual code that
# our pseudocode had to be modified. Our pseudocode originally had one function for the commands,
# but it turned out super weird, so we made every command its own function.
# So the move command would actually count what room you were in, and we had to put that number in a list,
# since initializing it as an integer in the main just kept turning it back to 0
# We had to split the file twice to try things so they could work! Anyway, we figured out
# that you can call a variable from a function to another function by returning the desired variable.
# Please enjoy our game! Also, at the end, a score above 0 is bad.

from graphics import *


# Function that lets you move through rooms and gets the room number you are in
def moves(room, a, inventory, actionCount):
    actionCount = str(actionCount)
    if 'MOVE' in a.upper():
        # beginning room movement options
        if room[0] == 0:
            while room[0] == 0:
                movement = input("You can move: \n WEST \n NORTH \n ").upper()
                if movement == 'WEST':
                    room[0] += 1
                    # Record action result in log
                    print('In room 2')
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + movement + "\n")
                    logText.close()
                    return
                elif movement == 'NORTH':
                    room[0] += 2
                    # Record action result in log
                    print('In room 3')
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + movement + "\n")
                    logText.close()
                    if 'FRIEND: BROKEN TORCH' in inventory:
                        print("Broken Torch's flickering light illuminates what it can, yet the room is dark,")
                        print("high walls rising into a deeply shadowed ceiling. You feel the dark press on you.")
                        print("Heavy Air seems to sigh and float up, while Broken Torch huddles")
                        print("closer to you, light fading slightly.")
                        print("The room is empty except for a gleaming golden amulet with a blood-red ruby")
                        print("embedded in its center. It hangs on a worn leather strap, seemingly from nothing.")
                        print("At the far north of the room, you can see a pit leading down into another room.")
                    else:
                        print("The room is too dark! You cannot see anything.")
                    return
                elif movement == 'EXIT':
                    return
                else:
                    print("Please type 'WEST' or 'NORTH'")
                    continue
        # first room movement options
        if room[0] == 1:
            while True:
                movement = input("You can move: \n EAST \n ").upper()
                if movement == 'EAST':
                    room[0] -= 1
                    # Record action result in log
                    print('In room 1')
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + movement + "\n")
                    logText.close()
                    return
                elif movement == 'EXIT':
                    return
                else:
                    print("Please type 'EAST'")
                    continue
        # Second room movement options
        if room[0] == 2:
            while True:
                if 'FRIEND: BROKEN TORCH' in inventory and 'FRIEND: HEAVY AIR' in inventory:
                    movement = input("You can move: \n DOWN \n SOUTH \n ").upper()
                    if movement == 'DOWN':
                        room[0] += 1
                        # Record action result in log
                        print("You jump down, and Heavy Air softens your fall.")
                        print('In room 4')
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + movement + "\n")
                        logText.close()
                        return
                    elif movement == 'SOUTH':
                        room[0] -= 2
                        # Record action result in log
                        print('In room 1')
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + movement + "\n")
                        logText.close()
                        return
                    elif movement == 'EXIT':
                        return
                    else:
                        print("Please type 'DOWN' or 'SOUTH'")
                        continue
                elif 'FRIEND: BROKEN TORCH' not in inventory:
                    movement = input("It's too dark to see!: \n SOUTH \n ").upper()
                    if movement == 'SOUTH':
                        room[0] -= 2
                        # Record action result in log
                        print('In room 1')
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + movement + "\n")
                        logText.close()
                        return
                    elif movement == 'EXIT':
                        return
                    else:
                        print("Please type 'SOUTH'")
                        continue
                elif 'FRIEND: HEAVY AIR' not in inventory and 'FRIEND: BROKEN TORCH' in inventory:
                    movement = input("The way down is too far a drop: \n SOUTH \n ").upper()
                    if movement == 'SOUTH':
                        room[0] -= 2
                        # Record action result in log
                        print('In room 1')
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + movement + "\n")
                        logText.close()
                        return
                    elif movement == 'EXIT':
                        return
                    else:
                        print("Please type 'SOUTH'")
                        continue
        # Third room movement options
        if room[0] == 3:
            while True:
                movement = input("You can move: \n SOUTH \n UP \n ").upper()
                if movement == 'SOUTH':
                    room[0] += 1
                    # Record action result in log
                    print('In room 5')
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + movement + "\n")
                    logText.close()
                    return
                elif movement == 'UP':
                    room[0] -= 1
                    print("Heavy Air envelopes you, and when you jump, somehow you float up through the opening.")
                    # Record action result in log
                    print('In room 2')
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + movement + "\n")
                    logText.close()
                    return room[0]
                elif movement == 'EXIT':
                    return
                else:
                    print("Please type 'SOUTH' or 'UP")
                    continue
        # Final room movement options
        if room[0] == 4:
            while True:
                movement = input("You can move: \n NORTH \n ").upper()
                if movement == 'NORTH':
                    room[0] -= 1
                    # Record action result in log
                    print('In room 3')
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + movement + "\n")
                    logText.close()
                    return
                elif movement == 'EXIT':
                    return
                else:
                    print("Please type 'NORTH")
                    continue
    else:
        return
    return room

# Action function that gets the action input from main and gives options for actions depending on room
# Also gets the score for the final puzzle, and uses actionCount to use in log
def action(room, a, inventory, scoreCount, actionCount):
    actionCount = str(actionCount)
    finalInventory = ["FRIEND: HEAVY AIR",
                      "FRIEND: BROKEN TORCH",
                      "ITEM: SMALL SHOES",
                      "ITEM: AMULET",
                      "ITEM: AGED STATUE"]
    if a == 'ACTION':
        # Beginning room inspection actions
        if room[0] == 0:
            # Describe room
            while True:
                if 'FRIEND: HEAVY AIR' not in inventory:
                    actions = input("What would you like to do?: \n TWIRL \n PICK UP \n ").upper()
                    if actions == 'TWIRL':
                        print("The air swirls around you. It feels cool on your skin.")
                        print("It seems to wrap around your arms and fingers, like water, and weighs on your shoulders.")
                        print("There's a whistling laughter in your ear.")
                        print("The air drapes around your body like a cloak. You now have a Heavy Air friend!")
                        # Store FRIEND: HEAVY AIR in text file or list Inventory
                        inventory.append("FRIEND: HEAVY AIR")
                        # Record action result in log
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + actions + "\n")
                        logText.close()
                        return
                    elif actions == 'PICK UP':
                        # Record action result in log
                        print("You look around, but there's nothing here!")
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + actions + "\n")
                        logText.close()
                        return
                    elif actions == 'EXIT':
                        return
                    else:
                        print("Please type 'TWIRL' or 'PICK UP'")
                        continue
                else:
                    actions = input("What would you like to do?: \n PICK UP \n ").upper()
                    if actions == 'PICK UP':
                        # Record action result in log
                        print("You look around, but there's nothing here!")
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + actions + "\n")
                        logText.close()
                        return
                    else:
                        print("Please type 'PICK UP'")
                        continue
        # First room inspection actions
        if room[0] == 1:
            # Describe room
            while True:
                if 'FRIEND: BROKEN TORCH' not in inventory:
                    actions = input("What would you like to do?: \n PULL TORCH \n PICK UP \n ").upper()
                    logText = open('Log.txt', 'a')
                    logText.write(actionCount + " " + a + ": " + actions + "\n")
                    logText.close()
                    if 'PULL' in actions:
                        print("Lucky! The torch may hide a secret passageway!")
                        print("After three tries to pull torch down, it breaks.")
                        print("Unfortunately it was just a normal torch. How rude! You just broke the poor Torch.")
                        if "FRIEND: HEAVY AIR" in inventory:
                            print("Heavy Air whistles in amusement as torch dims in disappointment at your rudeness.")
                        else:
                            print("Torch dims in disappointment at your rudeness.")

                        actions = input("Apologize to Torch? \n APOLOGIZE \n NO \n ").upper()

                        if actions == 'APOLOGIZE':
                            print("Maybe you can fix them if you get out! You now have a Broken Torch friend :).")
                            if "FRIEND: HEAVY AIR" in inventory:
                                print("It floats around you, hissing slightly as Heavy Air")
                                print("slaps at it with a mischievous whispering chuckle.")
                            else:
                                pass
                            # Store FRIEND: BROKEN TORCH in text file or list Inventory
                            inventory.append("FRIEND: BROKEN TORCH")
                            # Record action result in log
                            logText = open('Log.txt', 'a')
                            logText.write(actionCount + " " + a + ": " + actions + "\n")
                            logText.close()
                            return
                        else:
                            # I can't seem to figure out how to make a loop that doesn't break the game
                            # to continue to ask the player if they would like to apologize
                            print("How rude! Torch looks dejected.")
                            return
                    elif actions == 'PICK UP':
                        # Store ITEM: SMALL SHOES in inventory
                        if 'ITEM: SMALL SHOES' not in inventory:
                            print("You got a pair of shoes! They're too small for you though. (Stored in inventory)")
                            inventory.append("ITEM: SMALL SHOES")
                            # Record action result in log
                            logText = open('Log.txt', 'a')
                            logText.write(actionCount + " " + a + ": " + actions + "\n")
                            logText.close()
                            return
                        elif actions == 'EXIT':
                            return
                        else:
                            print("There is nothing else here.")
                            return
                    elif actions == 'EXIT':
                        return
                    else:
                        print("Please type 'PULL' or 'PICK UP'")
                        continue
                else:
                    actions = input("What would you like to do?: \n PICK UP \n ").upper()
                    if actions == 'PICK UP':
                        # Store ITEM: SMALL SHOES in inventory
                        if 'ITEM: SMALL SHOES' not in inventory:
                            print("You got a pair of shoes! They're too small for you though. (Stored in inventory)")
                            inventory.append("ITEM: SMALL SHOES")
                            # Record action result in log
                            logText = open('Log.txt', 'a')
                            logText.write(actionCount + " " + a + ": " + actions + "\n")
                            logText.close()
                            return

                        else:
                            print("There is nothing else here.")
                            return
                    elif actions == 'EXIT':
                        return
                    else:
                        print("Please type 'PULL' or 'PICK UP'")
                        continue
        # Second room inspection
        if room[0] == 2:
            # Describe room

            while True:
                actions = input("What would you like to do?: \n PICK UP \n ").upper()
                if actions == 'PICK UP':
                    if 'ITEM: AMULET' not in inventory:
                        print("You've obtained the AMULET! (Stored in inventory)")
                        # Store ITEM: AMULET in text file or list Inventory
                        inventory.append("ITEM: AMULET")
                        # Record action result in log
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + actions + "\n")
                        logText.close()
                        return
                    else:
                        print("There is nothing else here.")
                        return
                elif actions == 'EXIT':
                    return
                else:
                    print("Please type 'PICK UP'")
                    continue
        # Third room inspection
        if room[0] == 3:
            # Describe room
            while True:
                actions = input("What would you like to do?: \n PICK UP \n ").upper()
                if actions == 'PICK UP':
                    if 'ITEM: AGED STATUE' not in inventory:
                        print("Heavy Air envelopes you and when you lift the statue, if feels almost weightless.")
                        print("You've obtained the AGED STATUE! (Stored in inventory)")
                        # Store ITEM: AMULET in text file or list Inventory
                        inventory.append("ITEM: AGED STATUE")
                        # Record action result in log
                        logText = open('Log.txt', 'a')
                        logText.write(actionCount + " " + a + ": " + actions + "\n")
                        logText.close()
                        return
                    else:
                        print("There is nothing else here.")
                        return
                elif actions == 'EXIT':
                    return
                else:
                    print("Please type 'PICK UP'")
                    continue
        # Final room puzzle conditional needs to tell user that they do not have all the items they need
        if room[0] == 4:
            # Describe room

            while True:

                if len(inventory) == len(finalInventory):
                    # Final puzzle. Make a loop that takes input. While keywords are not fulfilled, print back:
                    # "You did", input, "but nothing happened!"
                    while True:
                        print("What would you like to do?")
                        actions = input(" STAND ON STONE \n EQUIP BOOTS \n PUT BOOTS ON STATUE \n ").upper()
                        if actions == "PUT BOOTS ON STATUE":
                            print("As soon as you manage to get the boots on the statue, it stands up and walks")
                            print("to stand on the stone!")
                            print("Now what would you like to do?")
                            actions = input(" EQUIP AMULET \n PUT AMULET ON STATUE \n ").upper()
                            logText = open('Log.txt', 'a')
                            logText.write(actionCount + " " + a + ": " + actions + "\n")
                            logText.close()
                            if actions == 'EQUIP AMULET':
                                print("You put the amulet on and stand in front of the door, but nothing happens!")
                                print("Until, a sudden gust of wind from Heavy Air makes Broken Torch flare.")
                                print("The light catches on the Amulet's ruby, and a beam of red connects the")
                                print("Amulet and the door. With a great 'clunk!', the door begins to swing out.")
                                print("Light streams from the exit, and you see an old ladder made of black iron")
                                print("leading into the outside world.")
                                room[0] += 1
                                return
                            else:
                                print("You tried it, but nothing happened!")
                                scoreCount[0] += 1
                                continue
                        else:
                            print("You tried it, but nothing happened!")
                            scoreCount[0] += 1
                            continue
                else:
                    print("You do not have all the items required to complete this puzzle")
                    scoreCount[0] += 1
                    return
    else:
        return
    return inventory


def viewInventory(a, inventory):
    # If command is VIEW INVENTORY return items in inventory and friends available
    if a == 'INVENTORY':
        for ele in inventory:
            print(ele)
        return
    else:
        return


def logger(a):
    # Not mandatory for the assignment, but would be cool
    # Record action in log in separate text file
    logText = open('Log.txt', 'r')
    log = logText.readlines()
    # View log
    if a == 'VIEW LOG':
        print('Here log')
        for lines in log:
            print(lines)
    else:
        return
    logText.close()


def observe(a, room, actionCount):
    # Command to see the storyPrint again
    actionCount = str(actionCount)
    if a == 'OBSERVE':
        logText = open('Log.txt', 'a')
        logText.write(actionCount + " " + a + "D\n")
        logText.close()
        storyText = open('Story.txt', "r")
        for line in storyText.readlines():
            if room[0] == int(line[0]):
                for ele in line.split('.'):
                    print(ele)
        storyText.close()
    else:
        return


def storyPrint(room, roomsVisited):
    # Print according to room number
    storyText = open('Story.txt', "r")
    for line in storyText.readlines():
        if room[0] == int(line[0]) and room[0] not in roomsVisited:
            for ele in line.split('.'):
                print(ele)
            # appends the room number to roomsVisited list so we don't get story print every time you enter a room
            roomsVisited.append(room[0])

    storyText.close()


def beginningGui():
    win = GraphWin("DUNGEON CRAWL", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw interface
    Text(Point(1.5, 3), "WELCOME").draw(win)
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "ENTER")
    button.setFill('gray')
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # wait for mouse click
    win.getMouse()

    # wait for click and then quit
    win.getMouse()
    win.close()


def __main__():
    beginningGui()
    room = [0]  # Had to change room variable from int to list because it somehow made the movement option output twice
    inventory = []
    scoreCount = [0]  # Same thing happened as with room
    roomsVisited = []
    actionCount = 0
    print("You wake up in a dark stone room.")
    while room[0] < 5:
        storyPrint(room, roomsVisited)  # Will print the description of each room
        print("\nActions available: \n MOVE \n ACTION \n INVENTORY \n OBSERVE \n VIEW LOG \n EXIT \n")
        a = input("What would you like to do? ").upper()
        if a != 'EXIT':
            print("\nYour command:", a)
            moves(room, a, inventory, actionCount)
            action(room, a, inventory, scoreCount, actionCount)
            viewInventory(a, inventory)
            logger(a)
            observe(a, room, actionCount)
            actionCount += 1
        else:
            break
    print("GAME END")
    print("Your score was", scoreCount[0])  # Due to the nature of the puzzle, a score higher than 0 is bad
    # Erase the log text file contents, so it doesn't get weird if you play again
    with open('Log.txt', 'w'):
        pass


if __name__ == '__main__':
    __main__()
