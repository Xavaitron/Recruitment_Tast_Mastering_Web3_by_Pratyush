class slot:
    def __init__(self, time: str, subsport: str, sport: str):
        self.time = time
        self.subsport = subsport
        self.sport = sport
        self.status = True

    def book_slot(self, user: object):  # Accepts user object
        if self.status:
            self.status = False
            self.booked_by = user.name  # Use user attributes
            self.booked_by_rollno = user.rollno
            print(f"Slot booked successfully!")
        else:
            print(f"Sorry! But this slot is already booked by {self.booked_by}({self.booked_by_rollno})")

    def cancel_slot(self,user :object):
        if self.booked_by_rollno == user.rollno:
            self.status = True
            self.booked_by = ""
            self.booked_by_rollno = None
            print(f"Slot cancelled successfully!")
        elif self.booked_by_rollno != user.rollno:
            print("Authentication Failed!:You cannot cancel this slot as you have not booked this slot")
        else:
            print("THis slot has not been booked yet")


    def display_availability(self):
        if self.status:
            print("This slot is available")
        else:
            print("This slot is not available")

class user:
    def __init__(self, name: str, rollno: int):
        self.name = name
        self.rollno = rollno
        self.history = []

    def book_slot_by(self, slot: object):
        slot.book_slot(self) # Pass the user object
        self.history.append(transaction(self , slot, "Booked"))

    def cancel_slot_by(self,slot : object):
        slot.cancel_slot(self)
        self.history.append(transaction(self, slot , "Cancelled"))

    def display_history(self):
        print(f"History for user {self.name}({self.rollno}):")
        for transaction in self.history:
            print(f"    {transaction.type} slot for {transaction.slot.sport} on {transaction.slot.subsport} at {transaction.slot.time}")

class sport:
    def __init__(self,sport_name : str):
        self.sport_name = sport_name
        self.slots_sport = []

    def add_slot(self,slot):
        if slot.sport.strip().lower() == self.sport_name.strip().lower():
            self.slots_sport.append(slot)
        else:
            print("The slot sport does not match with sport name ")

    def remove_slot(self,slot):
        self.slots_sport.remove(slot)

    def display_available_slots(self):
        print(f"The available slots in {self.sport_name} are:")
        for slot in self.slots_sport:
            if slot.status == True:
                print(f"At {slot.subsport} from {slot.time}")

class transaction:
    def __init__(self,user : object,slot : object, type : str):
        self.user = user
        self.slot = slot
        self.type = type


    
# Testing
table_tennis = sport("table_tennis")
slot1 = slot("5pm-6pm", "table1", "table_tennis")
table_tennis.add_slot(slot1)
slot2 = slot("5pm-6pm", "table2", "table_tennis")
table_tennis.add_slot(slot2)
slot3 = slot("6pm-7pm", "table1", "table_tennis")
table_tennis.add_slot(slot3)
slot4 = slot("6pm-7pm", "table2", "table_tennis")
table_tennis.add_slot(slot4)

slot1.display_availability()#Check availability of slot

table_tennis.display_available_slots()

user1 = user("Pratyush Singh", 230784)
user1.book_slot_by(slot1)#Booking the slot by user1

slot1.display_availability()#Slot availability changes to not avaialble

table_tennis.display_available_slots()

user2 = user("Shivansh", 230977)
user2.book_slot_by(slot1)  # Attempt to book already booked slot

user3  = user("Aayush Dubey",230026)
user3.book_slot_by(slot2)
user3.cancel_slot_by(slot2)
user3.display_history()#Showing history of a user
