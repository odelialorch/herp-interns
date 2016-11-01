def square(x):
	return (x*x)

def favorite_color(name):
	names = ['Ava', 'Crystal', 'Renee', 'Stephanie', 'Elena']
	favcolors = ['Blue', 'Blue', 'Purple', 'Blue', 'Silver']
	x = names.index(name)	
	return (favcolors[x])

def reverse(x):
	value = len(x) - 1
	y = []
	while (value >= 0):
		y.append(x[value])
		value = value - 1
	return (y)
