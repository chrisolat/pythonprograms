# file search
import sys


import os
file = ""
if len(sys.argv) > 1:
	file = str(sys.argv[1])
if file == "":
	file = input("enter file name(keyword only): ")


print("Results: \n")

def search(file):
	g = os.walk(r'C:')
	
	for i in g:
		for x in i:
			for y in x:
				if file in y:
				
					print(str(i[0])+str(y))
				

"""for i in file:
	x = []           #was for some advanced stuffs
	x.append(i)"""
	
	
	
filetitle = file.title()
search(file)
search(filetitle)

		