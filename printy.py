# creates a typewriter effect
import time, sys

def printy(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.06)
