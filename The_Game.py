def play_escape_the_black_hole(sound=True):
    #if they want to play with sound(default)
    if sound==True:
        #deletes all variables so that if statement works properly
        from IPython.display import Image
        from IPython.display import clear_output
        from time import sleep #this function is used occasionally when things don't output in the correct order
        from module import Wave
        from module import Freq
        from module import Frequency
        from module import Wave2
        from module import Wavefile
        import numpy as np
        from module import winsound
        tarray = np.arange(0,1,0.0001)
        yarray = 11*np.sin(2*np.pi*tarray*1000)+12*np.sin(2*np.pi*tarray*200)
        tsmall = np.arange(0,1,0.0001)
        ysmall = 11*np.sin(2*np.pi*tsmall*1000)


        game_start = True #you want the game to start initially


        #these parameters are used so that if the give an invalid input, the question repeats (false means unanswered)
        question_1 = False
        question_2 = False
        question_3 = False
        question_4 = False
        question_5 = False
        question_6 = False
        question_7 = False
        question_8 = False
        freq_question = False
        win = False #you have not won yet
        alive = True #you are alive to start the game

        while game_start == True:
            while alive == True:
                print('You wake up on a ship. You look around and notice it\'s pitch black aside from a small emergency light shining on a control panel. Do you check it out?')
                sleep(0.2)
                while question_1 == False: #while question 1 hasn't been answered
                    check_light = input('Yes or No? ')
                    if check_light == 'Yes' or check_light == 'yes' or check_light == 'y' or check_light == 'Y': #if they say yes
                        question_1 = True #answered question 1
                        check_light = True #they did check the lights
                        continue
                    elif check_light == 'No' or check_light == 'no' or check_light == 'n' or check_light == 'N': #if they say no
                        question_1 = True #answered question 1
                        check_light = False #they did not check the lights
                        continue
                    else:
                        print('Invalid input, please try again.')

                while question_2 == False: #while question 2 hasn't been answered
                    if check_light == False: #if you did not check the light
                        print('You happen to find a flashlight and begin roaming the ship. You suddenly feel some turbulence and emergency alarms begin to sound. Do you return to the control panel to see whats wrong?')
                        curiosity = input('Yes or No? ')
                        if curiosity == 'Yes' or curiosity == 'yes' or curiosity == 'y' or curiosity == 'Y':
                            question_2 = True
                            continue
                        elif curiosity == 'No' or curiosity == 'no' or curiosity == 'n' or curiosity == 'N':
                            question_2 == True
                            print('You have no idea what is wrong and now you begin to hear creaking on one side of the ship. You feel some weird force on your body and you feel queasy. Suddenly you hear a loud crash for a fraction of a second, then immediate silence: one side of your ship has been ripped apart from the rest and you are now subject to the black hole that you were oblivious to until that very moment.')
                            print('Displaying Ships Trajectory...')
                            with open('do_nothing.gif','rb') as file:
                                display(Image(file.read()))
                            alive = False #you died
                            break
                        else:
                            print('Invalid input, please try again.')
                    if check_light == True:
                        question_2 = True #no need for second question
                        continue
                if alive == False: #if you die, you stop playing
                    break

                print('You are at the control panel. You see a master switch to turn on the lights. After switching them on you notice your ship is trapped in an orbit around an immense stellar mass. Do you attempt to escape the orbit?')
                while question_3 == False:    
                    try_to_escape = input('Yes or No? ')
                    if try_to_escape == 'Yes' or try_to_escape == 'yes' or try_to_escape == 'y' or try_to_escape == 'Y':
                        question_3 = True
                        continue
                    elif try_to_escape == 'No' or try_to_escape == 'no' or try_to_escape == 'n' or try_to_escape == 'N':
                        question_3 = True
                        print('As you ship tumbles closer to the black hole, the immense force ejects you from your ship and you begin the process of spaghetification headfirst.')
                        print('Displaying Ships Trajectory...')
                        with open('do_nothing.gif','rb') as file:
                            display(Image(file.read()))
                        alive = False #you died
                        break
                    else:
                        print('Invalid input, please try again.')

                if alive == False: #if you die, you stop playing
                    break

                print('You now have one chance to alter the ship\'s thrusters to escape the stellar mass which you now know is a black hole after looking out the window and seeing pitch black. What speed do you choose to attempt to escape?')
                while question_4 == False:
                    esc_vel = input('(1) 1.016c\n(2) 0.992c\n(3) 0.985c\n(4) 0.973c?\n')
                    if esc_vel == '1' or esc_vel == '1.016c' or esc_vel == '1 ' or esc_vel == '(1) 1.016c':
                        question_4 = True
                        print('You have attempted to violate the laws of physics - for this, you die.')
                        print('We are very dissapointed in you, you should have known better.')
                        alive = False
                        break
                    elif esc_vel == '2' or esc_vel=='0.992c' or esc_vel == '2 ' or esc_vel == '(2) 0.992c':
                        question_4 = True
                        continue #you do not die and move on
                    elif esc_vel == '3' or esc_vel=='0.985c' or esc_vel == '3 ' or esc_vel == '(3) 0.985c':
                        question_4 = True
                        print('While you were traveling extremely fast, it was not enough to escape the tremendous pull of the black hole. You and your ship get pulled into the black hole as you are slowly spaghettified.')
                        with open('black_hole_985.gif','rb') as file:
                           display(Image(file.read()))
                        alive = False
                        break
                    elif esc_vel == '4' or esc_vel=='0.973c' or esc_vel == '4 ' or esc_vel == '(4) 0.973c':
                        question_4 = True
                        print('While you were traveling extremely fast, it was not enough to escape the tremendous pull of the black hole. You and your ship get pulled into the black hole as you are slowly spaghettified.')
                        with open('black_hole_973.gif','rb') as file:
                           display(Image(file.read()))
                        alive = False
                        break
                    else:
                        print('Invalid input, please try again.')
                if alive == False: #if you die, you stop playing
                    break

                print('You speed away from the black hole to safety.')
                with open('black_hole_992.gif','rb') as file:
                            display(Image(file.read()))
                sleep(0.5)
                print('You can now roam the ship freely without a worry. Would you like to visit the lab or go to sleep?')
                sleep(0.5)

                while question_5 == False:
                    activity = input('(1) Explore the Lab\n(2) Go to Sleep\n')
                    if activity == '1' or activity == 'lab' or activity == 'Lab' or activity == '1 ':
                        question_5 = True
                        continue
                    elif activity == '2' or activity == '2 ' or activity=='sleep' or activity=='Sleep':
                        question_5 = True
                        print('You go to sleep, and when you wake up you are on an alien spaceship. They intersected your ship while you were sleeping.')
                        with open('alien_intersect.gif','rb') as file:
                            display(Image(file.read()))
                            sleep(2)
                        print('You feel as if you are under the influence of a drug you have never experienced and you\'re unable to understand the aliens speaking about what they are going to do to you. You do not last long on the alien ship and no human will ever see you again.')
                        alive = False
                        break
                    else:
                        print('Invalid input, please try again.')

                if alive == False: #if you die, you stop playing
                    break


                print('You go to the lab and begin measuring the frequency of AC current from a signal generator. You attempt to take the Fourier transform of the signal in order to determine if there is any noise aside from the frequency you expect, which was supposed to be '+str(Freq(tarray,yarray))+' Hz.')
                print('The actual signal you are receving looks like this:')
                Wave(tarray,yarray)
                sleep(.8)
                print('It appreas there is a prominent peak that you were not expecting.')
                while freq_question == False:
                    analyze_freq = input('What is the frequency you were not expecting (without units)? ')
                    if analyze_freq.isnumeric() == True:
                        if np.double(analyze_freq) >995 and np.double(analyze_freq) < 1005:
                            freq_question=True
                            continue
                        elif np.double(analyze_freq) > 195 and np.double(analyze_freq) < 205:
                            print('This is the frequency you were expecting, try again.')
                        else:
                            print('You are not detecting a signal at this frequency, please try again.')
                    else:
                        print('Invalid input, please try again.')

                print('You sigle out the unexpected frequency and find')
                Wave2(tsmall,ysmall)
                print(Freq(tsmall,ysmall),'Hz')
                print('Do you attempt to send the same signal back into space using your own function generator and oscilloscope?')#from text file
                sleep(0.8)
                while question_6 == False:
                    send_freq = input('Yes or No? ')
                    if send_freq == 'Yes' or send_freq=='yes' or send_freq=='y' or send_freq=='Y':
                        question_6=True
                        print(Frequency('1000Hz.txt'),'Hz')
                        Wavefile('1000Hz.txt')
                        print('After sending the signal back into space you look out the window and notice a light some distance away that appears to be approaching you. Do you go to the control room and attempt to change your trajectory, or do you stay where you are?')
                        while question_7 == False:
                            stay_or_leave = input('(1) Stay\n(2) Leave\n')
                            if stay_or_leave=='1'or stay_or_leave=='Stay' or stay_or_leave=='1 'or stay_or_leave=='stay':
                                question_7=True
                                print('As the object gets closer you see it is an alien ship, at which point you are no longer able to speed away in any direction, you are trapped in a tractor beam. You see a sudden flash of light and you are immediately unconscious. When you wake up, you are on an alien spaceship and you feel as if you are under the influence of a drug you have never experienced, and you are unable to understand the aliens speaking about what they are going to do to you. You do not last long on the alien ship. No human will ever see you again.')
                                alive=False
                                with open('alien_intersect.gif','rb') as file:
                                    display(Image(file.read())) # captured
                                break
                            elif stay_or_leave=='2'or stay_or_leave=='Leave' or stay_or_leave=='2 'or stay_or_leave=='leave':
                                question_7=True
                                print('You avoid what you believed to be a hostile situation and you played it safe.')
                                with open('alien_escape.gif','rb') as file:
                                    display(Image(file.read()))  # Escape  
                                continue
                            else:
                                print('Invalid input, please try again.')
                    elif send_freq == 'No' or send_freq=='no' or send_freq=='N' or send_freq=='n':
                        question_6=True
                        print('You decided not to send the mysterious signal back into space. This was the correct choice, you have survived by escaping the black hole and the hostile aliens. Great Job!')
                        break
                    else:
                        print('Invalid input, please try again.')


                if alive == False: #if you die, you stop playing
                    break

                print('You are free to continue exploring space on your own time. You realize you\'re barreling through space at 0.992c and are still traversing light years in what feels like fermiseconds. You have been busy working and did not realize where you are now. You zoomed by a binary black hole system: OJ 287, but were not going fast enough. The strength of both massive black holes is pulling you towards them. It turns out the aliens you escaped earlier are hot on your tail, unfortunately for them, they get pulled into the black hole system as well. You must choose the velocity components to escape both the black hole and the hostiles: ')
                sleep(.2)
                while question_8==False:
                    binary_vel = input('(1) Vx = 0.48c, Vy = 0.88c\n(2) Vx = 0.66c, Vy = 0.76c\n')
                    if binary_vel=='1' or binary_vel=='1 ' or binary_vel=='(1)'or binary_vel=='(1) Vx = 0.48c, Vy = 0.88c':
                        question_8=True
                        print('You chose the right velocity knowing there was no other escape. You were too close to the binary system to travel fast enough to escape. The velocity you chose sent you on a path to slingshot around both black holes, impressive intuition. The aliens that followed you here were not so smart; as you slingshot out of the galaxy, you look back and see their ship fall quickly into the abyss. You live on to see more days of space exploration and tell others of your adventures. ')
                        with open('binary_escape_edited.gif','rb') as file:
                            display(Image(file.read()))  # Escape
                        print('Congratulations, you have won the game! You are an expert space explorer and we wish you nothing but the best on your future endeavors.')
                        win=True
                        break
                    elif binary_vel=='2' or binary_vel=='2 'or binary_vel=='(2)'or binary_vel=='(2) Vx = 0.66c, Vy = 0.76':
                        print('You chose a very fast speed, and it gives you a chance at escaping, but you are caught in the gravity well and you did not choose the right velocity to escape the inescapeable. You got spaghettified - you are now centered at an infinitely small point, just like the aliens who followed you here. You\'re both trapped indefinitely until the black hole decays into nothing... together.')
                        with open('binary_death_edited.gif','rb') as file:
                            display(Image(file.read()))  # not so much escape
                        alive=False
                        break
                    else:
                        print('Invalid input, please try again.')

                sleep(.5)
                alive=False #while you might not necesarrily be dead at this point, this ends my top while loop
                #this is why I added the 'win' parameter


            #you will reach this if you are no longer alive
            if alive == False and win == False:
                sleep(1)
                with open('you_died.gif','rb') as file:
                    display(Image(file.read()))
            elif win == True:
                with open('you_win.gif','rb') as file:
                    display(Image(file.read()))
                winsound()
            print('Do you want to play again?')
            sleep(.8)
            play_again = input('Yes or No? ')
            if play_again == 'Yes' or play_again == 'yes' or play_again == 'Y' or play_again == 'y':
                print('Resetting Game')
                sleep(1.5) #waits 1.5 seconds so they know game is resetting
                clear_output(wait=True) #I think this will clear the output but I am not 100% sure
                #reset intial conditions
                question_1 = False
                question_2 = False
                question_3 = False
                question_4 = False
                question_5 = False
                question_6 = False
                question_7 = False
                question_8 = False
                freq_question = False
                alive = True #this allows us to make players restart when they die
                win = False
                continue
            elif play_again == 'no' or play_again == 'No' or play_again == 'N' or play_again =='n':
                print('Thank you for playing!')
                game_start = False
            else:
                print('Invalid input - you really couldn\'t even get the last question right? Try again.')
    

    
    
    
    #if they want to play without sound (basically exactly the same except without a few lines
    elif sound==False: 
        #deletes all variables so that if statement works properly
        from IPython.display import Image
        from IPython.display import clear_output
        from time import sleep #this function is used occasionally when things don't output in the correct order
        from modulenosound import Wave
        from modulenosound import Freq
        from modulenosound import Frequency
        from modulenosound import Wave2
        from modulenosound import Wavefile
        import numpy as np
        tarray = np.arange(0,1,0.0001)
        yarray = 11*np.sin(2*np.pi*tarray*1000)+12*np.sin(2*np.pi*tarray*200)
        tsmall = np.arange(0,1,0.0001)
        ysmall = 11*np.sin(2*np.pi*tsmall*1000)


        game_start = True #you want the game to start initially


        #these parameters are used so that if the give an invalid input, the question repeats (false means unanswered)
        question_1 = False
        question_2 = False
        question_3 = False
        question_4 = False
        question_5 = False
        question_6 = False
        question_7 = False
        question_8 = False
        freq_question = False
        win = False #you have not won yet
        alive = True #you are alive to start the game

        while game_start == True:
            while alive == True:
                print('You wake up on a ship. You look around and notice it\'s pitch black aside from a small emergency light shining on a control panel. Do you check it out?')
                sleep(0.2)
                while question_1 == False: #while question 1 hasn't been answered
                    check_light = input('Yes or No? ')
                    if check_light == 'Yes' or check_light == 'yes' or check_light == 'y' or check_light == 'Y': #if they say yes
                        question_1 = True #answered question 1
                        check_light = True #they did check the lights
                        continue
                    elif check_light == 'No' or check_light == 'no' or check_light == 'n' or check_light == 'N': #if they say no
                        question_1 = True #answered question 1
                        check_light = False #they did not check the lights
                        continue
                    else:
                        print('Invalid input, please try again.')

                while question_2 == False: #while question 2 hasn't been answered
                    if check_light == False: #if you did not check the light
                        print('You happen to find a flashlight and begin roaming the ship. You suddenly feel some turbulence and emergency alarms begin to sound. Do you return to the control panel to see whats wrong?')
                        curiosity = input('Yes or No? ')
                        if curiosity == 'Yes' or curiosity == 'yes' or curiosity == 'y' or curiosity == 'Y':
                            question_2 = True
                            continue
                        elif curiosity == 'No' or curiosity == 'no' or curiosity == 'n' or curiosity == 'N':
                            question_2 == True
                            print('You have no idea what is wrong and now you begin to hear creaking on one side of the ship. You feel some weird force on your body and you feel queasy. Suddenly you hear a loud crash for a fraction of a second, then immediate silence: one side of your ship has been ripped apart from the rest and you are now subject to the black hole that you were oblivious to until that very moment.')
                            print('Displaying Ships Trajectory...')
                            with open('do_nothing.gif','rb') as file:
                                display(Image(file.read()))
                            alive = False #you died
                            break
                        else:
                            print('Invalid input, please try again.')
                    if check_light == True:
                        question_2 = True #no need for second question
                        continue
                if alive == False: #if you die, you stop playing
                    break

                print('You are at the control panel. You see a master switch to turn on the lights. After switching them on you notice your ship is trapped in an orbit around an immense stellar mass. Do you attempt to escape the orbit?')
                while question_3 == False:    
                    try_to_escape = input('Yes or No? ')
                    if try_to_escape == 'Yes' or try_to_escape == 'yes' or try_to_escape == 'y' or try_to_escape == 'Y':
                        question_3 = True
                        continue
                    elif try_to_escape == 'No' or try_to_escape == 'no' or try_to_escape == 'n' or try_to_escape == 'N':
                        question_3 = True
                        print('As you ship tumbles closer to the black hole, the immense force ejects you from your ship and you begin the process of spaghetification headfirst.')
                        print('Displaying Ships Trajectory...')
                        with open('do_nothing.gif','rb') as file:
                            display(Image(file.read()))
                        alive = False #you died
                        break
                    else:
                        print('Invalid input, please try again.')

                if alive == False: #if you die, you stop playing
                    break

                print('You now have one chance to alter the ship\'s thrusters to escape the stellar mass which you now know is a black hole after looking out the window and seeing pitch black. What speed do you choose to attempt to escape?')
                while question_4 == False:
                    esc_vel = input('(1) 1.016c\n(2) 0.992c\n(3) 0.985c\n(4) 0.973c?\n')
                    if esc_vel == '1' or esc_vel == '1.016c' or esc_vel == '1 ' or esc_vel == '(1) 1.016c':
                        question_4 = True
                        print('You have attempted to violate the laws of physics - for this, you die.')
                        print('We are very dissapointed in you, you should have known better.')
                        alive = False
                        break
                    elif esc_vel == '2' or esc_vel=='0.992c' or esc_vel == '2 ' or esc_vel == '(2) 0.992c':
                        question_4 = True
                        continue #you do not die and move on
                    elif esc_vel == '3' or esc_vel=='0.985c' or esc_vel == '3 ' or esc_vel == '(3) 0.985c':
                        question_4 = True
                        print('While you were traveling extremely fast, it was not enough to escape the tremendous pull of the black hole. You and your ship get pulled into the black hole as you are slowly spaghettified.')
                        with open('black_hole_985.gif','rb') as file:
                           display(Image(file.read()))
                        alive = False
                        break
                    elif esc_vel == '4' or esc_vel=='0.973c' or esc_vel == '4 ' or esc_vel == '(4) 0.973c':
                        question_4 = True
                        print('While you were traveling extremely fast, it was not enough to escape the tremendous pull of the black hole. You and your ship get pulled into the black hole as you are slowly spaghettified.')
                        with open('black_hole_973.gif','rb') as file:
                           display(Image(file.read()))
                        alive = False
                        break
                    else:
                        print('Invalid input, please try again.')
                if alive == False: #if you die, you stop playing
                    break

                print('You speed away from the black hole to safety.')
                with open('black_hole_992.gif','rb') as file:
                            display(Image(file.read()))
                sleep(0.5)
                print('You can now roam the ship freely without a worry. Would you like to visit the lab or go to sleep?')
                sleep(0.5)

                while question_5 == False:
                    activity = input('(1) Explore the Lab\n(2) Go to Sleep\n')
                    if activity == '1' or activity == 'lab' or activity == 'Lab' or activity == '1 ':
                        question_5 = True
                        continue
                    elif activity == '2' or activity == '2 ' or activity=='sleep' or activity=='Sleep':
                        question_5 = True
                        print('You go to sleep, and when you wake up you are on an alien spaceship. They intersected your ship while you were sleeping.')
                        with open('alien_intersect.gif','rb') as file:
                            display(Image(file.read()))
                            sleep(2)
                        print('You feel as if you are under the influence of a drug you have never experienced and you\'re unable to understand the aliens speaking about what they are going to do to you. You do not last long on the alien ship and no human will ever see you again.')
                        alive = False
                        break
                    else:
                        print('Invalid input, please try again.')

                if alive == False: #if you die, you stop playing
                    break


                print('You go to the lab and begin measuring the frequency of AC current from a signal generator. You attempt to take the Fourier transform of the signal in order to determine if there is any noise aside from the frequency you expect, which was supposed to be '+str(Freq(tarray,yarray))+' Hz.')
                print('The actual signal you are receving looks like this:')
                Wave(tarray,yarray)
                sleep(.8)
                print('It appreas there is a prominent peak that you were not expecting.')
                while freq_question == False:
                    analyze_freq = input('What is the frequency you were not expecting (without units)? ')
                    if analyze_freq.isnumeric() == True:
                        if np.double(analyze_freq) >995 and np.double(analyze_freq) < 1005:
                            freq_question=True
                            continue
                        elif np.double(analyze_freq) > 195 and np.double(analyze_freq) < 205:
                            print('This is the frequency you were expecting, try again.')
                        else:
                            print('You are not detecting a signal at this frequency, please try again.')
                    else:
                        print('Invalid input, please try again.')

                print('You sigle out the unexpected frequency and find')
                Wave2(tsmall,ysmall)
                print(Freq(tsmall,ysmall),'Hz')
                print('Do you attempt to send the same signal back into space using your own function generator and oscilloscope?')#from text file
                sleep(0.8)
                while question_6 == False:
                    send_freq = input('Yes or No? ')
                    if send_freq == 'Yes' or send_freq=='yes' or send_freq=='y' or send_freq=='Y':
                        question_6=True
                        print(Frequency('1000Hz.txt'),'Hz')
                        Wavefile('1000Hz.txt')
                        print('After sending the signal back into space you look out the window and notice a light some distance away that appears to be approaching you. Do you go to the control room and attempt to change your trajectory, or do you stay where you are?')
                        while question_7 == False:
                            stay_or_leave = input('(1) Stay\n(2) Leave\n')
                            if stay_or_leave=='1'or stay_or_leave=='Stay' or stay_or_leave=='1 'or stay_or_leave=='stay':
                                question_7=True
                                print('As the object gets closer you see it is an alien ship, at which point you are no longer able to speed away in any direction, you are trapped in a tractor beam. You see a sudden flash of light and you are immediately unconscious. When you wake up, you are on an alien spaceship and you feel as if you are under the influence of a drug you have never experienced, and you are unable to understand the aliens speaking about what they are going to do to you. You do not last long on the alien ship. No human will ever see you again.')
                                alive=False
                                with open('alien_intersect.gif','rb') as file:
                                    display(Image(file.read())) # captured
                                break
                            elif stay_or_leave=='2'or stay_or_leave=='Leave' or stay_or_leave=='2 'or stay_or_leave=='leave':
                                question_7=True
                                print('You avoid what you believed to be a hostile situation and you played it safe.')
                                with open('alien_escape.gif','rb') as file:
                                    display(Image(file.read()))  # Escape  
                                continue
                            else:
                                print('Invalid input, please try again.')
                    elif send_freq == 'No' or send_freq=='no' or send_freq=='N' or send_freq=='n':
                        question_6=True
                        print('You decided not to send the mysterious signal back into space. This was the correct choice, you have survived by escaping the black hole and the hostile aliens. Great Job!')
                        break
                    else:
                        print('Invalid input, please try again.')


                if alive == False: #if you die, you stop playing
                    break

                print('You are free to continue exploring space on your own time. You realize you\'re barreling through space at 0.992c and are still traversing light years in what feels like fermiseconds. You have been busy working and did not realize where you are now. You zoomed by a binary black hole system: OJ 287, but were not going fast enough. The strength of both massive black holes is pulling you towards them. It turns out the aliens you escaped earlier are hot on your tail, unfortunately for them, they get pulled into the black hole system as well. You must choose the velocity components to escape both the black hole and the hostiles: ')
                sleep(.2)
                while question_8==False:
                    binary_vel = input('(1) Vx = 0.48c, Vy = 0.88c\n(2) Vx = 0.66c, Vy = 0.76c\n')
                    if binary_vel=='1' or binary_vel=='1 ' or binary_vel=='(1)'or binary_vel=='(1) Vx = 0.48c, Vy = 0.88c':
                        question_8=True
                        print('You chose the right velocity knowing there was no other escape. You were too close to the binary system to travel fast enough to escape. The velocity you chose sent you on a path to slingshot around both black holes, impressive intuition. The aliens that followed you here were not so smart; as you slingshot out of the galaxy, you look back and see their ship fall quickly into the abyss. You live on to see more days of space exploration and tell others of your adventures. ')
                        with open('binary_escape_edited.gif','rb') as file:
                            display(Image(file.read()))  # Escape
                        print('Congratulations, you have won the game! You are an expert space explorer and we wish you nothing but the best on your future endeavors.')
                        win=True
                        break
                    elif binary_vel=='2' or binary_vel=='2 'or binary_vel=='(2)'or binary_vel=='(2) Vx = 0.66c, Vy = 0.76':
                        print('You chose a very fast speed, and it gives you a chance at escaping, but you are caught in the gravity well and you did not choose the right velocity to escape the inescapeable. You got spaghettified - you are now centered at an infinitely small point, just like the aliens who followed you here. You\'re both trapped indefinitely until the black hole decays into nothing... together.')
                        with open('binary_death_edited.gif','rb') as file:
                            display(Image(file.read()))  # not so much escape
                        alive=False
                        break
                    else:
                        print('Invalid input, please try again.')

                sleep(.5)
                alive=False #while you might not necesarrily be dead at this point, this ends my top while loop
                #this is why I added the 'win' parameter


            #you will reach this if you are no longer alive
            if alive == False and win == False:
                sleep(1)
                with open('you_died.gif','rb') as file:
                    display(Image(file.read()))
            elif win == True:
                with open('you_win.gif','rb') as file:
                    display(Image(file.read()))
            print('Do you want to play again?')
            sleep(.8)
            play_again = input('Yes or No? ')
            if play_again == 'Yes' or play_again == 'yes' or play_again == 'Y' or play_again == 'y':
                print('Resetting Game')
                sleep(1.5) #waits 1.5 seconds so they know game is resetting
                clear_output(wait=True) #I think this will clear the output but I am not 100% sure
                #reset intial conditions
                question_1 = False
                question_2 = False
                question_3 = False
                question_4 = False
                question_5 = False
                question_6 = False
                question_7 = False
                question_8 = False
                freq_question = False
                alive = True #this allows us to make players restart when they die
                win = False
                continue
            elif play_again == 'no' or play_again == 'No' or play_again == 'N' or play_again =='n':
                print('Thank you for playing!')
                game_start = False
            else:
                print('Invalid input - you really couldn\'t even get the last question right? Try again.')
