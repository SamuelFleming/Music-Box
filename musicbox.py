from gpiozero import Button
import pygame

pygame.init()

sndA = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_A.wav')
sndAs = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_A#.wav')
sndB = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_B.wav')
sndC = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_C.wav')
sndCs = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_C#.wav')
sndD = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_D.wav')
sndDs = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_D#.wav')
sndE = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_E.wav')
sndF = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_F.wav')
sndFs = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_F#.wav')
sndG = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_G.wav')
sndGs = pygame.mixer.Sound('/home/pi/Desktop/Music.Samples/Piano/piano_G#.wav')

scale,key,instruments = 0,1,1

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
btn_instrument = Button(15)

def scale_change():
    global scale
    if scale < 2:
        scale+=1
        print(scale)
    else:
        scale = 0
        print(scale)
        
btn_scale.when_pressed = scale_change

def one():
    sndA.play()
    print("A")
         
btn_one.when_pressed = one

def two():
    global scale
    if scale == 0:
        sndB.play()
        print("B")
    elif scale == 1:
        sndB.play()
        print("B")
    else:
        sndAs.play()
        print("A#")
btn_two.when_pressed = two

def three():
    global scale
    if scale == 0:
        sndCs.play()
        print("C#")
    elif scale == 1:
        sndC.play()
        print("C")
    else:
        sndCs.play()
        print("C#")
btn_three.when_pressed = three

def four():
    sndD.play()
    print("D")
btn_four.when_pressed = four

def five():
    sndE.play()
    print("E")
btn_five.when_pressed = five

def six():
    if scale == 0:
        sndFs.play()
        print("F#")
    else:
        sndF.play()
        print("F")
btn_six.when_pressed = six

def seven():
    if scale == 0:
        sndG.play()
        print("G")
    else:
        sndGs.play()
        print("G#")
btn_seven.when_pressed = seven

btn_eight.when_pressed = one

