#!/usr/bin/env python3

import os
import sys
import argparse
import buttonshim
import time
import signal
from PIL import Image
from inky import InkyWHAT

# locally defines modules
# from showimage import showImage

# this has to be refactored to a (few) classes
def showImage(img_file: str):
    # Open our image file that was passed in from the command line

    print("displaying image, please wait")
    img = Image.open(img_file)

    # Get the width and height of the image

    w, h = img.size

    # Calculate the new height and width of the image

    h_new = 300
    w_new = int((float(w) / h) * h_new)
    w_cropped = 400

    # Resize the image with high-quality resampling

    img = img.resize((w_new, h_new), resample=Image.LANCZOS)

    # Calculate coordinates to crop image to 400 pixels wide

    x0 = (w_new - w_cropped) / 2
    x1 = x0 + w_cropped
    y0 = 0
    y1 = h_new

    # Crop image

    img = img.crop((x0, y0, x1, y1))

    # Convert the image to use a white / black / red colour palette

    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

    img = img.convert("RGB").quantize(palette=pal_img)

    # Display the final image on Inky wHAT

    inky_display.set_image(img)
    inky_display.show()
    print("Image ready")

# initialize default buttonhandler for buttonshim
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    global button_flag
    button_flag = "button_1"
    
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    global button_flag
    button_flag = "button_2"
    
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    global button_flag
    button_flag = "button_3"

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    global button_flag
    button_flag = "button_4"

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):    
    global button_flag
    button_flag = "button_5"
    
try:
    if __name__ == '__main__':

        print("""Inky wHAT: Dither image

        Converts and displays dithered images on Inky wHAT.

        Button SHIM:

        Light up the LED a different color of the rainbow with each button pressed.
        Show an image depending on button pressed

        press <ctrl>+<c> to quit

        """)

        # Command line arguments to set display type and colour, and enter your name

        parser = argparse.ArgumentParser()
        parser.add_argument('--colour', '-c', type=str, required=True, choices=["red", "black", "yellow"], help="ePaper display colour")
        parser.add_argument('--image', '-i', type=str, required=True, help="Input image to be converted/displayed")
        args = parser.parse_args()

        colour = args.colour
        img_file = args.image

        button_flag = "null"  

        # Set up the inky wHAT display and border colour

        inky_display = InkyWHAT(colour)
        inky_display.set_border(inky_display.WHITE)

        showImage(img_file)
        print("press a button to show a different image...")

        while True:
            time.sleep(.1)
            if button_flag == "button_1":
                buttonshim.set_pixel(0x94, 0x00, 0xd3)
                button_flag = "null"
                showImage("resources/Escher_Dag-en-Nacht.jpg")
                print("press a button to show a different image...")
            elif button_flag == "button_2":
                buttonshim.set_pixel(0x00, 0x00, 0xff)
                button_flag = "null"
                showImage("resources/Escher_het_oog.jpg")
                print("press a button to show a different image...")
            elif button_flag == "button_3":    
                buttonshim.set_pixel(0x00, 0xff, 0x00)
                button_flag = "null"
                showImage("resources/Escher_Trappen.jpeg")
                print("press a button to show a different image...")
            elif button_flag == "button_4":       
                buttonshim.set_pixel(0xff, 0xff, 0x00)
                button_flag = "null"
                showImage("resources/InkywHAT-400x300-bw.png")
                print("press a button to show a different image...")
            elif button_flag == "button_5":   
                buttonshim.set_pixel(0xff, 0x00, 0x00)
                button_flag = "null"
                showImage("resources/pattern-3.jpg")
                print("press a button to show a different image...")

except KeyboardInterrupt:
    # quit
    print ("program terminated")
    sys.exit()
