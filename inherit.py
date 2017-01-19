class Parent(object):
	def implicit(self):
		print("PARENT implicit()")
	def override(self):
		print("PARENT override()")
	def altered(self):
		print("PARENT altered()")

class Child(Parent):
	def __init__(self, stuff):
		self.stuff = stuff
		super(Child,self).__init__()
		
	def override(self):
		print("CHILD override()")
	def altered(self):
		print("CHILD before parent.altered()")
		super(Child, self).altered()
		print("CHILD after parent.altered()")

dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.override()
son.override()

dad.altered()
son.altered()