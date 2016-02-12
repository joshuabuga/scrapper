import inspect

class setter():
	"""docstring for setter"""

	def __init__(self, shon):

		self.set_boss("me")

		for name, value in shon.items():
			if hasattr(self, 'set_' + name) and inspect.ismethod(getattr(self, 'set_' + name)):
				getattr(self, 'set_' + name)(value)
			else:
				self.__dict__[name] = value

	def get_boss(self):
		return self.boss + 'tt'
	 		

	def set_boss(self, value):
		self.boss = value + ' Sasa'
		#return self.name 

	

st = setter({'boss' : 'Mwitu', 'age' : '78'})
print st.boss
print st.age