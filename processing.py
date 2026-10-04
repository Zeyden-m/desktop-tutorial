import processing
	
a = 0

def setup(): 
	size(200, 200)
	background(0)
	noStroke()
	fill(102)

def draw():
	background(0)
	global a
	a = (a + 1) % width
	rect(a, 10, 2, 80)
