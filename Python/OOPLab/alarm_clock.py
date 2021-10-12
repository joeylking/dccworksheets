# As a developer, I want to create a AlarmClock class.

# As a developer, I want the AlarmClock class to have class instance variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).

# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.

# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# 1. Print the clock’s time to the terminal

# 2. Call the alarm clock’s change time method to change the time

# 3. Toggle the alarm clock’s on off switch

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
