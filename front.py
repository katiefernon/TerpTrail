import random   #this is for the random occurances that happen at each stop
import time     #this is for adding time delays

#setting values to stats
#def stats(hp, smarts, stamina, time):
hp = 0
smarts = 0
stamina = 0
time = 0

#welcome the people to umd
print("Welcome to the University of Maryland.\
 Where the contruction is never ending and the..[think of something funny] ")

#input player name
#give it a paramater that can be called in other functions   
player_name = input('What is your name Terp (limit 12 characters)?: ')
while len(player_name) >= 0: #making sure name longer than 2 letters
    if len(player_name) > 2:
        print(str(f'Nice to meet you {player_name}, have fun on your journey'))
        
        break
    
    if len(player_name) <= 1: 
        new_name = input(str(player_name)+ "is too short of a name, try again?(y/n): ")
        
        if new_name.lower() == "n":
            print("Well if its on your birth certificate, pop of than")
        
        elif new_name.lower() == "y":
            new_name = input(str(player_name)+ "is too short of a name, try again?(y/n): ")
    
        else:
            print("You do not type anything, try again") 
            
        print(player_name)


#diaoluge_1 for home screen
print('Welcome to Terp Trail. Your objective is to climb Stamp Hill.\
    \n Think you have what it takes?')
print('What is your major, you have a long jounrey ahead. Choose wisely!') 
    

#gives you your major options
print('These are your major options')#everything is out of 6
print('1. CompSci: HP = 2\n Stamina = 1\n Smarts = 3')    
print('2. Bio: HP = 3\n Stamina = 1\n Smarts = 2')
print('3. Business: HP = 2\n Stamina = 3\n Smarts = 1')
print('4. Pych: HP = 2 \n Stamina = 2\n Smarts = 2')

#choose major  
choose_your_major = input("Enter Major (Case Sensitive): ")
if choose_your_major == "CompSci":
    hp = 2
    stamina = 1
    smarts = 3
    print(f'Your major is Compsci. Good luck! Youll need it')    
elif choose_your_major == "Bio":
    hp = 3
    stamina = 1
    smarts = 2
    print(f'Your major is Bio. Good luck! Youll need it')     
elif choose_your_major == "Business":
    hp = 2
    stamina = 3
    smarts = 1
    print(f'Your major is Business. Good luck! Youll need it')
elif choose_your_major == "Pych":
    hp = 2
    stamina = 2
    smarts = 2
    print(f'Your major is Pych. Good luck! Youll need it')
else: #edge case
    print('Invaild Major. Try Again')
    choose_your_major = input("Enter Major (Case Sensitive): ")
print(choose_your_major)  


def random1(): #deal out hit to hp for stop 1
    #rocks = random.choices([1,2], weights = [4, 1])[0]
    #print("uh oh, looks like") # a dialogue for the random occurance
    
    instances = ["Rock", "Pothole","Squirrel", "Veo", "Blank"]
    
    value = random.choice(instances)
    print(f"Uh oh,") # a dialogue for the random occurance
                                        #substract healthpoints on the backend
    if value == "Rock":
        print ("Opps you tripped over some Rocks")
        print("You've lost some HP.")
        time =+ 1
        hp =-1
        #tripping over rocks = -0.25
         
    elif value == "Pothole":
        print("Dang you fell in an pothole")
        print("You've lost some HP")
        time =+ 1
        hp =- 1
        #rolling ankel on pothole = -0.25
        
    elif value == "Squirrel":
        print("S to the I to M to the P, theres squirrels in your pants")
        ("You've lost some HP")
        time =+ 1
        hp =- 1
        #squirrels attacked you = -0.5
        
    elif value == "Veo":
        print("Watch were your going \n YOU GOT RUN OVER BY A VEO!!")
        ("You've lost some HP")
        time =+ 1
        hp =- 1
        #get run over by veo = -0.75
    else:
        print("Hmmmm Nvm")
        
    return(value)
random1()

#diaoluge_2 for screen  
print('You make your way to the CompSci building.\
        \n You bump into a old classmate, Jim Henson.\
        \n Jim Henson: Hello friend, long time.\n Whats 9 + 10?')
print('Here are your choices. \n 19 \n 21 \n 910 \n 9.10')

