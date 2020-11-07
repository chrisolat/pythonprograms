import sys
import os

text = ""
if len(sys.argv) > 1:
	text = str(sys.argv[1])
if text == "":
	text = input("Enter Text: ")

count = 0

txt = text.split()

count = len(txt)
	
print(count)