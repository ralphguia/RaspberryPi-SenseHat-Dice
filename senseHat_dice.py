from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Colours defined
w = (255,255,255)    #white
y = (255, 255, 0)    #yellow
o = (255, 165, 0)    #orange
g = (0,255, 0)       #green
bl = (0, 0, 255)      #blue
p = (255, 0, 255)    #purple

b = (0, 0, 0)       #black

# dice 1
d1 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

# dice 2
d2 = [
    y, y, b, b, b, b, b, b,
    y, y, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, y, y,
    b, b, b, b, b, b, y, y
]

# dice 3
d3 = [
    o, o, b, b, b, b, b, b,
    o, o, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, o, o, b, b, b,
    b, b, b, o, o, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, o, o,
    b, b, b, b, b, b, o, o
]

# dice 4
d4 = [
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g
]

# dice 5
d5 = [
    bl, bl, b, b, b, b, bl, bl,
    bl, bl, b, b, b, b, bl, bl,
    b, b, b, b, b, b, b, b,
    b, b, b, bl, bl, b, b, b,
    b, b, b, bl, bl, b, b, b,
    b, b, b, b, b, b, b, b,
    bl, bl, b, b, b, b, bl, bl,
    bl, bl, b, b, b, b, bl, bl
]

# dice 6
d6 = [
    p, p, b, b, b, b, p, p,
    p, p, b, b, b, b, p, p,
    b, b, b, b, b, b, b, b,
    p, p, b, b, b, b, p, p,
    p, p, b, b, b, b, p, p,
    b, b, b, b, b, b, b, b,
    p, p, b, b, b, b, p, p,
    p, p, b, b, b, b, p, p
]

def setPixelDice(rolledDice):
    sense.set_pixels(rolledDice)


while True:
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']

  x = abs(x)
  y = abs(y)
  z = abs(z)
    
  print("x={0}, y={1}, z={2}".format(x, y, z))

  if x > 1 or y > 1 or z > 1:
      rolledDice = random.choice([d1,d2,d3,d4,d5,d6])
      sleep(1)
      setPixelDice(rolledDice)
      sleep(5)
  else:
      sense.clear()