#stop1: CompSci Building
question = input("Type Answer Here(numbers only): ")
if  question == "19":
    print("CORRECT: Smart lad, you may continue")
    smarts =+ 2
    time =+ 2
elif question == "21":
    print("Haha, your funny, I will let you go just this once")
    smarts =+ 1
    time =+ 2
elif question == "910":
    print("WRONG: I think you should change your major")
    smarts =- 1
    time =+ 2
elif question == "9.10":
    print("WRONG: Are you even trying")
    smarts =- 1
    time =+ 2
else:
    print("That was not one of the choices. Guess again")
    question = input("Type Answer Here(numbers only): ")
    


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
 
 #Stop2:Yahentamitsi, quest talk to President Pines   

picture = input("Do you want to take the selfie (y/n): ")
if picture == "y":
    print('Darryll Pines: Great, smile for the camera')
    stamina = +1
    time = +3
elif picture == "n":
    print('Darryll Pines: I understand, your a busy person. Maybe next time')
    time = +1
else:
    print('Invalid Answer: Please try again')
    picture = input("Do you want to take the selfie (y/n): ")


random1() #throw in another random occuracne


#diaoluge_4 for screen   
print("You have made it to The Clarice Smith Performing Arts Center")


def random2(): #a second random occurance that might
    print("Uh oh, looks like") 
    instances2 = ["Homework", "Hunger","Weather", "Bus", "Blank"]

    value2 = random.choice(instances2)
    if value2 == "Homework":
        print ("You just remembered you had homework due")
        print("You've lost some Smarts")
        smarts = -1
        time =+ 1
        
    elif value2 == "Hunger":
        print("You've been walking for to long, you need some food!!")
        print("You've lost some Stamina")
        stamina = -1
        time =+ 1
        
    elif value2 == "Weather":
        print("Maryland weather :/ it started raining")
        print("You've lost some Stamina")
        stamina = -0.5
        time =+ 1
        
    elif value2 == "BUS":
        print("BOOM \n You got hit by a bus")
        print("You might be dead??")
        hp = -100
        time =+ 10
    else:
        print("Hmm, must have been the wind")
        
    return(value2)
random2()


print("It's time for a Pop Quiz, Lets see if you know your stuff")
print("Is the Clarice one of the 12 'SCHOOLS' under UMD?" )


#stop3: Clarice pop quiz
school = input("What do you think (y/n): ")
if school == "n":
    print('Oh you really know your stuff')
    stamina =+ 0.25
    smarts =+ 0.5
    time =+ 3
elif school == "y":
        print("Wrong: That was a tricky question. Better luck next time")
        stamina = -1
        time = +3
else:
    print('Invalid Answer: Please try again')
    school = input("What do you think (y/n): ")

random2() #call the random occurance function
 

#diaoluge_5 for screen  
print("You have wandered down to the Journalism Building") 
print("Random Student: Welcome to the Journalism Building, home of The Diamondback\
    \n Thank you for joining us. Would you like to be in an interview for next weeks paper.\
    \n What do you say?")

#stop4: Journalism Building

interview = input("What do you think (y/n): ")
if interview == "y":
    print('Your going to be the face of nexts weeks issue')
    print("You've gained some Smarts")
    smarts = +1
    time = +3
elif interview == "n":
    print("You could have been a star")
    print("You've lost some Smarts")
    smarts = -1
    time = +1
else:
    print('Invalid Answer: Please try again')
    interview = input("What do you think (y/n): ")
    
random1() #call another random

#diaoluge_6 for screen  
print("You have have FINALLY made it to STAMP. You can now enjoy some Chick-fil-a")
print("This has been the end of Terp Trail")


print('You ended the game with:')
print(f'{hp} hp')
if hp <= 0:
  print('Game over, your dead')
else:
    print('You didnt die, good job')
    
print(f'{smarts} smarts')
if smarts <= 0:
  print('Game over, your dumb.')
else:
    print("Smartie Pants")

print(f'{stamina} stamina')
if stamina >= 3:
  print('Game over, your to slow')
else:
    print("Your a runner your a track star")

print("Would you like to play again")

def play_again():
    again = input("Start Over? (y/n): ")
    if again == "y":
        print('Here we go again')
        print("PLEASE RECONSIDER")
    else:
        print("hope you enjoyed your journey")
play_again()       
    
