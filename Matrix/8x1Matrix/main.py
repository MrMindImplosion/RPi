#!/usr/bin/env python3
import RPi.GPIO as GPIO #@UnresolvedImport
import time
import os

frameSpeed = 25
goOverCount = 5
class pin():
    clock = 18
    reset = 23
    input = 24
    out = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin.clock, GPIO.OUT)
GPIO.setup(pin.reset, GPIO.OUT)
GPIO.setup(pin.input, GPIO.OUT)
GPIO.setup(pin.out, GPIO.OUT)
def loadFrames(file):
    frames = open(file,"r").read().split("\n")
    return frames
def tick(on=pin.clock):
    GPIO.output(on,GPIO.HIGH)
    GPIO.output(on,GPIO.LOW)
def main():
    import sys
    try:
        file = sys.argv[1]
    except IndexError:
        file = "test"
    frames=loadFrames("./animations/%s" % file)
    while 1:
        for frame in frames:
            if frame == "":
                continue
            for x in range(goOverCount):
                for l in frame:
                    if l == "1":
                        GPIO.output(pin.out,GPIO.HIGH)
                    else:
                        GPIO.output(pin.out,GPIO.LOW)
                    tick()
                    time.sleep(1/(frameSpeed*len(frame)*goOverCount))
                tick(pin.reset)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    tick(pin.reset)
    GPIO.cleanup()
    
        