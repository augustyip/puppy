import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(1) # do real work here
    # update the bar
    sys.stdout.write( str(i) + "/" + str(toolbar_width))
    sys.stdout.flush()

sys.stdout.write("\n")
