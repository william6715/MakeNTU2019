import RPi.GPIO as GPIO

##馬達
class Servo:
    def __init__(self, CONTROL_PIN = 17, PWM_FREQ = 50):
        self.PWM_FREQ = PWM_FREQ
        GPIO.setmode(GPIO.BCM) ## it is mean use board number
        GPIO.setup(CONTROL_PIN, GPIO.OUT)##(number,output signal)
         
        self.pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ) ##(number,frequency)
        self.pwm.start(0)   ##dc代表佔空比0-100
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.pwm.stop()
        GPIO.cleanup()
        
    def angle_to_duty_cycle(self, angle=0):
        duty_cycle = (0.05 * self.PWM_FREQ) + (0.19 * self.PWM_FREQ * angle / 180)
        return duty_cycle

    def turn(self, angle):
        dc = self.angle_to_duty_cycle(angle)
        self.pwm.ChangeDutyCycle(dc)
         
