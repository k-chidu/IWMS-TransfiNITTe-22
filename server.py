from time import sleep
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if(event.src_path == "./hostel_in.txt"):
            os.system("python3 hack.py")
        if(event.src_path == "./hostel_out.txt"):
            os.system("python3 hack.py")
        if(event.src_path == "./campus_out.txt"):
            os.system("python3 hack.py")
        if(event.src_path == "./campus_in.txt"):
            os.system("python3 hack.py")

observer = Observer()
observer.schedule(Handler(), ".")
observer.start()

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()