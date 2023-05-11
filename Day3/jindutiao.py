import sys
import time

help(open)

for i in  range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)