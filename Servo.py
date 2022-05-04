import time
import pyfirmata
from pyfirmata import Arduino, util, SERVO

#config puerto Arduino y pin Servo
board = Arduino('COM3')
time.sleep(5)
board.digital[9].mode = SERVO
#movimiento Servo

def Servo(pos):
    board.digital[9].write(pos)

    