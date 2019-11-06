import os

class BFF_Reader():
	def __init__(self, file_path):
		self.file_path = file_path

	def read_file(self):
		#read BFF file.
		File = open(self.file_path, "r")
		return File.read()

	def split_by_line(self):
		#split file by lines and return all lines as a list. 
		return self.read_file().strip().split("\r\n")

	def get_grid(self):
		#Return grid as a list of list.
		lines = self.split_by_line
		pass



	print("Works fine!")



if __name__ == '__main__':
	BR = BFF_Reader("/Users/zacooky/Desktop/Lazor_Project/BFF_TXT/mad_1.bff")
	BR.read_file()
	print(BR.get_grid())
