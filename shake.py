ACTIVITY 3
from sense_hat import SenseHat
sense = SenseHat()
g = (0, 255, 102) #green
b = (0, 0, 0) #blank

Happy = [
  g,g,g,g,g,g,g,g,
  g,g,g,g,g,g,g,g,
  g,g,b,g,g,b,g,g,
  g,g,g,g,g,g,b,g,
  g,g,g,g,g,g,g,g,
  g,b,g,g,g,g,b,g,
  g,g,b,b,b,b,g,g,
  g,g,g,g,g,g,g,g,
]

Sad = [
  g,g,g,g,g,g,g,g,
  g,g,g,g,g,g,g,g,
  g,g,b,g,g,b,g,g,
  g,g,g,g,g,g,b,g,
  g,g,g,g,g,g,g,g,
  g,g,b,b,b,b,g,g,
  g,b,g,g,g,g,b,g,
  g,g,g,g,g,g,g,g,
]
sense.set_pixels(Happy)
x,y,z = sense.get_accelerometer_raw().values()
while x<1 and y<1 and z<1:
x,y,z = sense.get_accelerometer_raw().values()
sense.set_pixels(Sad)
