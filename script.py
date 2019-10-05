cadena = "Hola Mundo"

#print(cadena)

#for c in cadena:
#	print(c)

class Dog:
	"""
	OOP  for a Dog class
	"""

	def __init__(self, name, age):
		self.name = name
		self.age = age


	def say_hello(self):
		 return f'Hi I am {self.name}'
# Instance

puppet = Dog("Teodoro",10)

# Getter

print(puppet.say_hello())

print('El nombre del perro es {}'.format(puppet.name))
print('El nombre del perro es {name}'.format(name=puppet.name))

print('El nombre del perro es {name} y su edad {age}'.format(
	name=puppet.name,
	age=puppet.age
	))







