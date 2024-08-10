from random import randint

class Train:

    def __init__(self):
        self.trainNo = 12399 

    def booking(self, fro, to):
        print(f"Your ticket is booken in trainNo: {self.trainNo} from {fro} to {to}")

    def status(self):
        print(f"the train {self.trainNo} is running on time")

    def fare(self, fro, to):
        print(f"Ticket fare in train number :{self.trainNo} from {fro} to {to} is {randint(1000, 1500)}")

obj = Train()
obj.booking("Bhilwara", "Delhi")
obj.status()
obj.fare("Bhilwara", "Delhi")

        