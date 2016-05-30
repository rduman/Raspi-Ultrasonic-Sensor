import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24
print "Mesafe Olcumu"
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
while True:
    GPIO.output(TRIG,False)
    print "Uzaklik hesaplaniyor...."
    time.sleep(2)        
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end - pulse_start
    mesafe=pulse_duration * 17150
    mesafe= round(mesafe,2)
  
    
    if mesafe>0 and mesafe<50:
        print "Mesafe:",mesafe," cm"
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
    elif mesafe>50 and mesafe<75:
        print "Mesafe:",mesafe," cm"
        GPIO.output(20,GPIO.HIGH)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(26,GPIO.HIGH)
    elif mesafe>75 and mesafe<100:
        print "Mesafe:",mesafe," cm"
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)
        print "Mesafe Disi"
    time.sleep(2)
GPIO.cleanup()