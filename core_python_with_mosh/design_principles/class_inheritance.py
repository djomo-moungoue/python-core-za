class Parent: # parent class

	def __init__(self):
		print('Component Class object created...')

	def parent_method(self): # parent class method
		print('Component Class Method called...')

class Child(Parent): # child class inheriting parent class

	def __init__(self): # child class constructor
		print('Child Class object created...')

	def child_method(self): # child class method
		print('Child Class Method called...')

obj = Child() # creating object of child class

obj.parent_method() # calling parent class m1() method

obj.child_method() # calling child class m2() method