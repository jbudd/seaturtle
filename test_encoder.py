import RPi.GPIO as GPIO
import time 
time_stamp = time.time()

GPIO.setmode(GPIO.BOARD)

Motor1A = 31
Motor1B = 33		
Motor1E = 29

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(35,GPIO.IN)
motor = GPIO.PWM(Motor1E,500)
motor.start(0)


GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)

degrees = 360


count_degrees = int(abs(degrees)/18)
	#use interrupts to count number of encoder pulses
count = 0
while(count < count_degrees):
	
	motor.ChangeDutyCycle(60)
	GPIO.wait_for_edge(35,GPIO.FALLING)
	global time_stamp
	time_now = time.time()
	if(time_now - time_stamp) >= 0.13:
		print "increasing count count "
		count += 1
	time_stamp = time_now



motor.stop()
GPIO.cleanup()


	


