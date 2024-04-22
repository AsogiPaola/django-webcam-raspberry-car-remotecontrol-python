import cv2
import threading
import time
from django.shortcuts import render 
import datetime
from django.views.decorators import gzip
from django.template import Template, Context
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from yahboom.static.py.comandos import avanza, retrocede, para, izquierda, derecha, girar_izquierda, girar_derecha, main, detener_todo
from yahboom.static.py.ADSERVO import increase_angle, decrease_angle, increase_angle_h, decrease_angle_h, stop_servos
#from yahboom.static.py.automata import automata, brake
# Create your views here.
ENA = 16
IN1 = 20
IN2 = 21
ENB = 13
IN3 = 19
IN4 = 26
video_camera = None
@gzip.gzip_page
def Home(request):
    try:
        global video_camera
        if video_camera is None:
            video_camera = VideoCamera()
        #cam = VideoCamera()
        
        return render(request, 'yahboom/Templates/index.html', {'video_feed_url': '/video_feed'})
    except Exception as e:
        print(e)
        pass
    return render(request, 'yahboom/Templates/index.html')

def video_feed(request):
    try:
        global video_camera
        if video_camera is None:
            video_camera = VideoCamera()
        #cam = VideoCamera()
        return StreamingHttpResponse(gen(video_camera), content_type='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        print(e)
        pass
    return HttpResponse()

class VideoCamera(object):
    def __init__(self):
        self.video =cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
    
    def __del__(self):
        self.video.realease()
    
    def get_frame(self):
        _, jpeg = cv2.imencode('.jpg', self.frame)
        return jpeg.tobytes()
    
    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame =  camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-TYpe: image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')
   
def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre : %s / Edad:  %s </p>
    
    </body>
    </html>

    """ % (nombre ,edad)
    return HttpResponse(contenido)

def Templates(request):
    #abro documento que contiene a la plantilla
    platillaexterna = open("/home/robot/python/yahboom/yahboom/Templates/index.html")
    template = Template(platillaexterna.read())
    platillaexterna.close()

    contexto= Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

@csrf_exempt
def procesa_estado(request):
    if request.method == 'POST' and 'valor_estado' in request.POST:
        estado = request.POST['valor_estado']
        if estado == '1':
            avanza()
        elif estado == '2':
            izquierda()
        elif estado == '3':
            derecha()
        elif estado == '4':
            retrocede()
        elif estado == '5':
            para()
        elif estado == '6':
            girar_izquierda()
        elif estado == '7':
            girar_derecha()
            
        elif estado == '8':
            increase_angle()
        elif estado == '9':
            decrease_angle()
        elif estado == '10':
            increase_angle_h()
        elif estado == '11':
            decrease_angle_h()
        elif estado == '12':
            stop_servos()
            
        elif estado == '13':
            main(True)
        elif estado == '14':
            detener_todo(False)
            
        return JsonResponse({'message': 'Estado procesado correctamente'})
    else:
        return JsonResponse({'error': 'Solicitud incorrecta'})


def detener_autonomia():
    # Esta función levantará una excepción KeyboardInterrupt después de 1 segundo
    time.sleep(1)
    raise KeyboardInterrupt

  
