#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import cgi;
import cgitb;
cgitb.enable()
print("Content-Type: text.plain")
print("")
form = cgi.FieldStorage()
GPIO.setmode(GPIO.BOARD)
led = 11
servo = 13
poco = 10
GPIO.setup(led,GPIO.OUT)
GPIO.setup(servo,GPIO.OUT)
p = GPIO.PWM(servo,50)
p.start(5)

time.sleep(poco)
GPIO.output(led,True)
p.ChangeDutyCycle(10.5)
time.sleep(poco)
GPIO.output(led,False)
p.ChangeDutyCycle(5)
time.sleep(0.5)
p.stop()
print "Se ha realizado con exito"
GPIO.cleanup()


