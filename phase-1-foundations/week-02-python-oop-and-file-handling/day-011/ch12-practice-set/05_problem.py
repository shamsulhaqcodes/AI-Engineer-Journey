# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Pakistani Railways.

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book_Ticket(self):
        print(f"The ticket is booked of train no: {self.trainNo}")

    def get_Status(self):
        print(f"Train No: {self.trainNo} is on the way")

    def get_Fare(self, fro, to):
        print(f"Train no: {self.trainNo} is going from {fro} to {to}")

t1 = Train(11019)
t1.book_Ticket()
t1.get_Status()
t1.get_Fare("Lahore", "Islamabad")