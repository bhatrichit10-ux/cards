import time
import board
import neopixel

num_leds = 3
data_pin = board.P6
brightness = 0.3

pixels = neopixel.NeoPixel(data_pin, num_leds, brightness=brightness, auto_write=False, pixel_order=neopixel.GRB)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
off = (0, 0, 0)
purple = (180, 0, 255)


def solid(color):
    pixels.fill(color)
    pixels.show()


def wheel(pos):
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


def rainbow_cycle(wait=0.005):
    for j in range(255):
        for i in range(num_leds):
            idx = (i * 256 // num_leds) + j
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)


def chase(color, wait=0.15):
    for i in range(num_leds):
        pixels.fill(off)
        pixels[i] = color
        pixels.show()
        time.sleep(wait)
    pixels.fill(off)
    pixels.show()


def breathe(color, steps=50, wait=0.01):
    for s in range(steps):
        f = s / steps
        pixels.fill((int(color[0]*f), int(color[1]*f), int(color[2]*f)))
        pixels.show()
        time.sleep(wait)
    for s in range(steps, 0, -1):
        f = s / steps
        pixels.fill((int(color[0]*f), int(color[1]*f), int(color[2]*f)))
        pixels.show()
        time.sleep(wait)


while True:
    solid(red)
    time.sleep(0.5)
    solid(green)
    time.sleep(0.5)
    solid(blue)
    time.sleep(0.5)

    chase(white)
    chase(white)

    rainbow_cycle()

    breathe(purple)
    breathe(purple)

    pixels.fill(off)
    pixels.show()
    time.sleep(0.5)
