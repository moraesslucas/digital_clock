import sys
from threading import Thread
import time

class Clockable(Thread):

    def __init__ (self, clock, timezone):
        Thread.__init__(self)
        self.alarm = ""
        self.clock = clock
        self.timezone = timezone

    def update_clock(self):
        time_string = time.strftime("%H:%M:%S", self.timezone())
        if (time_string == self.alarm): self.setBackground("red")
        self.clock.config(text=time_string)
        self.clock.after(200, self.update_clock)

    def set_alarm(self, hours, minutes):
        self.alarm = "{0}:{1}:00".format(hours, minutes)

    def set_background(self, color):
        self.clock.config(bg = color)

    def run(self):
        self.update_clock()