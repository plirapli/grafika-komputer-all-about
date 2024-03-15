import matplotlib.pyplot as plt

def bresenham_circle(r):
  x = r
  y = 0
  err = 0
  points = []

  while(x >= y):
    points.append((x, y))
    points.append((-x, y))
    points.append((x, -y))
    points.append((-x, -y))
    points.append((y, x))
    points.append((-y, x))
    points.append((y, -x))
    points.append((-y, -x))

    y += 1
    err += 1 + 2 * y
    
    if 2 * (err - x) + 1 > 0:
      x -= 1
      err += 1 - 2 * x

  return points

r = 50
points = bresenham_circle(r)

# plot the points
plt.scatter([x for x, y in points], [y for x, y in points])

# draw the circle
circle = plt.Circle((0, 0), r, fill=False)
plt.gcf().gca().add_artist(circle)

plt.show()