import lightpack, math, time, re, random

lpack = lightpack.lightpack('127.0.0.1', 3636, range(1,11) )
lpack.connect()
lpack.lock()

leds = 10
# beats per minute

bpm = 120

lpack.lock()        
while True :
    bpm_time = 60.0 / bpm
    bpm_wait = bpm_time - 0.05
    for k  in range (0, leds):
        lpack.setColor(k+1, 255, 255, 255)
    time.sleep(0.05)
    for k  in range (0, leds):
        lpack.setColor(k+1, 0, 0, 0)
    time.sleep(bpm_time)
    bpm = bpm + 1


lpack.unlock()

