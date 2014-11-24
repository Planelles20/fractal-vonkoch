from Tkinter import *
from numpy import sin, cos, pi, sqrt
from time import sleep
from math import atan2


def copo_vonkoch(self, lado, n):
	x_vertice1 = 600
	y_vertice1 = 600

	x_vertice2 = x_vertice1-lado
	y_vertice2 = y_vertice1

	x_vertice3 = x_vertice1 - lado/2
	y_vertice3 = y_vertice1-sqrt(lado**2-(lado/2)**2)

	vonkoch(self, x_vertice1, y_vertice1, x_vertice2, y_vertice2, n)
	vonkoch(self, x_vertice2, y_vertice2, x_vertice3, y_vertice3, n)
	vonkoch(self, x_vertice3, y_vertice3, x_vertice1, y_vertice1, n)

	return 0


def vonkoch(self, xi, yi, xf, yf, n):
	if n== 0:
		self.create_line(xi, yi, xf, yf)
		n -=1

	elif n > 0:
		x1 = xi + (xf-xi)/3.0
		y1 = yi + (yf-yi)/3.0

		x3 = xf - (xf-xi)/3.0
		y3 = yf - (yf-yi)/3.0

		dx = x3 - x1
		dy = y3 - y1
		r = sqrt(dx**2 + dy**2)
		a = atan2(dy, dx)
		x2 = x1 + r*cos(a+pi/3)
		y2 = (y1 + r*sin(a+pi/3))

		vonkoch(self, xi, yi, x1, y1, n-1)
		vonkoch(self, x1, y1, x2, y2, n-1)
		vonkoch(self, x2, y2, x3, y3, n-1)
		vonkoch(self, x3, y3, xf, yf, n-1)

	else:
		return 0


tk = Tk()
canvas = Canvas(tk, width=701, height=701)

for i in range(6):
	copo_vonkoch(canvas, 500, i)
	canvas.pack()
	tk.update()
	sleep(1)
	
	