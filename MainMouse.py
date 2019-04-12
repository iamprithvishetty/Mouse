from serial import Serial
port='COM31'
baudrate= 9600
ser = Serial(port,baudrate)
from pymouse import PyMouse
push=1
counter = 0
m=PyMouse()
max_v=12
centre=max_v/2
threshold=max_v/4
j=m.position()[0]
k=m.position()[1]
def C_value(this_value,centre):
  reading = this_value*max_v/1024
  center=centre
  distance = reading - center
  if abs(distance) < threshold: 
   distance = 0
  return distance


while True:
  value = ser.readline()
  x=int(value.split('-')[1])
  y=int(value.split('-')[0])
  push=int(value.split('-')[2])
  x_max = m.screen_size()[0]
  y_max = m.screen_size()[1]
  print(x,y)
  x_new= C_value(x,centre)
  y_new= C_value(y,centre)
  m.move(j+x_new,k-y_new)
  j=m.position()[0]
  k=m.position()[1]
  if push==0:
   counter = 1
  if counter-push == 0:
   m.click(j+x_new,k-y_new,1)
   counter = 0
 
 