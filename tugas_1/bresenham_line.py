import matplotlib.pyplot as plt

plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bresenham_line(x1,y1,x2,y2):
  x,y = x1,y1
  dx = abs(x2 - x1)
  dy = abs(y2 -y1)
  pk = 2 * dx - dy

  gradient = dy / dx
  print("gradien: ", gradient)

  if gradient > 1:
      dx, dy = dy, dx
      x, y = y, x
      x1, y1 = y1, x1
      x2, y2 = y2, x2

  print(f"x = {x}, y = {y}")

  # Initialize the plotting points
  xcoordinates = [x]
  ycoordinates = [y]

  while (x < x2 or y < y2):
    if pk < 0:
        pk = pk + 2 * dy
    else:
        pk = pk + 2 * (dy - dx)
        y = y + 1 if y < y2 else y - 1 # kalo menurun y -1

    x = x + 1 if x < x2 else x - 1 # kalo ke kanan x - 1

    print(f"x = {x}, y = {y}")
    xcoordinates.append(x)
    ycoordinates.append(y)

  plt.plot(xcoordinates, ycoordinates)
  plt.show()

x1 = 4
y1 = 14
x2 = 12
y2 = 2

bresenham_line(x1, y1, x2, y2)