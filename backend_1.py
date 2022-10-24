#welcome the people to umd
print("--------------------\nWelcome to the University of Maryland.\
 Where the contruction is never ending and the..[think of something funny] ")


#IMPORTANT
pstats = []
timer = 0
import random as ran


#input player name
def naming():
    player_name = input('What is your name Terp (limit 12 characters)?: ')
    while len(player_name) >= 0: #making a name longer than 2 letters
        if len(player_name) > 2:
            print(str(f'Nice to meet you {player_name}, have fun on your journey\n'))
            pstats.append(player_name)
            intro()
        break
    

    if len(player_name) == 12:
        new_name = input(str(player_name)+"ohhh uhh too long, try again?(y/n): ")
        if new_name.lower() == "y":
            print("Well if it's on your birth certificate, pop off then")
            pstats.append(player_name)
            intro()
        
        elif new_name.lower() == "n":
            naming()
    
        else:
            print("You do not type anything, try again")
            naming()

print('Welcome to Terp Trail. Your objective is to climb Stamp Hill. Think\
 you have what it takes?')


#choose major
# return major a number
def intro():
    print('What is your major, you have a long jounrey ahead. Choose wisely!') 
    
#wouldnt I have to print the stats for the majors, so the player can see?
    print('These are your major options')
    print('1. Computer Science: hp = 2 \n stamina = 1 \n smarts = 3')     
    print('2. Biology: hp = 3 \n stamina = 1 \n smarts = 2') 
    print('3. Buisness: hp = 2 \n stamina = 3 \n smarts = 1') 
    print('4. Psychology: hp = 2 \n stamina = 2 \n smarts = 2') 
  
    major_s = [
        ['compsci'],
        ['bio'],
        ['psych'],
        ['business']
    ]
    
    choose_your_major = int(input("Enter Major as a number: "))
    try:
        print(f'Your major is {(major_s[(choose_your_major - 1)])}. Good luck! You\'ll need it!')
    except (ValueError):
        print("You did not enter an integer, try again")
        intro()

    majorstats(int(choose_your_major))

def majorstats (n):
    #calls intro function that returns number that correlates to stats
    major_stats = [
        ['compsci', 2, 1, 3],
        ['bio', 3, 1, 2],
        ['psych', 2, 2, 2],
        ['business',2, 3, 1]
    ]
    #major, hp, stamina, intelligence = major_stats[n]
    for i in major_stats[n-1]:
        pstats.append(i)
    print(pstats)

naming()


def random1(): #deal out hit to hp for stop 1
    #rocks = random.choices([1,2], weights = [4, 1])[0]
    #print("uh oh, looks like") # a dialogue for the random occurance
    
    instances = ["Rock", "Pothole","Squirrel", "Veo", "Blank"]
    value = ran.choice(instances)
    print(f"Uh oh,") # a dialogue for the random occurance
                                        #substract healthpoints on the backend
    if value == "Rock":
        print ("Opps you tripped over some Rocks")
        print("You've lost some HP and Stamina. ")
        stamina = -0.25
        pstats[1] = pstats[1] - 0.25
        pstats[2] = pstats[2] - stamina
        
    elif value == "Pothole":
        print("Dang you fell in an pothole")
        print("You've lost some HP and Stamina")
        stamina = -0.25
        pstats[1] = pstats[1] - 0.25
        pstats[2] = pstats[2] - stamina
       
        
    elif value == "Squirrel":
        print("S to the I to M to the P, theres squirrels in your pants")
        print("You've lost some HP and Stamina")
        stamina = -0.50
        pstats[1] = pstats[1] - 0.25
        pstats[2] = pstats[2] - stamina
       
        
        
    elif value == "Veo":
        print("Watch were your going \n YOU GOT RUN OVER BY A VEO!!")
        print("You've lost some HP")
        stamina = -0.75
        pstats[2] = pstats[2] + stamina
        
        #get run over by veo = -0.75
    else:
        print("Hmmmm Nvm")
random1()
timer += 1
print(f'Your current stats are: {pstats}')
 
#diaoluge_2 for screen  
print('You make your way to the CompSci building.\
        \n You bump into a old classmate, Jim Henson.\
        \n Jim Henson: Hello friend, long time.\n Whats 9 + 10?')
print('Here are your choices. \n 19 \n 21 \n 910 \n 9.10')

