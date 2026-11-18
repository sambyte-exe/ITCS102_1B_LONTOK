s = 7
u = 4

for x in range(n):
  for y in range(u):
    if x + y == u - 1 or ( x == 0 ans y >= 3):
      print('*', end=' ')
    elif (x==r-1 and y<=3) or (x+y==u-1 and y>=4):
      print('*', end=' ')
    else:
            print(' ', end=' ')
  print()
