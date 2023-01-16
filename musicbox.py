from gpiozero import Button

import pygame

pygame.init()

scale_num,key_num = 0, 0

#Arrays of integer values corresponding values:
key_nom = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "G", "G#"]
scale_nom = ["Major", "Minor", "Phyrigian Dominant"]


#dynamic array:
array_dynam = [0, 2, 4, 5, 7, 9, 11]

#definition of default sound file variables
snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/0.wav')
snd2 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/2.wav')
snd3 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/4.wav')
snd4 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/5.wav')
snd5 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/7.wav')
snd6 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/9.wav')
snd7 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/11.wav')

#sound array
Snd = ["0.wav", "2.wav", "4.wav", "5.wav", "7.wav", "9.wav", "11.wav", ]


#default scale arrays:
def_0 = [0, 2, 4, 5, 7, 9, 11]
def_1 = [0, 2, 3, 5, 7, 8, 10]
def_2 = [0, 1, 4, 5, 7, 8, 10]


#definition of button
btn_one = Button(26)
btn_two = Button(16)
btn_three = Button(13)
btn_four = Button(12)
btn_five = Button(5)
btn_six = Button(1)
btn_seven = Button(11)
btn_eight = Button(25)
btn_key = Button(17)
btn_scale = Button(14)




#main configuration function
def scale_config():
    
    #setting integers as global variables
    global scale_num
    global key_num
    global array_dynam
    global current_scale
    global def_0
    global def_1
    global def_2
    
    #if statement to determine current scale list/array
    if scale_num == 0:
        current_scale = def_0
    elif scale_num == 1:
        current_scale = def_1
    else:
        current_scale = def_2
        
    
    # for loop calculates an enters a new value in array_dynam for as many times as the length of the lis (seven times)
    for x in range(0, len(current_scale)):
               
        current_value = current_scale[x]
        #adding the key_num to default scale values to calculate dynamic array values
        if (current_value + key_num) < 12:
            array_dynam[x] = (current_value + key_num)
        else:
            array_dynam[x] = (current_value + key_num - 12)
        
        #varaibel input into the sound file arrays
        snd[x] = str(array_dynam[x]) + ".wav"
    
    #selecting the sound files via index value in list; 'snd'
    snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[0]))
    snd2 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[1]))
    snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[2]))
    snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[3]))
    snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[4]))
    snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[5]))
    snd1 = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/' + str(array_dynam[6]))
    print("The new key is; " + str(key_nom[key_num]) + " " + str(scale_nom[scale_num]))

  

def scale_change():
    global scale_num
    if scale_num < 2:
        scale_num+=1
    else:
        scale_num = 0
    current_scale_nat = scale_nom[scale_num]
    print("The new key is; " + str(key_nom[key_num]) + " " + str(current_scale_nat))
    print ("you just changed the nature of the key (Scale type).")
    print ("")

    scale_config
btn_scale.when_pressed = scale_change

def key_change():
    global key_num
    if key_num < 11:
        key_num+=1
    else:
        key_num = 0
    current_key = key_nom[key_num]
    print("The new key is; " + str(key_nom[key_num]) + " " + str(scale_nom[scale_num]))
    print ("you just changed the pitch of the key (Key Bass Note).")
    print ("")

    scale_config()
btn_key.when_pressed = key_change
    
#executing the sound per button pressed
def one():
    snd1.play()
    print(array_dynam[0])
btn_one.when_pressed = one

def two():
    snd2.play()
    print(array_dynam[1])
btn_two.when_pressed = two

def three():
    snd3.play()
    print(array_dynam[2])
btn_three.when_pressed = three

def four():
    snd4.play()
    print(array_dynam[3])
btn_one.when_pressed = four

def five():
    snd5.play()
    print(array_dynam[4])
btn_one.when_pressed = five

def six():
    snd6.play()
    print(array_dynam[5])
btn_six.when_pressed = six

def seven():
    snd7.play()
    print(array_dynam[6])
btn_seven.when_pressed = seven

btn_eight.when_pressed = one

