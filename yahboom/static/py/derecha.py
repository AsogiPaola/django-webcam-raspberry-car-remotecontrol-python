import RPi.GPIO as GPIO
# Define los pines GPIO
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)
#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
global pwm_ENA
global pwm_ENB
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
pwm_ENA = GPIO.PWM(ENA, 2000)
pwm_ENB = GPIO.PWM(ENB, 2000)
pwm_ENA.start(0)
pwm_ENB.start(0)

#hacia derecha
def derecha():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)


try:
    derecha()
    
except KeyboardInterrupt:
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup() 

