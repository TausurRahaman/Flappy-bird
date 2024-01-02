import time

last = time.time()

for i in range(1,100):
  print(i)

current = time.time()
dt = current - last
print(dt)