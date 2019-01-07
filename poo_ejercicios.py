import math

class Punto:
	x = 0
	y = 0
	
	def __init__(self, x = 0,y = 0):
		self.x = x
		self.y = y
	
	def __str__(self):
		return("{},{}".format(self.x, self.y))
	def cuadrante(self):
		if self.x > 0 and self.y > 0:
			return("Cuandrante 1")
		elif self.x < 0 and self.y > 0:
			return("Cuadrante 2")
		elif self.x < 0 and self.y < 0:
			return("Cuadrante 3")
		elif self.x > 0 and self.y < 0:
			return("Cuadrante 4")
		else:
			return("Origen")
	def vector(self,o):
		xv = o.x - self.x
		yv = o.y - self.y
		return("Vector resultante {},{}".format(xv,yv))
	def distancia(self, o):
		distancia = math.sqrt((o.x - self.x)**2 + (o.y - self.y)**2)   
		return(distancia)


class Rectangulo:
	x1 = 0
	y1 = 0
	x2 = 0 
	y2 = 0
	
	def __init__(self,a,b):
		self.x1 = a.x
		self.y1 = a.y
		self.x2 = b.x
		self.y2 = b.y
	def base(self):
		return(self.x2 - self.x1)
	def altura(self):
		if self.y2 > self.y1:
			return(self.y2 - self.y1)
		else:
			return(self.y1 - self.y2)
	def area(self):
		return(self.base()*self.altura())

#if a.distancia(d) > b.distancia(d) and a.distancia(d) > c.distancia(d):
#    print("El punto A es el más lejano")
#elif b.distancia(d) > a.distancia(d) and b.distancia(d) > c.distancia(d):
#    print("El punto B es el mas lejano")
#else: 
#    print("El punto C es el más lejano")