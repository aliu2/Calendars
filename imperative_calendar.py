#adding an appointment to a day
def add_appointment(appointment_name, start_day, start_time, end_day, end_time, week):
	if start_day == end_day:
		entry = [appointment_name, start_time, end_time]
		week[start_day.lower()].append(entry)
		# week[start_day.lower()][len(week[start_day.lower()])-1]
	else:
		start_day_entry = [appointment_name, start_time, -1]
		end_day_entry = [appointment_name, -1, end_time]
		week[start_day.lower()].append(start_day_entry)
		week[end_day.lower()].append(end_day_entry)


#printing the appointments for a specific day
def print_day(day, day_name):
	if len(day) == 0:
		return "You have no appointments scheduled for " + day_name.capitalize()
	s = day_name.capitalize() + ":\n"
	for curr_appointment in day:
		appointment_name = curr_appointment[0]
		#if the appointment starts or ends on a different day
		if -1 in curr_appointment:
			if curr_appointment[1] == -1:
				#if the appointment starts on a different day and ends on this day
				s += appointment_name + " starts on a different day and ends at " + curr_appointment[2] + "\n"
			else:
				#if the appointment starts on this day and ends on a different day
				s += appointment_name + " starts at " + curr_appointment[1] + " and ends on a different day\n"
		else:
			s += appointment_name + " starts at " + curr_appointment[1] + " and ends at " + curr_appointment[2] + "\n"
	return s


def remove_appointment(appointment_name, week):
	for day in week:
		for curr_appointment in day:
			if appointment_name in curr_appointment:
				day.remove(curr_appointment)
	print("Appointment removed")
	return week



def main():
	week = {
		"monday": [['walk dog', '13:00', '12:00']],
		"tuesday": [],
		"wednesday": [],
		"thursday": [],
		"friday": [],
		"saturday": [],
		"sunday": []
	}

	print("\033[H\033[J")
	command = input("What do you wish to do?\n")

	while command != "end":

		if command == "add":
			#takes user input and adds an appointment
			appointment_name = input("Please enter a name for the appointment\n")
			start_day = input("Please enter the start day of your appointment\n")
			start_time = input("Please enter the start time of your appointment (HH:MM)\n")
			end_day = input("Please enter the end day of your appointment\n")
			end_time = input("Please enter the end time of your appointment (HH:MM)\n")
			add_appointment(appointment_name, start_day, start_time, end_day, end_time, week)
			print("\033[H\033[J")
			print("Appointment added!")
			print(week)


		elif command == "remove":
			#read user input and remove the task
			appointment_name = input("What is the name of the appointment you would like to remove?\n")
			week = remove_appointment(appointment_name, week)

		elif command == "print day":
			#read day and print the day
			day = input("Which day's appointments would you like to see?\n")
			print(print_day(week[day.lower()], day))

		elif command == "print week":
			#print the week
			pass
		else:
			print("Please enter a valid command")

		command = input("What do you wish to do?\n")


if __name__ == '__main__':
	main()