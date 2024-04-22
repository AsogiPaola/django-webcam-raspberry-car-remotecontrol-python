import RPi.GPIO as GPIO
import time

# Definir el pin GPIO para el servo
ServoPin_v = 9  # Vertical, mueve la cámara hacia atrás y adelante
ServoPin_h = 11 #Horizontal. miueve el servomotot hacia los lados

# Configurar la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ServoPin_v, GPIO.OUT)
GPIO.setup(ServoPin_h, GPIO.OUT)

# Crear un objeto PWM con una frecuencia de 50Hz (20ms)
pwm_v = GPIO.PWM(ServoPin_v, 50)
pwm_v.start(0)
pwm_h = GPIO.PWM(ServoPin_h, 50)
pwm_h.start(0)

# Función para mover el servo a un ángulo específico
def move_servo_v(angle):
    duty_cycle = 2 + (angle / 18)
    pwm_v.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

# Función para aumentar los grados del servomotor en 10
def increase_angle():
    global current_angle
    current_angle += 10
    if current_angle > 180:
        current_angle = 180
    move_servo_v(current_angle)
    print(f"El ángulo actual del servomotor es: {current_angle} grados")
    time.sleep(0.5)

# Función para disminuir los grados del servomotor en 10
def decrease_angle():
    global current_angle
    current_angle -= 10
    if current_angle < 0:
        current_angle = 0
    move_servo_v(current_angle)
    print(f"El ángulo actual del servomotor es: {current_angle} grados")
    time.sleep(0.5)
###########################################
#servo motor horizontal
def move_servo_h(angle):
    duty_cycle = 2 + (angle / 18)
    pwm_h.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

# Función para aumentar los grados del servomotor en 10
def increase_angle_h():
    global current_angle
    current_angle += 10
    if current_angle > 180:
        current_angle = 180
    move_servo_h(current_angle)
    print(f"El ángulo del es: {current_angle} grados")
    time.sleep(0.5)

# Función para disminuir los grados del servomotor en 10
def decrease_angle_h():
    global current_angle
    current_angle -= 10
    if current_angle < 0:
        current_angle = 0
    move_servo_h(current_angle)
    print(f"El ángulo del es: {current_angle} grados")
    time.sleep(0.5)

# Ángulo inicial del servo
current_angle = 130

# Función para procesar el estado recibido
def procesa_estado(estado):
    if estado == 8:
        print("AUMENTANDO ANGULO VERTICAL")
        increase_angle()
    elif estado == 9:
        print("DISMINUYENDO ANGULO VERTICAL")
        decrease_angle()
    elif estado == 10:
        print("MOVIENDO A LA IZQUIERDA")
        decrease_angle_h()
    elif estado == 11:
        print("MOVIENDO A LA DERECHA")
        decrease_angle_h()
    
    else:
        print("Estado no reconocido")

def stop_servos():
    pwm_v.ChangeDutyCycle(0)
    pwm_h.ChangeDutyCycle(0)
    print("SERVO MOTORES DE LAS CAMARAS QUIETOS")

