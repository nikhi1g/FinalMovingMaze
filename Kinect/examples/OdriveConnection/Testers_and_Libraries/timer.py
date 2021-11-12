import time

time_start = time.time()
seconds = 0
minutes = 0

running = True

while running:
        print(seconds)
        time.sleep(1)
        seconds = int(time.time() - time_start)

