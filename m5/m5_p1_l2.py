class Point:

	def __init__(self, x, y):
		self.x = x 
		self.y = y 

	def __add__(self, other):
		new_x = self.x + other.x
		new_y = self.y + other.y 
		return Point(new_x, new_y)

	def subtract(self, other):
		new_x = self.x - other.x
		new_y = self.y - other.y 
		return Point(new_x, new_y)
	
	def multiply(self, other):
		new_x = self.x * other.x
		new_y = self.y * other.y 
		return Point(new_x, new_y)

	def dist(self, other):
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5	

	def show_point(self):
		return self.x, self.y


p1 = Point(4, 1)
p2 = Point(3, -2)

p3 = p1 + p2
print(f'p1{p1.show_point()} + p2{p2.show_point()} = p3{p3.show_point()}')

p4 = p1.subtract(p2)
print(f'p1{p1.show_point()} - p2{p2.show_point()} = p4{p4.show_point()}')

p5 = p1.multiply(p2)
print(f'p1{p1.show_point()} * p2{p2.show_point()} = p5{p5.show_point()}')

print(f'Расстояние между точками p1 и p2 - {p1.dist(p2)}')