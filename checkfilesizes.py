import os

def search():
	g = os.walk(r'C:')
	
	for i in g:
		for x in i:
			for y in x:
				print(file_size(g))
				
				
				


def convert_bytes(num):
	
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return (num, x)
		num /= 1024.0
		

def file_size(file_path):
	if os.path.isfile(file_path):
		file_info = os.stat(file_path)
		
		return convert_bytes(file_info.st_size)
		
search()