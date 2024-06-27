# Imports go at the top
from microbit import *

def light_left_side():
    for row in range(5):
        display.set_pixel(0,row,9)
        display.set_pixel(1,row,9)
    
def light_right_side():
    for row in range(5):
        display.set_pixel(3,row,9)
        display.set_pixel(4,row,9)

# Statuses:
a_pressed = False
b_pressed = False
both_pressed = False

# Button Counts:
count_a = 0
count_b = 0
count_both = 0

while True:
    if button_a.is_pressed():
        light_left_side()
        if count_both > count_a:
            light_right_side()
        a_pressed = True

    if button_b.is_pressed():
        light_right_side()
        if count_both > count_b:
            light_left_side()
        b_pressed = True

    if button_a.is_pressed() and button_b.is_pressed():
        both_pressed = True

    if not button_a.is_pressed() and not button_b.is_pressed():
        display.clear()
        if both_pressed:
            count_both += 1
        elif a_pressed:
            count_a += 1
        elif b_pressed:
            count_b += 1
        a_pressed = b_pressed = both_pressed = False
