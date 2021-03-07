'''
The same problem[1] arises here if this file is called directly
'''
try:
	from module1 import *	
except ModuleNotFoundError:
	from package import TestClass #works because it is imported in __init__.py file

def main(): #this is defined as the entry point whenever package command is used. 
	TestClass() #just a class that prints a message; class defined inside moduel1.py 

if __name__ == "__main__":
	main()
