import numpy as NumPy


class KwCall:
	pass


class IterableAdaptor:

	@staticmethod
	def iterator(it):
		_this_x = it
		return python_HaxeIterator(_this_x.__iter__())


class IteratorAdaptor:

	@staticmethod
	def iterator(it):
		return python_HaxeIterator(it)


class DynamicIterationAdaptor:

	@staticmethod
	def iterator(it):
		it1 = it
		_this_x = it1
		return python_HaxeIterator(_this_x.__iter__())


class Script:

	@staticmethod
	def main():
		world_alcohol = NumPy.genfromtxt("world_alcohol.csv","U75",delimiter = ",",skip_header = True)
		third_column = world_alcohol[:,2]
		countries_canada = third_column == "Canada"
		first_column = world_alcohol[:,0]
		years_1984 = first_column == "1984"
		print(str(countries_canada))
		print(str(years_1984))


class python_HaxeIterator:

	def __init__(self,it):
		self.it = None
		self.x = None
		self.has = None
		self.checked = None
		self.checked = False
		self.has = False
		self.x = None
		self.it = it

	def next(self):
		if (not self.checked):
			self.hasNext()
		self.checked = False
		return self.x

	def hasNext(self):
		if (not self.checked):
			try:
				self.x = self.it.__next__()
				self.has = True
			except Exception as _hx_e:
				_hx_e1 = _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					self.has = False
					self.x = None
				else:
					raise _hx_e
			self.checked = True
		return self.has




Script.main()