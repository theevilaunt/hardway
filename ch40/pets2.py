class Pet(object):
	def __init__(self, name, animal):
		self.name = name
		self.type = animal

	def speaks(self):
		if self.type == 'dog':
			print('bark')
		elif self.type == 'cat':
			print('meow')
		elif self.type == 'bird':
			print('tweet')
		elif self.type == 'horse':
			print('whinny')

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pets = {}

	def add_pet(self, pet):
		self.pets[pet.name] = pet.type


my_dog = Pet('kiki', 'dog')
my_dog.speaks()

my_bird = Pet('ciel', 'bird')
my_bird.speaks()

me = Person('heidi')
me.add_pet(my_dog)
me.add_pet(my_bird)
print(me.pets)
for pet_name, pet_type in me.pets.items():
	print("%s is my %s" % (pet_name, pet_type))
	my_pet = Pet(pet_name, pet_type)
	my_pet.speaks()



