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

	def get_name(self):
		return self.name

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
		self.length = 0


	def get_head(self):
		return self.head


	#add an appointment to the week
	def add_appointment(self, appointment):
		#if appointment is empty then just 
		if self.length == 0:
			self.head = appointment
		else:
			appointment.set_pointer(self.head)
			self.head = appointment
		self.length += 1
		print("Appoinment added!")


	#removes appointment from appointment list
	def remove_appointment(self, appointment_name):
		if self.length == 1:
			self.head = None
		else:
			curr_appointment = self.head
			prev_appointment = self.head
			while curr_appointment != None:
				if curr_appointment.get_name() == appointment_name:
					prev_appointment.set_pointer(curr_appointment.get_pointer())
				prev_appointment = curr_appointment
				curr_appointment = curr_appointment.get_pointer()
		#self.length -= 1
		print("Appointment removed!")


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
		if self.length > 0:
			week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",]
			for day in week:
				if self.has_appointment(day):
					self.print_day(day)
		else:
			print("You have no appointments scheduled for the week")



def main():
	calendar = AppointmentList()
	command = input("What do you wish to do?\n")

	while command != "end":

		#reads user input and adds an appointment
		if command == "add":
			name = input("Please enter a name for the appointment: ")
			times = input("Please enter a start a start day, a start time, an end day and an end time:\n")
			times = times.split()
			appointment = Appointment(name, times[0], times[1], times[2], times[3])
			calendar.add_appointment(appointment)

			
		#read user input and remove the task
		elif command == "remove":
			appointment_name = input("What is the name of the appointment you would like to remove?\n\n")
			calendar.remove_appointment(appointment_name)


		#read day and print the day
		elif command == "print day":
			day = input("Which day's appointments would you like to see?\n\n")
			print("\n============================\n")
			calendar.print_day(day)
			print("\n============================\n")


		#print the week
		elif command == "print week":
			print("\n============================\n")
			calendar.print_week()
			print("\n============================\n")

		else:
			print("Please enter a valid command")

		command = input("What do you wish to do?\n")

if __name__ == '__main__':
	main()