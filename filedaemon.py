import os
import sys, time, logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import subprocess
import _thread

#potential dangerous file extentions
ext = [".bat", ".cmd", ".vb", ".vbs", ".js", ".ws", ".wsf", ".wsc", ".wsh", ".wsc",
 ".ps1", ".ps1xml", ".ps2", ".msh", ".scf", ".lnk", ".inf"]

def validate(event):
	s = event.src_path.split("\\")

	file = s[-1]
	
	for i in ext:
		if file.endswith(i): 
			print("danger. found potential virus. do you want to delete this file")
			ans = input("y/n \n")
			if(ans == "y" or ans == "Y"):
				print("deleting...")
				time.sleep(3)
			
				os.remove(event.src_path)
			else:
				pass

def on_created(event):
	logging.info("Created - " + event.src_path)
	validate(event)
	
def on_deleted(event):
	logging.info("Deleted - " + event.src_path)
def on_modified(event):
	logging.info("Modified - " + event.src_path)
def on_moved(event):
	logging.info("Moved - " + event.src_path)

def watcher():
	logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(message)s", datefmt = "%Y-%m-%d  %H:%M:%S")
	
	path = sys.argv[1] if len(sys.argv) > 1 else "E:\\User\\Downloads"
	event_handler = LoggingEventHandler()
	
	file_event = FileSystemEventHandler()
	file_event.on_created = on_created
	file_event.on_deleted = on_deleted
	file_event.on_modified = on_modified
	file_event.on_moved = on_moved
	observer = Observer()
	observer.schedule(file_event, path, recursive=True)
	
	observer.start()
	
	
	
	
	try:
		while True:
			time.sleep(1)
			#print(logging.LogRecord.getMessage(event_handler))
	except KeyboardInterrupt:
		observer.stop()
	observer.join
	

	
watcher()
# def child(tid):
	# print("hello from thread ", tid)
	
# def parent():
	# i = 0
	# while True:
		# i += 1
		# _thread.start_new_thread(child, (12,))
		# if input() == "q": break
		
# parent()