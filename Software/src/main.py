import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep
PWML="P9_14"
PWMR="P9_22"

class Motor:
    def __init__(self, PWMpin, dirForward, dirBackward):
        self.PWM = PWMpin
        self.forward = dirForward
        self.backward = dirBackward
        PWM.start(self.PWM, 0, 1000)
        PWM.set_duty_cycle(self.PWM, 0)
        GPIO.setup(self.forward, GPIO.OUT)
        GPIO.output(self.forward, GPIO.LOW)
        GPIO.setup(self.backward, GPIO.OUT)
        GPIO.output(self.backward, GPIO.LOW)

    def move(self, percentage):
        if percentage < 0:
            GPIO.output(self.forward, GPIO.LOW)
            GPIO.output(self.backward, GPIO.HIGH)
            if percentage < -100:
                percentage = -100
        else:
            GPIO.output(self.backward, GPIO.LOW)
            GPIO.output(self.forward, GPIO.HIGH)
            if percentage > 100:
                percentage = 100
        PWM.set_duty_cycle(self.PWM, abs(percentage))
    
    def stop(self):
        GPIO.output(self.backward, GPIO.LOW)
        GPIO.output(self.forward, GPIO.LOW)
        PWM.stop(self.PWM)
        PWM.cleanup()

            

def main():
    GPIO.setup("P8_17", GPIO.OUT)
    GPIO.output("P8_17", GPIO.HIGH)
    sleep(2)
    GPIO.output("P8_17", GPIO.LOW)
    motorL = Motor("P9_14", "P9_18", "P9_24")
    motorR = Motor("P9_22", "P9_26", "P9_30")
    motorL.move(50)
    motorR.move(-25)
    sleep(2)
    motorL.move(-75)
    motorR.move(-100)
    sleep(2)
    motorL.stop()
    
    

if __name__ == "__main__":
    main()