import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.GP0
num_pixels = 70

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

def color_chase(colors, wait):
    for i in range(num_pixels):
        color = colors[i % len(colors)]
        pixels[i] = color
        pixels.show()
        time.sleep(wait)


def reverse_color_chase(colors, wait):
    for i in reversed(range(num_pixels)):
        color = colors[i % len(colors)]
        pixels[i] = color
        pixels.show()
        time.sleep(wait)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

def color_fade(color1, color2, steps):
    fade_colors = []
    # Fade from color1 to color2
    for step in range(steps):
        red = int((color1[0] * (steps - step) + color2[0] * step) / steps)
        green = int((color1[1] * (steps - step) + color2[1] * step) / steps)
        blue = int((color1[2] * (steps - step) + color2[2] * step) / steps)
        fade_colors.append((red, green, blue))
    # Fade from color2 back to color1
    for step in range(steps):
        red = int((color2[0] * (steps - step) + color1[0] * step) / steps)
        green = int((color2[1] * (steps - step) + color1[1] * step) / steps)
        blue = int((color2[2] * (steps - step) + color1[2] * step) / steps)
        fade_colors.append((red, green, blue))
    return fade_colors


def moving_color_fade(colors, wait, cycles=1, reverse=False):
    length = len(colors)
    offset = 0

    for cycle in range(cycles):
        for _ in range(length):
            for i in range(num_pixels):
                index = (i + offset) % length if not reverse else (length - 1 - (i + offset) % length)
                pixels[i] = colors[index]
                
            pixels.show()
            time.sleep(wait)
            offset = (offset + 1) % length if not reverse else (offset - 1 + length) % length

        # Reset the offset for the next cycle, ensuring it wraps around correctly
        offset = offset % length




while True:
    #pixels.fill(RED)
    #pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    #time.sleep(1)
    #pixels.fill(GREEN)
    #pixels.show()
    #time.sleep(1)
    #pixels.fill(BLUE)
    #pixels.show()
    #time.sleep(1)
    #color_chase(RED, 0.1)  # Decrease the number to slow down the color chase
    #color_chase(YELLOW, 0.1)
    #color_chase(GREEN, .2)
    #color_chase(CYAN, 0.1)
    #color_chase(BLUE, 0.1)
    #color_chase(PURPLE, 0.1)
    #color_chase(OFF, .2)
    #reverse_color_chase(GREEN, .2)
    #reverse_color_chase(OFF, .2)
    #rainbow_cycle(0.1)  # Increase the number to slow down the rainbow
    #---------------FADE---------------#
    fade_colors = color_fade(BLUE, GREEN, num_pixels)
    ##for i in range(num_pixels):
    ##    pixels[i] = fade_colors[i % len(fade_colors)]
    ##pixels.show()
    ##time.sleep(0.1)  # Adjust the sleep time as needed
    #color_chase(fade_colors, 0.03)
    moving_color_fade(fade_colors, 0.04, cycles=1, reverse=False)  # Forward
    moving_color_fade(fade_colors, 0.04, cycles=1, reverse=True)   # Reverse
