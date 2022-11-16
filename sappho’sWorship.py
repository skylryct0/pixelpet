from sense hat import SenseHat
sense = SenseHat()

d = (255,80, 12) #dark orange
o = (255,119,51) #orange
w = (255,255,255) #white
p = (229,150,200) #pink
a = (150,77,130) #dark pink
n = (0,0,0) #nothing

image = [
  d,d,d,d,d,d,d,d,
  o,o,o,o,o,o,o,o,
  w,w,w,w,w,w,w,w,
  p,p,p,p,p,p,p,p,
  a,a,a,a,a,a,a,a,
  n,n,n,n,n,n,n,n,
  n,n,n,n,n,n,n,n,
  n,n,n,n,n,n,n,n
]

sense.set_pixells(image)
