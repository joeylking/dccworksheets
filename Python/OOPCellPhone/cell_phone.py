class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = 1112223333
        self.contacts = {}
        self.messages = []
        self.vibrate = False

    def receive_text(self, message):
        print(message)
        self.messages.append(message)
    
    def toggle_vibrate(self):
        if self.vibrate == False:
            self.vibrate = True
            print("Vibrate mode turned on.")
        else:
            self.vibrate = False
            print("Vibrate mode turned off.")

    def send_text(self):
        recipient = input("To: ")
        outgoing_text = input("Your message: ")
        print(f"Sending '{outgoing_text}' to {recipient}")

    def add_contact(self):
        name = input("New contact's name: ")
        number = input("New contact's number: ")
        self.contacts[name] = number
