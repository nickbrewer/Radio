import RPi.GPIO as GPIO
import time
import sys
import time
import atexit
import traceback
import Adafruit_GPIO as GPIO
import os
import atexit
from time import sleep
import Image
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO.SPI as SPI

stderr = sys.stderr.write;


DC = 22
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0
gpio = GPIO.get_platform_gpio()
gpio.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch for Bluetooth
gpio.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch for Aux
gpio.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch for RPi
state = 0
btaux = 0

# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()

# Execute system command sub-routine
def exec_command(cmd):
     result = ""
     p = os.popen(cmd)
     for line in p.readline().split('\n'):
          result = result + line
     return result

def image():
	station = exec_command("mpc current").split(" ")
	if station[0] == "KSUA" and btaux == 0:
		#print station[0]
		image = Image.open('/home/pi/radio/images/ksua.jpg') # Load an image.	
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels.						
		disp.display(image)  # Draw the image
		
	elif station[0] == "Radio":
		#print station[0] 
		image = Image.open('/home/pi/radio/images/rfb.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels.			
		disp.display(image)  # Draw the image  
		
	elif station[0] == "KEXP.ORG":
		#print station[0]
		image = Image.open('/home/pi/radio/images/kexp.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image 	

	elif station[0] == "KCRW":
		#print station[0]
		image = Image.open('/home/pi/radio/images/kcrw.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image 
		
	elif station[0] == "WNYC":
		#print station[0]
		image = Image.open('/home/pi/radio/images/wnyc.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image 	
		
	elif station[0] == "KUAC":
		#print station[0]
		image = Image.open('/home/pi/radio/images/kuac.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image 	
		
	elif station[0] == "WFMU":
		#print station[0]
		image = Image.open('/home/pi/radio/images/wfmu.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image 	
		
	elif station[0] == "KRUA":
		#print station[0]
		image = Image.open('/home/pi/radio/images/krua.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image	
		
	elif station[0] == "KUTX":
		#print station[0]
		image = Image.open('/home/pi/radio/images/kutx.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image							

	elif station[0] == "WICB":
		#print station[0]
		image = Image.open('/home/pi/radio/images/wicb.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image		

	elif station[0] == "WMUA":
		#print station[0]
		image = Image.open('/home/pi/radio/images/wmua.jpg') # Load an image.		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image	

def bt():
		exec_command("mpc stop")
		image = Image.open('/home/pi/radio/images/bluetooth.jpg') # Load an image. 		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image

def aux():			
		exec_command("mpc stop")
		image = Image.open('/home/pi/radio/images/aux.jpg') # Load an image. 		
		image = image.rotate(90).resize((240, 320)) # Resize the image and rotate it so it's 240x320 pixels. 			
		disp.display(image)  # Draw the image 

### Main routine ###  
if __name__ == "__main__":
        exec_command("service mpd start") 
        exec_command("mpc clear")         
     	exec_command("mpc load feblist") #Put name of playlist here, but leave off the .m3u part
        exec_command("mpc play")           
        exec_command("mpc volume 100") 
        disp.clear()
        print "Use Ctl-C to exit"

while True:
    try: 
		station = exec_command("mpc current").split(" ")
		print station[0]
		image()
		input_state = gpio.input(26)
		if input_state == False:
			exec_command("mpc next")
			time.sleep(0.2)
		
		input_state2 = gpio.input(19)
		if input_state2 == False:
			exec_command("mpc prev")
			time.sleep(0.2)  
			
		#input_state3 = gpio.input(13)
		#if input_state3 == False and state == 0:
		#	exec_command("mpc pause")
		#	state = 1
		#	print "paused"
		#	time.sleep(0.5) 
		
		#input_state4 = gpio.input(13)	
		#if input_state4 == False and state == 1:
		#	exec_command("mpc play")
		#	state = 0
		#	print "play"
		#	time.sleep(0.5)

		input_state5 = gpio.input(21)	
		if input_state5 == False:
			bt()
			time.sleep(0.5)	
			
		input_state6 = gpio.input(20)	
		if input_state6 == False:
			aux()
			time.sleep(0.5)				

		input_state6 = gpio.input(16)	
		if input_state6 == False:
			exec_command("mpc play")
			time.sleep(0.5)
    	 
    except KeyboardInterrupt:
		exec_command("mpc stop")
		disp.clear()
		print "\nExit"
		sys.exit(0)		                   
