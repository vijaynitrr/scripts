import time
import commands

while True:
    time.sleep(3600)
    commands.getstatusoutput("notify-send 'Sir please drink water' 'And take an walk'")
