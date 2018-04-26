from tkinter import *
from tkinter import ttk
from clockable import Clockable
from alarm import Alarm
import time
import random

root = Tk()
root.title('Clock')

digital_clocks = []

def random_timezone():
    available_timezones = [time.gmtime, time.localtime]
    return random.choice(available_timezones)

for i in range(0,3):
    clock = Label(root, font = ("Times", 50 , "bold"), bg = "white")
    clock.grid(row = i, column = 1, columnspan = 2)
    digital_clocks.append(Clockable(clock, random_timezone()))

alarm = Alarm()

alarm_hour = StringVar(root)
alarm_hour.set(alarm.hours[0])
e = ttk.Combobox(root, textvariable = alarm_hour, values = alarm.hours)
e.grid(row = 3, column = 1)

alarm_minute = StringVar(root)
alarm_minute.set(alarm.minutes[0])
e = ttk.Combobox(root, textvariable = alarm_minute, values = alarm.minutes)
e.grid(row = 3, column = 2)

b = Button(root,text='Configurar alarme', command = lambda: alarm.set_alarm(alarm_hour.get(), alarm_minute.get(), digital_clocks))
b.grid(row = 4, column = 1)

b = Button(root,text='Resetar alarmes', command = lambda: alarm.reset_alarms(alarm_hour, alarm_minute, digital_clocks))
b.grid(row = 4, column = 2)

for clock in digital_clocks:
    clock.start()

root.mainloop()