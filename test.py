from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
  bar.next()
  time.sleep(1)
bar.finish()
