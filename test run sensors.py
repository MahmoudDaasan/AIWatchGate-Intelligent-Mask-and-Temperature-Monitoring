import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning
LED_PIN = 7               # Define PIN for LED
IR_PIN = 29                 # Define PIN for IR Sensor
GPIO.setup(LED_PIN,GPIO.OUT)   # Set pin function as output
GPIO.setup(IR_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)   # Set pin function as input  
while (1):
    #Check switch pressed or not 
    if GPIO.input(IR_PIN) == GPIO.LOW:
        print ("Obstacle Detected and LED ON")
        GPIO.output(LED_PIN,GPIO.LOW)  #LED ON                 
    else :
        print ("Obstacle released and LED OFF")
        GPIO.output(LED_PIN,GPIO.HIGH)   # LED OFF