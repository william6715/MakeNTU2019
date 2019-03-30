import sys
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,12,13,15
# GPIO17,GPIO18,GPIO21,GPIO22
StepPins = [17,18,21,22]

# Set all pins as output
for pin in StepPins:
    print ("Setup pins")
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

StepCount = len(Seq)
StepDir = 1


# Read wait time from command line
if len(sys.argv)>1:
WaitTime = int(sys.argv[1])/float(1000)
else:
WaitTime = 10/float(1000)

# Initialise variables
StepCounter = 0

# Start main loop
while True:

    print (StepCounter)
    print (Seq[StepCounter])

    for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
            print (" Enable GPIO " ,(xpin))
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)

    StepCounter += StepDir

    # If we reach the end of the sequence
    # start again
    if (StepCounter>=StepCount):
        StepCounter = 0
    if (StepCounter<0):
        StepCounter = StepCount+StepDir

    # Wait before moving on
    time.sleep(WaitTime)
