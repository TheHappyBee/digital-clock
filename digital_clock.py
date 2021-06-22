from datetime import datetime
import tkinter as tk
from threading import Thread
import time


class clock():
     def __init__(self):
          self.display = tk.Tk()
     def start(self):
          def get():
               self.display.geometry("215x62")
               self.display.title("Clock")
               while True:
                    try:
                         now = datetime.now()
                         current_time = now.strftime("%H:%M %p") 
                         lbl = tk.Label(self.display, text=str(current_time),
                         background = 'black', font = ("Helvetica", 37),
                         foreground = 'red')
                         lbl.place(x=0, y=0)
                         time.sleep(0.1)
                    except:
                         break
          receive_thread = Thread(target=get)
          receive_thread.start()
          self.display.mainloop()
clock = clock()
clock.start()
