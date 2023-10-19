#Library
import random

#global variables
loop = "y" #if its y it will loop, if n it will stop the application
iUserLoad = 0 #index for loading game user history into program
iMatchLoad = 0 #index for loading game match history into program
iComputerLoad = 0 #index for loading game Computer history into program
iDrawLoad = 0 #index for loading game draw history into program
loadCounter = 0 #counts each time a line is read
currentPlayer = " " #Empty slot for current users name
lastMatch = 1 #records last match played before game 

#list structures
matchNum = [] #stores match number
user = [] #stores each user by first name
computer = [] #stores computer score
wins = [] #stores each users score
draw = [] #stores draw count

#open the file
gameHistory = open('../files/GAME_HISTORY.txt', 'r') #opens file in read mode

#add each value to list structure

##User and Draw

for row in gameHistory:
    gameHistoryContent = gameHistory.readline() #reads a line
    gameHistoryContentSplit = gameHistoryContent.split(" ") #removes the space so it can be stored
    #gameHistoryContentSplit = gameHistoryContent.split("\n")

    #add values to list structures at the specified index


    if (gameHistoryContentSplit[0] == "Draws"):
        draw.insert(iDrawLoad, gameHistoryContentSplit[1]) #adds draws
        iDrawLoad = iDrawLoad+1 #adds 1 to index


    else:
        user.insert(iUserLoad, gameHistoryContentSplit[0]) #adds username
        wins.insert(iUserLoad, gameHistoryContentSplit[1]) #adds user wins
        iUserLoad = iUserLoad+1 #adds 1 to index

    loadCounter = loadCounter+1 #adds one to loadCounter each time a line is read

#close gameHistory file
gameHistory.close()

#####match and computer##############################################

#open the file
gameHistory = open('../files/GAME_HISTORY.txt', 'r') #opens file in read mode

gameHistoryContent = gameHistory.readline()
gameHistoryContentSplit = gameHistoryContent.split(" ")

for line in gameHistory:

    if gameHistoryContentSplit[0] == "Match":
        matchNum.insert(iMatchLoad, gameHistoryContentSplit[1])
        #print(matchNum)
        iMatchLoad = iMatchLoad+1
        gameHistoryContent = gameHistory.readline()
        gameHistoryContentSplit = gameHistoryContent.split(" ")
        lastMatch = lastMatch+1

    elif gameHistoryContentSplit[0] == "Computer":
        computer.insert(iComputerLoad, gameHistoryContentSplit[1])
        #print(computer)
        iComputerLoad = iComputerLoad+1
        gameHistoryContent = gameHistory.readline()
        gameHistoryContentSplit = gameHistoryContent.split(" ")

#close gameHistory file
gameHistory.close()

while loop == "y": #starts the game on a loop, when game stops it will return to the home screen

    #functions for rules, game, and stopping the game
    def howToPlay(): #Gives users a tutorial of how to play, new users have to do it
        loopHTP = "Y" #loop to ensure user understands rules but to also make it annoying
        while loopHTP == "Y":
            print("\nThis is a game of chance....aka a dice rolling game..why? " +
                  "\nEach player will be given two dice rolls each, whoever gets above 12 first wins!" +
                  "\nOR...if both players get over 12 its a draw!" +
                  "\nHowever! if under the rarest chances neither player gets above 12 and the score is equal then it goes to a chance..but whats that?" +
                  "\nChance means the person with the highest score gets to choose whether they want to roll again, after that the other player rolls!" +
                  "\nThere are also be opportunites to get a bonus!! If you roll two numbers in a row (like 2 and 3 or 6 and 7)" +
                  "then the lower number is doubled and added to the largest" +
                  "\nIn chance, if all three rolls are in a roll (1,2,3) then it is an automatic win!" +
                  "\nYou will be going up against our champion Connor (313 248 317-51) model RK800!")

            ruleInput = input("\n\nDo you understand the rules? (Y/N)") #if no repeat, if yes start game

            if(ruleInput == "Y" or ruleInput == "y"): #user understands
                loopHTP == "N" #ends loop
                gameStart() #starts game
                break

            elif (ruleInput == "N" or ruleInput == "n"): #user needs it to be repeated
                loopHTP == "Y" #continues loop

            else:
                print("error 01\nSee ERROR_LIST\n")
            
        


