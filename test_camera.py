import picamera
import subprocess
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])



camera = picamera.PiCamera()
camera.resolution = (x,y)

camera.capture('image3.jpeg', use_video_port=True)

argument = ' -W '+ str(x) + ' -H ' + str(y) +' image3.jpeg'

# print argument

proc = subprocess.Popen('../apriltags/build/bin/apriltags_demo' + argument, 
	shell=True,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	stdin=subprocess.PIPE)

so, se = proc.communicate()

print  "this is the return" + so 
print se
