import os


def convert_bytes(num):
	
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return (num, x)
		num /= 1024.0
		

def file_size(file_path):
	if os.path.isfile(file_path):
		file_info = os.stat(file_path)
		
		return convert_bytes(file_info.st_size)

def remove(file_path):
	print(file_path)                          #deleter
	os.system("del /Q " + file_path)

def changefiletype(file_path):
	os.system("move " + file_path + " " + file_path[:-4] + ".jpg")
	

#file = input(r"Input file path ")
#file_path = file
'''print (file_size(file_path))'''
#remove(file_path)


for i in os.listdir():
	#if(i.endswith(".pdf")):
		#print(i)
		changefiletype(i)
	#if (((file_size(i)[1]) == 'KB') and i.startswith('f')):  #i.startswith was for a purpose.. not needed
		#remove(i)     #commented for safety purposes ahah:)
	