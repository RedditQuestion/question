"""
Problem[1]: How can I make it so that this package can be imported without a 'ModuleNotFoundError'?
error occures in the line 7;
"""
try:
	from module1 import *
except:
	from package.module1 import *

"""
I import all the classes in the module1.py file because they are used in module2.py and I can simply 
call the "TestClass" class in module1.py using 

>>		import package
>>		package.TestClass (Works fine)
"""
