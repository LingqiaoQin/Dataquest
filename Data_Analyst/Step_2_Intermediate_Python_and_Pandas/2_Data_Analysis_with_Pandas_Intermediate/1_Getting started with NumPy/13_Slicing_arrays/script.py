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
		def _hx_local_0():
			d = None
			kwArgs = dict()
			kwArgs["dtype"] = "U75"
			kwArgs["skip_header"] = True
			kwArgs["delimiter"] = ","
			d = kwArgs
			return d
		world_alcohol = NumPy.genfromtxt("world_alcohol.csv",**_hx_local_0())
		first_twenty_regions = world_alcohol[0:20,1:3]
		print(str(first_twenty_regions))


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