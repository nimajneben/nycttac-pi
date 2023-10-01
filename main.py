#!/usr/bin/env python3

# Set up Display
from dothat import lcd
from dothat import backlight as bklit

bklit.rgb(100,0,100)
lcd.write("NYCT TAC - RPi")
lcd.set_contrast(55)
lcd.set_cursor_position(0,1)
lcd.write("v1")

# Set up
