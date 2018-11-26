#an appointment class to be treated as a node and added in the linked list 
class Appointment(object):
	def __init__(self, name, start_day, start_time, end_day, end_time):
		self.name = name
		self.start_day = start_day
		self.start_time = start_time
		self.end_day = end_day
		self.end_time = end_time
		self.pointer = None

	def get_name(self):
		return self.name

	def get_start_day(self):
		return self.start_day

	def get_start_time(self):
		return self.start_time

	def get_end_day(self):
		return self.end_day

	def get_end_time(self):
		return self.end_time

	def get_pointer(self):
		return self.pointer

	def set_pointer(self, appointment):
		pointer = appointment

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

	def is_empty(self):
		return self.head == None

	def add_appointment(self, appointment):
		if self.is_empty():
			self.head = appointment
		else:
			week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]




def main():
	appointment1 = Appointment("walk dog", "monday", "14:00", "monday", "15:00")

	print(appointment1)

if __name__ == '__main__':
	main()