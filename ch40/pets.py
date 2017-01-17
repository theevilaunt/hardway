class Animal(object):
	def __init__(self, name):
		self.name = name

	def call(self):
		print(self.name)

	def speak(self):
		print("%s makes a noise" % self.name)

class Dog(Animal):
	def speak(self):
		print(self.name + " barks")

class Cat(Animal):
	def speak(self):
		print(self.name + " meows")

class Bird(Animal):
	def speak(self):
		print(self.name + " tweets")

class Horse(Animal):
	def speak(self):
		print(self.name + " whinnies")

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pets = {}
	def add_pet(self, type, name):
		if type == 'dog':
			dog = Dog(name)
			print("after adding dog: %s named %s" % (dog, dog.name))
		elif type == 'cat':
			cat = Cat(name)
	def list_pets(self):
		for a_pet in self.pets:
			print("my pet %s named %s" % a_pet)


my_horse = Horse('warlock')
my_horse.call()
my_horse.speak()

my_bird = Bird('ciel')
my_bird.call()
my_bird.speak()

my_animal = Animal('bunky')
my_animal.call()
my_animal.speak()