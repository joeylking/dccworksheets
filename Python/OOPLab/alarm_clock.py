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
        self.current_time = ""
        self.alarm_time = ""
        self.alarm_on = False