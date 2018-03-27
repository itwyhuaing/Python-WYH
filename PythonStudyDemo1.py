
import math
import string

def move(x,y,step,angle=0):
  nx = x + step * math.cos(angle)
  ny = y + step * math.cos(angle)
  return nx,ny

print(move(1,3,1,0))
name = input()
print('name = ',name)
