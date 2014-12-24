#import picamera
import subprocess

#camera = picamera.PiCamera()

#camera.capture('image2.png')

proc = subprocess.Popen('../../../apriltags/build/bin/apriltags_demo' +' image.png', 
	shell=True,
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE,
	stdin=subprocess.PIPE)

so, se = proc.communicate()

print  "this is the return" + so 
print se
