import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
  x = x1
  y = y1
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  
  # find max difference
  steps = max(dx, dy)

  # calculate the increment in x and y
  x_inc = dx / steps if x < x2 else (dx / steps) * -1
  y_inc = dy / steps if y < y2 else (dy / steps) * -1
  
  # make a list for coordinates 
  x_coordinates = [] 
  y_coordinates = []

  # first coordinates
  x_coordinates.append(x) 
  y_coordinates.append(y) 

  for i in range(steps):

    # increment the values 
    x += x_inc
    y += y_inc

    # append the x,y coordinates in respective list 
    x_coordinates.append(x) 
    y_coordinates.append(y) 

  print(x_coordinates, y_coordinates)
  # plot the line with coordinates list 
  plt.plot(x_coordinates, y_coordinates) 
  plt.show() 

x1, y1 = 4, 14
x2, y2 = 12, 2
dda_line(x1, y1, x2, y2)