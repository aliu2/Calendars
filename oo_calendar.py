# an appointment class to be treated as a node and added in the linked list 
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
		# if the appointment starts and end on the same day then keep print statement more concise
		if self.start_day == self.end_day:
			return f"{self.name}:   |{self.start_day} {self.start_time} - {self.end_time}|"
		else:
			return f"{self.name}:   |{self.start_day} {self.start_time}| - |{self.end_day} {self.end_time}|"




# a linked list of appointments
class AppointmentList(object):
	def __init__(self):
		self.head = None
		self.length = 0


	# add an appointment to the week
	# adds appointment to the front of the list every time so runtime is always O(1)
	def add_appointment(self, appointment):
		# if list is empty then just add appointment to the head
		if self.length == 0:
			self.head = appointment
		else:
			appointment.set_pointer(self.head)
			self.head = appointment
		self.length += 1
		print("\nAppoinment added!")


	# removes appointment from appointment list
	def remove_appointment(self, appointment_name):
		if self.head.get_name() == appointment_name:
			self.head = self.head.get_pointer()
		else:
			curr_appointment = self.head
			next_appointment = self.head.get_pointer()
			while next_appointment != None:
				if next_appointment.get_name() == appointment_name:
					curr_appointment.set_pointer(next_appointment.get_pointer())
				curr_appointment = next_appointment
				next_appointment = next_appointment.get_pointer()
		self.length -= 1
		print("\nAppointment removed!")


	# check if a day has an appointment
	def has_appointment(self, day):
		curr_appointment = self.head
		while curr_appointment != None:
			if curr_appointment.get_day() == day:
				return True
			curr_appointment = curr_appointment.get_pointer()
		return False


	# print the appointments for a given day
	def print_day(self, day):
		# check if given appointment is even scheduled for this day
		if self.has_appointment(day):
			curr_appointment = self.head
			while curr_appointment != None:
				if curr_appointment.get_day() == day:
					print(curr_appointment)
				curr_appointment = curr_appointment.get_pointer()
		else:
			print(f"You have no appointments scheduled for {day.capitalize()}")


	# print all appointments for the week
	def print_week(self, week):
		if self.length > 0:
			for day in week:
				if self.has_appointment(day):
					self.print_day(day)
		else:
			print("You have no appointments scheduled for the week")



def main():
	calendar = AppointmentList()
	print("\n============================\n")
	print("Welcome to your calendar\n")
	print("The commands are:\nadd - to add an appointment\nremove - to remove an appointment\nprint day - to print your appointments for a given day\nprint week - to print your appointments for the week")
	print("\n============================\n")
	command = input("What do you wish to do?\n")
	week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",]

	# keep taking commands until the user types "end"
	while command != "end":

		# reads user input and adds an appointment
		if command == "add":
			name = input("Please enter a name for the appointment: ")
			times = input("Please enter a start day, a start time, an end day and an end time (in the format 'start-day HH:MM end-day HH:MM):\n")
			times = times.split()
			# checks to see if the input is correct
			if len(times) == 4 and times[0] in week and times[2] in week:
				appointment = Appointment(name.lower(), times[0].lower(), times[1], times[2].lower(), times[3])
				calendar.add_appointment(appointment)
			else:
				# error message for invalid day/time input
				print("\nPlease enter a valid start day, start time, end day and end time\n\n")

			
		# read user input and remove the task
		elif command == "remove":
			appointment_name = input("What is the name of the appointment you would like to remove?\n")
			if calendar.has_appointment(appointment_name):
				calendar.remove_appointment(appointment_name)
			else:
				#error message for attempting to remove an appointment that isn't scheduled
				print(f"\nYou don't have '{appointment_name}' scheduled anywhere\n\n")


		# read day and print the day
		elif command == "print day":
			day = input("Which day's appointments would you like to see?\n\n")
			print("\n============================\n")
			calendar.print_day(day)
			print("\n============================\n")


		# print the week
		elif command == "print week":
			print("\n============================\n")
			calendar.print_week(week)
			print("\n============================\n")

		else:
			print("Please enter a valid command")

		command = input("\nWhat do you wish to do?\n")

if __name__ == '__main__':
	main()
	print("Goodbye")