#Daniel Tugendhaft 318465291
#task_1 - Area:

import math

Shape = input('Please enter the area you want to calculate R or r for rectangle, C or c for circle:')



if Shape == 'r' or Shape == 'R':

  Rectangle = input('Please enter width and height of the rectangle separated by comma:').split(',')

  Rectangle[0] = float(Rectangle[0])

  Rectangle[1] = float(Rectangle[1])

  print ('The area of a rectangle with width' ,Rectangle[0] ,'and height' ,Rectangle[1] ,'is :' ,Rectangle[0]*Rectangle[1])

elif Shape == 'c' or Shape == 'C':

  Radios = float(input('Please enter the radius:'))

  print ('The area of a circle with radius' ,Radios ,'is' ,Radios**2*math.pi)

else:

  print ('option', Shape, 'does not exist')
