from gpiozero import Button, RGBLED
import random, time

btnR = Button(19)
btnB = Button(26)
RGB = RGBLED(22,27,17)

red = (1,0,0)
blue = (0,1,0)
green = (0,0,1)

def monitorButtons(seconds):

    timeEnd = time.time() + seconds
    while time.time()<timeEnd:
            if btnR.is_pressed:
                return announceWinner(btnR)    
            if btnB.is_pressed:
                    return announceWinner(btnB)
    return False

def announceWinner(btn):

    if RGB.color == green:
            winner = red if btn == btnR else blue
    else:
            winner = blue if btn == btnB else red

    RGB.blink(on_color = winner, n = 5 , background = 0)

btnPressed = False
while btnPressed == False:

    ledColor = random.choice([red,green,blue])

    RGB.color = ledColor
    btnPressed = monitorButtons(5)
    

        