#Follow rules, 2 rolls each, if score greater than 12 is a win, both over 12 draw, below 12 highest wins, below 12 and draw is chance round
    def gameStart(): #starts the game

        #variables
        gameLoop = "Y" # y = loop n = end
        userWins = 0 #total amount of times the user wins
        computerWins = 0 #total amount of times the computer wins
        drawTotal = 0 #total amount of times its a draw

        while gameLoop == "Y":
            
            #computer rolls first
            computerR1 = random.randint(1,6) #computers first roll
            computerR2 = random.randint(1,6) #computers second roll

            print("Connor has rolled twice, he got: ")
            print(computerR1)
            print(computerR2)
            
            computerTotal = computerR1 + computerR2 #total of both rolls
            print("Connor has a total of:")
            print(computerTotal)
            print("\n\nNow it is your turn!")

            #user rolls second
            input("\n\nPRESS ENTER TO ROLL!") #give realism of rolling a dice
            userR1 = random.randint(1,6) #users first roll
            print('Your first roll is:')
            print(userR1)
            input("\n\nPRESS ENTER TO ROLL!") #give realism of rolling a dice
            userR2 = random.randint(1,6) #users second roll
            print("Your second roll is a:")
            print(userR2)
            userTotal = userR1 + userR2 #Total of both of users rolls
            print("Overall you have rolled:")
            print(userTotal)
            input("\n\nCalculating score.....[PRESS ENTER]")

            #adds bonuses for computer
            if (computerR1 + 1 == computerR2): #(R1 being lower value (1 + 1 == 2) )
                computerBonusTotal = (computerR1 * 2) + computerR2 #doubles R1 and adds to R2
                computerTotal = computerBonusTotal #sets new computer total
                print ("OH NO! Looks like Connor has gotten a sequence!" +
                       "\nWe have gone ahead and doubled R1....Connors' new total is:\n")
                print(computerTotal)
                input("[PRESS ENTER TO CONTINUE]")
                print("\n\n")

            elif(computerR2 + 1 == computerR1): #(R2 being lower value (1 + 1 == 2) )
                computerBonusTotal = (computerR2 * 2) + computerR1 #doubles R1 and adds to R2
                computerTotal = computerBonusTotal #sets new computer total
                print ("OH NO! Looks like Connor has gotten a sequence!" +
                       "\nWe have gone ahead and doubled R2....Connors' new total is:\n")
                print(computerTotal)
                input("[PRESS ENTER TO CONTINUE]")
                print("\n\n")

            #add bonuses for user
            
            if (userR1 + 1 == userR2): #(R1 being lower value (1 + 1 == 2) )
                userBonusTotal = (userR1 * 2) + userR2 #doubles R1 and adds to R2
                userTotal = userBonusTotal #sets new user total
                print("Looks like you have gotten a sequence!" +
                      "\nWe have gone ahead and doubled R1....Your new total is:\n")
                print(userTotal)
                input("[PRESS ENTER TO CONTINUE]")
                print("\n\n")
                

            elif (userR2 + 1 == userR1): #(R2 being lower (1 + 1 == 2) )
                userBonusTotal = (userR2 * 2) + userR1 #doubles R2 and adds to R1
                userTotal = userBonusTotal #sets new user total
                print("Looks like you have gotten a sequence!" +
                      "\nWe have gone ahead and doubled R2....Your new total is:\n")
                print(userTotal)
                input("[PRESS ENTER TO CONTINUE]")
                print("\n\n")

            #figure out score

            if(computerTotal > 12): #if computer/both gets over 12
                if(userTotal > 12): #if user score is over 12 which means draw
                    print("What a boring game....its a draw.")
                    drawTotal = drawTotal + 1 #adds a draw to the record

                else: #computer wins
                    print("WOW! Connor wins again!")
                    computerWins = computerWins + 1 #adds a computer win to the record

            elif(computerTotal <= 12): #if computer/both gets under 12
                if(userTotal > 12): #if user score is over 12
                    print("CONGRADULATIONS!!! You have beat Connor by getting over 12 first!")
                    userWins = userWins + 1 #adds a user win to the record
                    

                elif(userTotal > computerTotal): #if user total is greater than computer
                    print("Well done! You have just beat Connor!")
                    userWins = userWins + 1 #adds a user win to the record

                elif(userTotal < computerTotal): #if user total is less than computer
                    print("What a close game! Connor just beat you!")
                    computerWins = computerWins + 1 #adds a computer win to record

                elif(userTotal == computerTotal): #if score is equal

                    #roll third dice
                    print("Its a tie game....However no one has scored over 12! Time for the Chance round!!!")
                    chanceInput = input("PRESS [ENTER]")

                    #computer
                    computerR3 = random.randint(1,6) #random roll
                    computerTotal = computerTotal + computerR3 #adds roll to computerTotal
                    print("\n\nConnor now has a total of:")
                    print(computerTotal)
                    print("\n\nNow it is your turn!")

                    #user
                    userR3I = input("PRESS [ENTER] TO ROLL")
                    userR3 = random.randint(1,6) #random roll
                    userTotal = userTotal + userR3 #adds user roll to userTotal
                    print("\n\nYou have rolled:")
                    print(userR3)
                    print("\nThis brings your total to:")
                    print(userTotal)
                    input("\n\nNow! Lets see who has won! [ENTER]")

                    #check computer for automatic win 3 in row

                    if((computerR1 + computerR2 - computerR3 == computerR3)
                         or (computerR2 + computerR3 - computerR1 == computerR1)
                         or (computerR3 + computerR1 - computerR2 == computerR2)): #computer wins
                        print("OH No!!! CONNOR HAS GOTTEN THREE IN A ROW!! HE HAS WON!")
                        computerWins = computerWins + 1 #adds 1 to computer wins
                    
                    elif((userR1 + userR2 - userR3 == userR3)
                       or (userR2 + userR3 - userR1 == userR1)
                       or (userR3 + userR1 - userR2 == userR2)): #user wins
                        print("WOW! THREE IN A ROW!!! You have won!")
                        userWins = userWins+1 #adds 1 to user wins

                                                
                    #see who the winner is

                    elif(computerTotal > 12): #if computer/both gets over 12
                        if(userTotal > 12): #if user score is over 12 which means draw
                            print("What a boring game....its a draw.")
                            drawTotal = drawTotal + 1 #adds a draw to the record

                        else: #computer wins
                            print("WOW! Connor wins again!")
                            computerWins = computerWins + 1 #adds a computer win to the record

                    elif(computerTotal <= 12): #if computer/both gets under 12
                        if(userTotal > 12): #if user score is over 12
                            print("CONGRADULATIONS!!! You have beat Connor by getting over 12 first!")
                            userWins = userWins + 1 #adds a user win to the record

                        elif(userTotal > computerTotal): #if user total is greater than computer
                            print("Well done! You have just beat Connor!")
                            userWins = userWins + 1 #adds a user win to the record

                        elif(userTotal < computerTotal): #if user total is less than computer
                            print("What a close game! Connor just beat you!")
                            computerWins = computerWins + 1 #adds a computer win to record

                        elif(userTotal == computerTotal): #if score is equal
                            print("WHAT ARE THE CHANCES!!!! IT'S A DRAW AGAIN!!")
                            drawTotal = drawTotal + 1 #adds a draw to the record
                

            #REMATCH OR END GAME
            replayInput = input("\n\nWould you like to play again? [Y/N]: ") #Y = replay N = No/Break

            if(replayInput == "Y" or replayInput == "y"):
                gameLoop = "Y" #rematch
                
            elif(replayInput == "N" or replayInput == "n"):
                gameLoop = "N" #end game

                #add records to list structure
                wins.append(userWins)
                draw.append(drawTotal)
                computer.append(computerWins)

                #append history
                closeFile = open('../files/GAME_HISTORY.txt', 'w') #opens the file to record results
                writeLoop = 0
                matchNumber = 0

                while writeLoop <= iUserLoad:

                    if (matchNum[writeLoop] == lastMatch):
                        closeFile.write("\n") #new line
                        closeFile.write("Match ")
                        closeFile.write(str(matchNum[writeLoop]) ) #writes match number
                        closeFile.write("\n") #new line
                        closeFile.write(user[writeLoop] + " ") #writes user name
                        closeFile.write(str(wins[writeLoop])) #writes user wins
                        closeFile.write("\n") #new line
                        closeFile.write("Computer ")
                        closeFile.write(str(computer[writeLoop])) #writes computer wins
                        closeFile.write("\n") #new line
                        closeFile.write("Draws ")
                        closeFile.write(str(draw[writeLoop])) #writes draw total
                        writeLoop = writeLoop+1
                        print("PLEASE CLOSE APPLICATION, THE LOOP REFUSES TO END. FAILING TO DO SO WILL BREAK EVERYTHING!")
                        gameLoop = "N" #end game

                    else:
                        closeFile.write("Match ")
                        closeFile.write(str(matchNum[writeLoop]) ) #writes match number
                        #closeFile.write("\n") #new line
                        closeFile.write(user[writeLoop] + " ") #writes user name
                        closeFile.write(str(wins[writeLoop])) #writes user wins
                        closeFile.write("Computer ")
                        closeFile.write(str(computer[writeLoop])) #writes computer wins
                        closeFile.write("Draws ")
                        closeFile.write(str(draw[writeLoop])) #writes draw total
                        writeLoop = writeLoop+1


    def errorList(): #idk whether to keep
        errorFile = open('../files/ERROR_LIST.txt', 'r') #opens file in read mode
        for row in errorFile:
            errorFileR = errorFile.readlines()
            print(errorFileR[0])
            print(errorFileR[1])
            
        print("\n")
        errorFile.close()
        
            
            

    def gameEnd(): #ends the program
        exit()



    #actual code for game    
    print("Welcome to the Ultimate Dice Rolling Championship!\n")
    inputName = input("To start please tell me your name, or pick an option from below: " +
                      "\n\n1. Error List" +
                      "\n2. Close Application" +
                      "\n\nPlease Enter your name or option number: ") #input section

    #check if name is valid (<2)
    if (inputName in user): #existing player
        currentPlayer = inputName
        print("\nHello there " + currentPlayer
              + "! It seems like you have already played this game before, would you like a refresher of the rules?")
        ruleInput = input("Y/N: ")

        #if the user selects N it will start the game, y will tell them the rules
        if (ruleInput == "N" or ruleInput == "n"):
            currentPlayer = inputName
            user.insert(iUserLoad, currentPlayer) #adds current player to record
            iMatchLoad = iMatchLoad+1 #generates new game
            matchNum.insert(iMatchLoad, iMatchLoad) #adds new game to record
            gameStart() #loads gameStart function
            
        elif (ruleInput == "Y" or ruleInput == "y"):
            currentPlayer = inputName
            user.insert(iUserLoad, currentPlayer) #adds current player to record
            iMatchLoad = iMatchLoad + 1 #generates new game
            matchNum.insert(iMatchLoad, iMatchLoad) #adds new game to record
            howToPlay() #loads howToPlay function

        else:
            print("error 01\nSee ERROR_LIST\n")
            
    elif (inputName == "1"): #see error list
        errorList() #loads errorList function
        
    elif (inputName == "2"): #end program
        gameEnd()
    
        
    else:
        currentPlayer = inputName
        print("\nAhh a new player...well Hello There " + currentPlayer
              + "! \nUnfortunatly, all our new players have to go through the rules of the game...sorry\n\n\n")
        input("PRESS [ENTER] TO CONTINUE")
        user.insert(iUserLoad, currentPlayer) #adds current player to record
        iMatchLoad = iMatchLoad+1 #generates new game
        matchNum.insert(iMatchLoad, iMatchLoad) #adds new game to record
        howToPlay()
