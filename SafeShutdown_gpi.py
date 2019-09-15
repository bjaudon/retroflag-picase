#!/usr/bin/env python3
from gpiozero import Button, LED
import os 
from signal import pause
import subprocess

powerPin = 26  
powerenPin = 27 
hold = 1
power = LED(powerenPin)
power.on()

#functions that handle button events
def when_pressed():
 output = int(subprocess.check_output(['/opt/RetroFlag/multi_switch.sh', '--es-pid']))
 if output:
     os.system("/opt/RetroFlag/multi_switch.sh --es-poweroff")
 else:
     os.system("sudo shutdown -h now")
    
btn = Button(powerPin, hold_time=hold)
btn.when_pressed = when_pressed
pause()
