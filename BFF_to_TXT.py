import os

def BFF_to_TXT(path):
	'''
	This code is used to read the BFF file and save the content
	 into a .txt file under the same directory of the path.

	In order to read the file, path of .BFF file should be provided.
	'''

	file = os.path.basename(path)
	file_name = os.path.splitext(file)[0]
	txt_path = os.path.dirname(path)
	txt_file = open("%s/" % txt_path + file_name + ".txt", "w")

	fileData = open(path)
	for lines in fileData:
		print(lines)
		txt_file.writelines(lines)

	txt_file.close()



if __name__ == "__main__":
	BFF_to_TXT("/Users/zacooky/Desktop/Lazor_Project/yarn_5.bff")