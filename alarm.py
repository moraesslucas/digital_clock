class Alarm:
    def __init__(self):
        self.hours = []
        self.minutes = []
        for i in range(0, 24):
            self.hours.append(str(i).zfill(2))

        for i in range(0, 60):
            self.minutes.append(str(i).zfill(2))

    def set_alarm(self, hours, minutes, clocks):
        for clock in clocks:
            clock.setAlarm(hours, minutes)

    def reset_alarms(self, hours, minutes, clocks):
        hours.set("00")
        minutes.set("00")
        for clock in clocks:
            clock.setAlarm("00", "00")
            clock.setBackground("white")
