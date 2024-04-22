#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Definition of  motor pin
# Definition of motor pin
def setup_pins():
    # Motor pins
    global IN1, IN2, IN3, IN4, ENA, ENB
    IN1 = 20
    IN2 = 21
    IN3 = 19
    IN4 = 26
    ENA = 16
    ENB = 13

    # RGB module pins
    global LED_R, LED_G, LED_B
    LED_R = 22
    LED_G = 27
    LED_B = 24

    # Ultrasonic module pins
    global EchoPin, TrigPin
    EchoPin = 0
    TrigPin = 1

    # Servo pin
    global ServoPin
    ServoPin = 23

#Ignore warning information
GPIO.setwarnings(False)
# Global variables
global motors_initialized
global ejecucion
motors_initialized = False
ejecucion = False

pwm_ENA = None
pwm_ENB = None
pwm_servo = None
#Motor pin initialization operation
def init_motors():
    global pwm_ENA, pwm_ENB, motors_initialized

    setup_pins()

    # Set up motor GPIO pins
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    
    #lEDS
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)

    # Set up PWM for motors
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    
    #servo_initiliazed = True
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)

    motors_initialized = True    
    

################################# 

def run(leftspeed, rightspeed):
    print("AVANCE AUTONOMO")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
#advance


def avanza():
    global motors_initialized, pwm_ENA, pwm_ENB
    try:
        GPIO.setmode(GPIO.BCM)
        if not motors_initialized:
            init_motors()
        print("AVANZANDO")
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        pwm_ENA.ChangeDutyCycle(50)
        pwm_ENB.ChangeDutyCycle(50)
    except Exception as e:
        print("Error:", e)

#back
def retrocede():
    global motors_initialized, pwm_ENA, pwm_ENB
    if not motors_initialized:
        init_motors()
    print("RETROCEDIENDO")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

#turn left
def izquierda():
    global motors_initialized, pwm_ENA, pwm_ENB
    if not motors_initialized:
        init_motors()
    print("MOVIENTO A LA IZQUIERDA")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

#turn right
def derecha():
    global motors_initialized, pwm_ENA, pwm_ENB
    if not motors_initialized:
        init_motors()
    print("MOVIENDO A LA DERECHA")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    

#turn left in place
def girar_izquierda():
    global motors_initialized, pwm_ENA, pwm_ENB
    if not motors_initialized:
        init_motors()
    print("GIRANDO A LA IZQUIERDA")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

#turn right in place
def girar_derecha():
    global motors_initialized, pwm_ENA, pwm_ENB
    if not motors_initialized:
        init_motors()
    print("GIRANDO A LA DERECHA")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

#brake
def para():
    global motors_initialized, pwm_ENA, pwm_ENB
    if not motors_initialized:
        init_motors()
    print("SIN MOVIMIENTO")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)


def Distance():
    GPIO.output(TrigPin,GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    t3 = time.time()
    
    while not GPIO.input(EchoPin):
        t4 = time.time()
        if (t4 - t3) > 0.03 :
            return -1

    t1 = time.time()

    while GPIO.input(EchoPin):
        t5 = time.time()
        if(t5 - t1) > 0.03 :
            return -1

    t2 = time.time()
    time.sleep(0.01)
#    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    return ((t2 - t1)* 340 / 2) * 100

def Distance_test():
    num = 0
    ultrasonic = []
    while num < 5:
            distance = Distance()
            while int(distance) == -1 :
                distance = Distance()
                #print("Tdistance is %f"%(distance) )
            while (int(distance) >= 500 or int(distance) == 0) :
                distance = Distance()
                #print("Edistance is %f"%(distance) )
            ultrasonic.append(distance)
            num = num + 1
            time.sleep(0.01)
    #print (ultrasonic)
    distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3])/3
    #print("distance is %f"%(distance) ) 
    return distance

#The servo rotates to the specified angle
def servo_appointed_detection(pos):
    global ServoPin
    GPIO.setup(ServoPin, GPIO.OUT)
    pwm_servo = GPIO.PWM(ServoPin, 50)
    #pwm_servo.start(2.5 + 10 * 160/180)
    time.sleep(0.05)
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)	

def servo_color_carstate():
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(0.08)
    para()
    servo_appointed_detection(0)
    time.sleep(0.8)
    leftdistance = Distance_test()
    servo_appointed_detection(180)
    time.sleep(0.8)
    rightdistance = Distance_test()
    servo_appointed_detection(90)
    time.sleep(0.8)
    frontdistance = Distance_test()
    
    if Distance_test() < 30 and rightdistance < 30 and frontdistance < 30:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        girar_derecha()
        time.sleep(0.58)
    elif Distance_test() >= rightdistance:
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        girar_izquierda()
        time.sleep(0.28)
    elif Distance_test() <= rightdistance:
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        girar_derecha()
        time.sleep(0.28)
        
def detener_todo(ejecute):
    global pwm_ENA, pwm_ENB, motors_initialized
    global ejecucion
    
    ejecucion = ejecute
    motors_initialized = False
    GPIO.setmode(GPIO.BCM)
    
     # Set up motor GPIO pins
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    # Detener los motores
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def main(ejecute):
    GPIO.setmode(GPIO.BCM)
    global ejecucion
    ejecucion = ejecute
    
    if not motors_initialized:
        init_motors()
    try:
        
        while ejecucion:
            distance = Distance_test()
            if distance > 50:
                run(55, 55)
            elif 30 <= distance <= 50:
                run(45, 45)
            elif distance < 30:
                servo_color_carstate()
           
    except KeyboardInterrupt:
        pass
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()    
if __name__ == "__main__":
    main()

