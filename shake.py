#ACTIVITY 3
from sense_hat import SenseHat
sense = SenseHat()
g = (0, 255, 102) #green
b = (0, 0, 0) #blank
p = (204, 0 , 204) #pink
g = (0, 102, 102) #green
w = (255, 255, 255) #white
r = (255, 0, 0) #red
o = (255, 75, 75) #orange
y = (204, 204, 0) #yellow


Happy = [
        b,b,b,b,b,r,b,r,
        g,g,b,b,b,r,b,r,
        g,g,b,b,b,b,b,b,
        g,g,g,b,b,r,b,r,
        g,b,g,g,b,b,b,b,
        g,w,g,b,g,b,b,b,
        g,g,g,w,g,g,b,b,
        g,g,g,g,g,g,b,b
]

Sad = [
        e,y,e,e,e,e,y,e,
        e,e,e,y,e,y,e,y,
        y,e,g,g,g,g,e,e,
        e,g,w,g,e,g,g,e,
        e,g,e,g,w,g,g,e,
        e,g,g,g,g,g,g,e
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
]
sense.set_pixels(Happy)
x,y,z = sense.get_accelerometer_raw().values()
while x<1 and y<1 and z<1:
x,y,z = sense.get_accelerometer_raw().values()
sense.set_pixels(Sad)
