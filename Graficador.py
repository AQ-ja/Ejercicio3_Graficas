from IA import Renderer, V2, color
from numpy import sin, cos


width = 1920
height = 1080

rend = Renderer(width, height)
rend.glColor(0.3, 1, 0.4)

rend.glLoadModel("modelos/silla.obj",V2(width/2, height/2), V2(5,5))


rend.glFinish("Ejercicio#3.bmp")