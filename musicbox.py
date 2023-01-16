from gpiozero import Button

import pygame

pygame.init()


sndRed = pygame.mixer.Sound('/home/pi/Desktop/Music_Samples/piano-g_G_major.wav')
sndYellow = pygame.mixer.Sound('/home/pi/Desktop/Music_Samples/piano-f_F_major.wav')
sndOrange = pygame.mixer.Sound('/home/pi/Desktop/Music_Samples/piano-eb_D#_major.wav')

btnRed = Button(17)
btnYellow = Button(14)
btnOrange = Button(15)

def red():
    print("red has been pressed (G)")
    sndRed.play()
    
def yellow():
    print("yellow has been pressed (F)")
    sndYellow.play()

def orange():
    print("orange has been pressed (D#)")
    sndOrange.play()
    
btnRed.when_pressed = red
btnYellow.when_pressed = yellow
btnOrange.when_pressed = orange

