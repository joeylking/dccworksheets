
class AlarmClock:
    def __init__(self):
        self.current_time = "12:00 AM"
        self.alarm_time = "07:00 AM"
        self.alarm_on = False

    def display_time(self):
        print("Current time: ", self.current_time)

    def set_time(self):
        self.current_time = input("What is the current time? ")
        self.display_time()

    def toggle_alarm(self):
        if self.alarm_on == False:
            self.alarm_on = True
            print("The alarm is now on.")
        else:
            self.alarm_on = False
            print("The alarm is now off.")

    def display_alarm_time(self):
        print("Alarm set for: ", self.alarm_time)
        on_off = "on" if self.alarm_on == True else "off"
        print(f"The alarm is currently {on_off}.")
        alarm_switch = input("Would you like to change that? [y/n] ")
        if alarm_switch == "y":
            self.toggle_alarm()
        

    def set_alarm(self):
        self.alarm_time = input("For what time do you need an alarm? ")
        self.display_alarm_time()
