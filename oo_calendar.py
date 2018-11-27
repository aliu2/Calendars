#an appointment class to be treated as a node and added in the linked list 
class Appointment(object):
	def __init__(self, name, start_day, start_time, end_day, end_time):
		self.name = name
		self.start_day = start_day
		self.start_time = start_time
		self.end_day = end_day
		self.end_time = end_time
		self.pointer = None


	def get_day(self):
		return self.start_day

	def get_pointer(self):
		return self.pointer

	def set_pointer(self, appointment):
		self.pointer = appointment

	def __str__(self):
		#if the appointment starts and end on the same day then keep print statement more concise
		if self.start_day == self.end_day:
			return f"{self.name}:   |{self.start_day} {self.start_time} - {self.end_time}|"
		else:
			return f"{self.name}:   |{self.start_day} {self.start_time}| - |{self.end_day} {self.end_time}|"




#a linked list of appointments
class AppointmentList(object):
	def __init__(self):
		self.head = None


	def get_head(self):
		return self.head

	#check if calendar is empty or not
	def is_empty(self):
		return self.head == None


	#add an appointment to the week
	def add_appointment(self, appointment):
		#if appointment is empty then just 
		if self.is_empty():
			self.head = appointment
		else:
			appointment.set_pointer(self.head)
			self.head = appointment


	#check if a day has an appointment
	def has_appointment(self, day):
		curr_appointment = self.head
		while curr_appointment != None:
			if curr_appointment.get_day() == day:
				return True
			curr_appointment = curr_appointment.get_pointer()
		return False


	#print the appointments for a given day
	def print_day(self, day):
		if self.has_appointment(day):
			curr_appointment = self.head
			while curr_appointment != None:
				if curr_appointment.get_day() == day:
					print(curr_appointment)
				curr_appointment = curr_appointment.get_pointer()
		else:
			print(f"You have no appointments scheduled for {day.capitalize()}")


	#print all appointments for the week
	def print_week(self):
		week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",]
		for day in week:
			if self.has_appointment(day):
				self.print_day(day)



def main():
	appointment1 = Appointment("walk dog", "monday", "14:00", "monday", "15:00")
	appointment2 = Appointment("get groceries", "monday", "16:00", "monday", "19:00")
	appointment3 = Appointment("do assignments", "tuesday", "15:00", "wednesday", "16:00")
	calendar = AppointmentList()
	calendar.add_appointment(appointment1)
	calendar.add_appointment(appointment2)
	calendar.add_appointment(appointment3)
	calendar.print_day("monday")

if __name__ == '__main__':
	main()