import subprocess

class TestClass(object):
	def __init__(self):
		print(f"This is the class in module1.py")


def main(): 
	subprocess.Popen("./cpp_files/file.out") #This process calls a compiled c++ file located inside the cpp_files directory.


if __name__ == "__main__":
	main()
