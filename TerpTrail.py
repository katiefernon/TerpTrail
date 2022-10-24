
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
    text = ""
    background = 'UMD_aerial.jpg'
    hp = 10
    stamina = 0
    smarts = 0
    introText = "Welcome to Terp Trail! Your goal is to climb Stamp hill. Think you have what it takes?\n \
        Time to choose a major! You have a long journey ahead, choose wisely!\n \
            These are your major options\n \
            1. CompSci: HP = 2, Stamina = 1, Smarts = 3\n \
            2. Bio: HP = 3, Stamina = 1, Smarts = 2\n \
            3. Business: HP = 2, Stamina = 3, Smarts = 1\n \
            4. Psych: HP = 2, Stamina = 2, Smarts = 2\n \
                Select 'Next' to choose a major."
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

    def random1(hp): #deal out hit to hp for stop 1
    #rocks = random.choices([1,2], weights = [4, 1])[0]
    #print("uh oh, looks like") # a dialogue for the random occurance
    
        instances = ["Rock", "Pothole", "Squirrel", "Veo", "Blank"]
    
        value = random.choice(instances)
        output = "Uh oh...\n" # a dialogue for the random occurance
                                        #substract healthpoints on the backend
        if value == "Rock":
            output = output + ("Oops you tripped over some Rocks. You lost some HP!")
            hp = hp - 1
        elif value == "Pothole":
            output = output + ("Dang, you fell in an pothole. You lost some HP!")
            hp = hp - 1
        elif value == "Squirrel":
            output = output + ("S to the I to M to the P, there's squirrels in your pants! You lost some HP!")
            hp = hp - 2
        elif value == "Veo":
            output = output + ("Watch where you're going... \n YOU GOT RUN OVER BY A VEO!! You lost some HP!")
            hp = hp - 2
        else:
            output = output + ("hmmmm nevermind. \nYou avoided a random obstacle!")
        
        return(output)

    def stop1(smarts):
        question = easygui.enterbox("Type Answer Here (numbers only): ")
        if  question == "19":
            output = "CORRECT: Smart lad, you may continue. \nYou have gained smart points!"
            smarts = smarts + 2
        
        elif question == "21":
            output = "Haha, you're funny, I will let you go just this once. \nYou have gained smart points!"
            smarts = smarts + 1
        
        elif question == "910":
            output = "WRONG: I think you should change your major.\nYou have lost smart points!"
            smarts = smarts - 2
        
        elif question == "9.10":
            output = "WRONG: Are you even trying?\nYou have lost smart points!"
            smarts = smarts - 2
        
        else:
            print("That was not one of the choices. Guess again")
            stop1(smarts)
        
        return(output)

    def stop2(stamina):
        picture = easygui.enterbox("Do you want to take the selfie (y/n): ")
        if picture.lower() == "y":
            output = "Darryll Pines: Great, smile for the camera\nYou have gained stamina points!"
            stamina = stamina + 1
            time = +2
        elif picture.lower() == "n":
            output = "Darryll Pines: I understand, you're a busy person. Maybe next time"
            time = +1
        else:
            stop2(stamina)

        return(output)

    def stop3(smarts):
        school = easygui.enterbox("What do you think? (y/n): ")
        if school.lower() == "n":
            output = 'Oh, you really know your stuff. \nYou have gained smart points!'
            smarts = smarts + 1
            time = +1
        elif school.lower() == "y":
            output = "Wrong: That was a tricky question. Better luck next time. \nYou have lost smart points."
            smarts = smarts - 1
            time = +3
        else:
            stop3(smarts)
        
        return(output)

    def random2(smarts, stamina):
        instances = ["Homework", "Hunger", "Weather", "Bus", "Blank"]
    
        value = random.choice(instances)
        output = "Uh oh...\n" # a dialogue for the random occurance
                                        #substract healthpoints on the backend
        if value == "Homework":
            output = output + ("You just remembered you had homework due")
            smarts = smarts - 1
        elif value == "Hunger":
            output = output + ("You've been walking for to long, you need some food!!")
            stamina = stamina - 1
        elif value == "Weather":
            output = output + ("Maryland weather :/ it started raining")
            stamina = stamina - 1
        elif value == "Bus":
            output = output + ("BOOM \n You got hit by a bus")
            running = False
        else:
            output = output + ("hmmmm nevermind. \nYou avoided a random obstacle!")
        
        return(output)

    def stop4(smarts):
        interview = easygui.enterbox("What do you think (y/n): ")
        if interview.lower() == "y":
            output = "You're going to be the face of nexts week's issue! You gained smart points!"
            smarts = smarts + 1
            time = +3
        elif interview.lower() == "n":
            output = "You could have been a star. You lost smart points."
            smarts = smarts - 1
            time = +1
        else:
            stop4(smarts)

        return(output)

    def play_again():
        again = easygui.enterbox("Start Over? (y/n): ")
        if again.lower() == "y":
            output= "Here we go again!"
        elif again.lower() == "n":
            output = "We hope you've enjoyed your journey!"
        else: 
            play_again()

        return(output)

    # Game Loop
    running = True
    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        ### Screen contents ###
        
        # Showing most recent updated text; if new, is blank

        resetPlayScreen(background)

        blit_text(SCREEN, text, (150, 375), font)

        if text == "": # beginning of game
            text = "Welcome to the University of Maryland... where the construction is never ending and the sidewalks are always full."
            blit_text(SCREEN, text, (150, 375), font)

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
                    if text == "Welcome to the University of Maryland... where the construction is never ending and the sidewalks are always full.":
                        player_name = naming()
                        text = "Nice to meet you " + player_name + ", have fun on your journey"
                    elif text == "Nice to meet you " + player_name + ", have fun on your journey":
                        text = introText
                    elif text == introText:
                        major = intro()
                        text = "Your major is " + major + ". Good luck! You'll need it"
                        if major == "CompSci":
                            stamina = 1
                            smarts = 3
                        elif major == "Bio":
                            stamina = 1
                            smarts = 2
                        elif major == "Business":
                            stamina = 3
                            smarts = 1
                        else:
                            stamina = 2
                            smarts = 2
                    elif text == "Your major is " + major + ". Good luck! You'll need it":
                        obstacle1 = random1(hp)
                        text = obstacle1 + " First problem of the day!"
                        background = 'umd_walk.jpg'
                    elif text == obstacle1 + " First problem of the day!":
                        text = hensonText
                        background = 'henson.jpg'
                    elif text == hensonText:
                        stop1Answer = stop1(smarts)
                        text = stop1Answer
                    elif text == stop1Answer:
                        text = darryllText
                        background = 'theY.jpg'
                    elif text == darryllText:
                        stop2Answer = stop2(stamina)
                        text = stop2Answer
                    elif text == stop2Answer:
                        obstacle2 = random1(hp)
                        text = obstacle2 + " Second problem of the day!"
                        background = 'umd_walk.jpg'
                    elif text == obstacle2 + " Second problem of the day!":
                        text = clariceText
                        background = 'clarice.jpg'
                    elif text == clariceText:
                        stop3Answer = stop3(smarts)
                        text = stop3Answer
                    elif text == stop3Answer:
                        obstacle3 = random2(smarts, stamina)
                        text = obstacle3
                        background = 'umd_walk.jpg'
                    elif text == obstacle3:
                        text = journalismText
                        background = 'journalism.jpg'
                    elif text == journalismText:
                        stop4Answer = stop4(smarts)
                        text = stop4Answer
                    elif text == stop4Answer:
                        text = endText
                        background = 'stamp.jpg'
                    elif text == endText:
                        repeat = play_again()
                        text = repeat
                    elif text == "Here we go again!":
                        text = ""
                        background = 'UMD_aerial.jpg'
                    elif text == "We hope you've enjoyed your journey!":
                        main_menu()
                    else:
                        text == "Woops, something went wrong! Plz reload and try again"
                    
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