def stop1(): #for stop three
    question = input("Type Answer Here(numbers only): ")
    if  question == "19":
        print("CORRECT: Smart lad, you may continue")
        
    elif question == "21":
        print("Haha, your funny, I will let you go just this once")
         
    elif question == "910":
        print("WRONG: I think you should change your major")
        
    elif question == "9.10":
        print("WRONG: Are you even trying")
        
    else:
        print("That was not one of the choices. Guess again")
        stop1()
timer += 1
stop1()

#diaoluge_3 for screen
print ("You have made it to the newest dining hall on campus. Looks who's here\
President Darryll Pines")
print("Darryll Pines: Hello Terp. I hope you are loving your time at UMD\
We have recently opened a new dining hall\
    \n The new dining hall is named to honor the Piscataway,\
who are indigenous to Maryland.\
    \n Yahentamitsi means “a place to go eat” in the Piscataway people’s\
spoken Algonquian language.\
    \nLets take a selfie together to commemorate the opening of Yahentamitsi ")
 
 #talking to President Pines   
def stop2():
    picture = input("Do you want to take the selfie (y/n): ")
    if picture == "y":
        print('Darryll Pines: Great, smile for the camera')
        stamina = 1
        pstats[2] = pstats[2] + stamina
        check_stamina(stamina)

    elif picture == "n":
        print('Darryll Pines: I understand, you\'re a busy person. Maybe next time')
        stamina = 1
        pstats[2] = pstats[2] - 1
        check_stamina(stamina)
        
    else:
        print('Invalid Answer: Please try again')
        stop2()
stop2()
timer += 1

random1() #throw in another random occuracne


 #diaoluge_4 for screen   
print("You have made it to The Clarice Smith Performing Arts Center")
def random2(): #more random stuff
    
    instances2 = ["Homework", "Hunger","Weather", "Bus", "Blank"]
    
    value2 = ran.choice(instances2)
    print(f"Uh oh,") 
    if value2 == "Homework":
        print ("You just remembered you had homework due")
        ("You've lost some Smarts")
        smarts = -1
        pstats[-1] = pstats[-1] + smarts

        
    elif value2 == "Hunger":
        print("You've been walking for to long, you need some food!!")
        ("You've lost some Stamina")
        stamina = -1
        pstats[2] = pstats[2] + stamina
        
    elif value2 == "Weather":
        print("Maryland weather :/ it started raining")
        ("You've lost some Stamina")
        stamina = -0.5
        pstats[2] = pstats[2] + stamina
        
    elif value2 == "BUS":
        print("BOOM \n You got hit by a bus")
        print("You might be dead??")
        hp = -1
        pstats[1] = pstats[1] + hp
        if hp <= 0:
            print('You died get, not everyone can survive UMD')
            print('End')
            quit()


    else:
        print("hmm did you hear something")
        
    return(value2)
random2()
timer += 1
print("It's time for a Pop Quiz, Lets see if you know your stuff")
print("Is the Clarice one of the 12 'SCHOOLS' under UMD?" )


def stop3(): 
    school = input("What do you think (y/n): ")
    
    if school == "n":
        print('Oh you really know your stuff')
        stamina = +1
        pstats[2] = pstats[2] + stamina
        
        
    elif school == "y":
        print("Wrong: That was a tricky question. Better luck next time")
        stamina = -1
        pstats[2] = pstats[2] + stamina
    else:
        print('Invalid Answer: Please try again')
        stop3()
stop3()
timer += 1

random2() #more random stuff
timer += 1
 

#diaoluge_5 for screen  
print("You have wandered down to the Journalism Building") 
print("Random Student: Welcome to the Journalism Building, home of The Diamondback\
    \n Thank you for joining us. Would you like to be in an interview for next weeks paper.\
    \n What do you say?")

def stop4():
    interview = input("What do you think (y/n): ")
    if interview == "y":
        print('Your going to be the face of nexts weeks issue')
        smarts = +1
        pstats[-1] = pstats[-1] + smarts

    elif interview == "n":
        print("You could have been a star")
        smarts = -1
        pstats[-1] = pstats[-1] + smarts
        
    else:
        print('Invalid Answer: Please try again')
        stop4()
stop4()
timer += 1

random1()

#diaoluge_6 for screen  
print("You have have FINALLY made it to STAMP. You can now enjoy some Chick-fil-a")
print("This has been the end of Terp Trail")
print("Would you like to play again")

def play_again():
    again = input("Start Over? (y/n): ")
    if again == "y":
        print('Here we go again')
        
       
    else:
        print("hope you enjoyed your journey")
play_again()

 
def check_stamina(n):
    if n> 0:
        pass
    else:
        print('You need to rest! Resting takes off 3 hours.')
        timer += 3
    