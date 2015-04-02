import picamera
import subprocess
import sys, time

x = int(sys.argv[1])
y = int(sys.argv[2])



camera = picamera.PiCamera()
camera.resolution = (1024,768)


camera.capture('image3.jpeg', use_video_port=True, resize =(x,y))

argument = ' -W '+ str(x) + ' -H ' + str(y) +' image3.jpeg'

print argument

# proc = subprocess.Popen('../../../apriltags/build/bin/apriltags_demo' + argument, 
# 	shell=True,
# 	stdout = subprocess.PIPE,
# 	stderr = subprocess.PIPE,
# 	stdin=subprocess.PIPE)

proc = subprocess.Popen('../apriltags/build/bin/apriltags_demo' + argument, 
	shell=True,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	stdin=subprocess.PIPE)

so, se = proc.communicate()

# print so , se


print  "this is the return" + so 
print se
