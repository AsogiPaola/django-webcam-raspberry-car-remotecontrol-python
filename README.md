# django-webcam-raspberry-car-remotecontrol-python
In this project I mainly used the Python language, since I worked on a Raspberry Pi 4, here I implemented Django to use a local IP in the project, the car used is from Yahmboom, which has some pre-established codes, and has a camera , motors, servomotors, ultrasound sensor, and of course the raspberry.
![7](https://github.com/AsogiPaola/django-webcam-raspberry-car-remotecontrol-python/assets/106194428/2c4b0089-9a9c-4b7a-bf78-aee46e5e8c63)

This is the index.html page that contains 4 main sections, the home, the camera, the remote control and a footer, since it is a personal project, it does not have real information, and the html is a template edited with images of the internet, without any objective beyond research.
![5](https://github.com/AsogiPaola/django-webcam-raspberry-car-remotecontrol-python/assets/106194428/46299ac1-3709-4a2f-8bff-89358220ef5c)

This is the viewing section through the camera that is connected to the raspberry, it can be seen from the website, this part is specified in views.py
![6](https://github.com/AsogiPaola/django-webcam-raspberry-car-remotecontrol-python/assets/106194428/bd60faa1-ee3e-4e74-8cbd-6e6e3ea81023)

This is the remote control section and footer, a section of java code was added to the remote control section, for the operation of the buttons, button pressure actions and their connections to the different motors, the Images used for the buttons were taken from https://icon-icons.com/
![4](https://github.com/AsogiPaola/django-webcam-raspberry-car-remotecontrol-python/assets/106194428/f2d3ed42-3d55-4f63-b5ee-4c4c8c5b2b2b)


For the operation of the remote control, send through the front states assigned to each button, and its corresponding function that responded to these states, here are some examples, These are for the first buttons, which basically allow manual control of the directions of the car, being:
move forward, left, right, go back, stop, turn left and turn right, in that order states 1, 2, 3, 4, 5, 6 and 7 are assigned
![8](https://github.com/AsogiPaola/django-webcam-raspberry-car-remotecontrol-python/assets/106194428/efdc3393-3cd4-4bc2-abd9-ed4d1aff4cc9)

Now they are states 8, 9, 10, 11 and 12, which correspond to increasing vertical angle, decreasing vertical angle, increasing horizontal angle, decreasing horizontal angle and stopping servomotors.
![12](https://github.com/AsogiPaola/django-webcam-raspberry-car-remotecontrol-python/assets/106194428/a593f5ab-442d-410f-8d98-868e9a3b685a)

