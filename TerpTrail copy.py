
import pygame, sys, easygui, random
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

font = pygame.font.Font("PixelCowboy.ttf", 25)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("PixelCowboy.ttf", size)

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    max_width = max_width - 200
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def start():
    #text = ""
    background = 'UMD_aerial.jpg'
    status = [10, 0, 0, ""]
        #   [hp, stamina, smarts, text]
    #hp = 10
    #stamina = 0
    #smarts = 0
    introText = "Welcome to Terp Trail! Your goal is to climb Stamp hill. Think you have what it takes?\n \
        Time to choose a major! You have a long journey ahead, choose wisely!\n \
        You will begin the game with 10 health points(HP).\
            \nThese are your major options\n \
            1. CompSci: Stamina = 1, Smarts = 3\n \
            2. Bio: Stamina = 1, Smarts = 2\n \
            3. Business: Stamina = 3, Smarts = 1\n \
            4. Psych: Stamina = 2, Smarts = 2\n \
                     Select 'Next' to type in a major name."
    hensonText = 'You make your way to the CompSci building.\
        \n You bump into an old classmate, Jim Henson.\
        \n Jim Henson: Hello friend, long time no see.\n Whats 9 + 10?\n \
        Here are your choices: 19, 21, 910, 9.10'
    darryllText = "You have made it to the newest dining hall on campus. \nLooks who's here, President Darryll Pines!\
        \nDarryll Pines: Hello Terp. I hope you are loving your time at UMD\
        \nWe have recently opened a new dining hall.\
        \nThe new dining hall is named in honor of the Piscataway, \
        \nwho are indigenous to Maryland.\
        \nYahentamitsi means “a place to go eat” in the Piscataway people’s\
        \nspoken Algonquian language.\
        \nLet's take a selfie together to commemorate the opening of Yahentamitsi!"
    clariceText = "You have made it to The Clarice Smith Performing Arts Center.\
        \nIt's time for a Pop Quiz! Let's see if you know your stuff.\
        \nIs the Clarice one of the 12 'SCHOOLS' within UMD?"
    journalismText = "You have wandered down to the Journalism Building \
        \nRandom Student: Welcome to the Journalism Building, home of The Diamondback\
        \nThank you for joining us. Would you like to participate in an interview for next week's paper?"
    endText = "You have FINALLY made it to STAMP. You can now enjoy some Chick-fil-a \
        \nFinal HP: " + str(status[0]) + " \
        \nFinal stamina points: " + str(status[1]) + "\
        \nFinal smart points: " + str(status[2]) + " \
        \nThis has been the end of Terp Trail. \
        \nWould you like to play again?"

    def resetPlayScreen(background):
            currentBackground = pygame.image.load(background)
            SCREEN.fill((0, 0, 0))
            SCREEN.blit(currentBackground, (0,0))

            # Low opacity textbox
            textBox = pygame.Surface((1204, 300))
            textBox.set_alpha(160)
            textBox.fill((0,0,0))
            SCREEN.blit(textBox, (0,350))

    def naming():
        player_name = easygui.enterbox('What is your name Terp (limit 12 characters)?: ')
        if len(player_name) <= 0:
            naming()
        return player_name

    def intro():
  
        CompSci = 1
        Bio = 2
        Business = 3
        Psych = 4
    
        choose_your_major = easygui.enterbox("Enter Major (Case Sensitive): ")
        if (choose_your_major == "CompSci") or (choose_your_major == "Bio") or (choose_your_major == "Business") or (choose_your_major == "Psych"):
            return choose_your_major

        else:
            intro()

    def random1(status): #deal out hit to hp for stop 1
    #rocks = random.choices([1,2], weights = [4, 1])[0]
    #print("uh oh, looks like") # a dialogue for the random occurance
    
        instances = ["Rock", "Pothole", "Squirrel", "Veo", "Blank"]
    
        value = random.choice(instances)
        output = "Uh oh...\n" # a dialogue for the random occurance
                                        #substract healthpoints on the backend
        if value == "Rock":
            output = output + ("Oops you tripped over some Rocks. You lost some HP!")
            status[0] = status[0] - 1
        elif value == "Pothole":
            output = output + ("Dang, you fell in an pothole. You lost some HP!")
            status[0] = status[0] - 1
        elif value == "Squirrel":
            output = output + ("S to the I to M to the P, there's squirrels in your pants! You lost some HP!")
            status[0] =status[0] - 2
        elif value == "Veo":
            output = output + ("Watch where you're going... \n YOU GOT RUN OVER BY A VEO!! You lost some HP!")
            status[0] =status[0] - 2
        else:
            output = output + ("hmmmm nevermind. \nYou avoided a random obstacle!")
        status[3] = output
        return(status)

    def stop1(status):
        question = easygui.enterbox("Type Answer Here (numbers only): ")
        if  question == "19":
            output = "CORRECT: Smart lad, you may continue. \nYou have gained smart points!"
            status[2] = status[2] + 2
        
        elif question == "21":
            output = "Haha, you're funny, I will let you go just this once. \nYou have gained smart points!"
            status[2] = status[2] + 1
        
        elif question == "910":
            output = "WRONG: I think you should change your major.\nYou have lost smart points!"
            status[2] = status[2] - 2
        
        elif question == "9.10":
            output = "WRONG: Are you even trying?\nYou have lost smart points!"
            status[2] = status[2] - 2
        
        else:
            print("That was not one of the choices. Guess again")
            stop1(status[2])
        
        status[3] = output
        return(status)

    def stop2(status):
        picture = easygui.enterbox("Do you want to take the selfie (y/n): ")
        if picture.lower() == "y":
            output = "Darryll Pines: Great, smile for the camera\nYou have gained stamina points!"
            status[1] = status[1] + 1
            time = +2
        elif picture.lower() == "n":
            output = "Darryll Pines: I understand, you're a busy person. Maybe next time"
            time = +1
        else:
            stop2(status[1])

        status[3] = output
        return(status)

    def stop3(status):
        school = easygui.enterbox("What do you think? (y/n): ")
        if school.lower() == "n":
            output = 'Oh, you really know your stuff. \nYou have gained smart points!'
            status[2] = status[2] + 1
            time = +1
        elif school.lower() == "y":
            output = "Wrong: That was a tricky question. Better luck next time. \nYou have lost smart points."
            status[2] = status[2] - 1
            time = +3
        else:
            stop3(status[2])
        
        status[3] = output
        return(status)

    def random2(status):
        instances = ["Homework", "Hunger", "Weather", "Bus", "Blank"]
    
        value = random.choice(instances)
        output = "Uh oh...\n" # a dialogue for the random occurance
                                        #substract healthpoints on the backend
        if value == "Homework":
            output = output + ("You just remembered you had homework due")
            status[2] = status[2] - 1
        elif value == "Hunger":
            output = output + ("You've been walking for to long, you need some food!!")
            status[1] = status[1] - 1
        elif value == "Weather":
            output = output + ("Maryland weather :/ it started raining")
            status[1] = status[1] - 1
        elif value == "Bus":
            output = output + ("BOOM \n You got hit by a bus")
            running = False
        else:
            output = output + ("hmmmm nevermind. \nYou avoided a random obstacle!")
        
        status[3] = output
        return(status)

    def stop4(status):
        interview = easygui.enterbox("What do you think (y/n): ")
        if interview.lower() == "y":
            output = "You're going to be the face of nexts week's issue! You gained smart points!"
            status[2] = status[2] + 1
            time = +3
        elif interview.lower() == "n":
            output = "You could have been a star. You lost smart points."
            status[2] = status[2] - 1
            time = +1
        else:
            stop4(status)

        status[3] = output
        return(status)

    def play_again(status):
        again = easygui.enterbox("Start Over? (y/n): ")
        if again.lower() == "y":
            output= "Here we go again!"
        elif again.lower() == "n":
            output = "We hope you've enjoyed your journey!"
        else: 
            play_again()

        status[3] = output
        return(status)

    # Game Loop
    running = True
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        ### Screen contents ###
        
        # Showing most recent updated text; if new, is blank

        resetPlayScreen(background)

        blit_text(SCREEN, status[3], (150, 375), font)

        if status[3] == "": # beginning of game
            status[3] = "Welcome to the University of Maryland... where the construction is never ending and the sidewalks are always full."
            blit_text(SCREEN, status[3], (150, 375), font)

        PLAY_NEXT = Button(image=None, pos=(300, 660), 
                            text_input="NEXT", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_NEXT.changeColor(PLAY_MOUSE_POS)
        PLAY_NEXT.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(1140, 660), 
                            text_input="MENU", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_NEXT.checkForInput(PLAY_MOUSE_POS):
                    if status[3] == "Welcome to the University of Maryland... where the construction is never ending and the sidewalks are always full.":
                        player_name = naming()
                        status[3] = "Nice to meet you " + player_name + ", have fun on your journey"
                    elif status[3] == "Nice to meet you " + player_name + ", have fun on your journey":
                        status[3] = introText
                    elif status[3] == introText:
                        major = intro()
                        status[3] = "Your major is " + major + ". Good luck! You'll need it"
                        if major == "CompSci":
                            status[1] = 1
                            status[2] = 3
                        elif major == "Bio":
                            status[1] = 1
                            status[2] = 2
                        elif major == "Business":
                            status[1] = 3
                            status[2] = 1
                        else:
                            status[1] = 2
                            status[2] = 2
                    elif status[3] == "Your major is " + major + ". Good luck! You'll need it":
                        obstacle1 = random1(status)
                        status = obstacle1
                        status[3] = status[3] + " First problem of the day!"
                        background = 'umd_walk.jpg'
                    elif status[3] == obstacle1[3] + " First problem of the day!":
                        status[3] = hensonText
                        background = 'henson.jpg'
                    elif status[3] == hensonText:
                        stop1Answer = stop1(status)
                        status = stop1Answer
                    elif status[3] == stop1Answer[3]:
                        status[3] = darryllText
                        background = 'theY.jpg'
                    elif status[3] == darryllText:
                        stop2Answer = stop2(status)
                        status[3] = stop2Answer
                    elif status[3] == stop2Answer:
                        obstacle2 = random1(status)
                        status[3] = obstacle2 + " Second problem of the day!"
                        background = 'umd_walk.jpg'
                    elif status[3] == obstacle2 + " Second problem of the day!":
                        status[3] = clariceText
                        background = 'clarice.jpg'
                    elif status[3] == clariceText:
                        stop3Answer = stop3(status)
                        status[3] = stop3Answer
                    elif status[3] == stop3Answer:
                        obstacle3 = random2(status)
                        status[3] = obstacle3
                        background = 'umd_walk.jpg'
                    elif status[3] == obstacle3:
                        status[3] = journalismText
                        background = 'journalism.jpg'
                    elif status[3] == journalismText:
                        stop4Answer = stop4(status)
                        status[3] = stop4Answer
                    elif status[3] == stop4Answer:
                        status[3] = endText
                        background = 'stamp.jpg'
                    elif status[3] == endText:
                        repeat = play_again(status)
                        status[3] = repeat
                    elif status[3] == "Here we go again!":
                        status = [10, 0, 0, ""]
                        background = 'UMD_aerial.jpg'
                    elif status[3] == "We hope you've enjoyed your journey!":
                        main_menu()
                    else:
                        status[3] == "Woops, something went wrong! Plz reload and try again"
                    
        pygame.display.update()

    # If running is false, return to menu
    main_menu()


def main_menu():
    while True:
        SCREEN.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TERP TRAIL", True, "#FF0000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        START_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="START", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 400), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
