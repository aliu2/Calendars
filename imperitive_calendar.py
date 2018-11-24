#EDITS TO BE MADE: APPOINTMENTS SHOULD BE APPENDED AS AN ARRAY
#FIRST INDEX IN THIS ARRAY IS THE NAME OF THE APPOINTMENT FOLLOWED BY THE USUAL DETAILS

#adding an appointment to a day
def add_appointment(start_day, start_time, end_day, end_time, week):
	if start_day == end_day:
		week[start_day.lower()].append(start_time)
		week[start_day.lower()].append(end_time)
	else:
		week[start_day.lower()].append(start_time)
		week[start_day.lower()].append(-1)
		week[end_day.lower()].append(-1)
		week[end_day.lower()].append(end_time)
	print("appointment added")



#printing the appointments for a specific day
def print_day(day, day_name):
	if len(day) == 0:
		return "You have no appointments scheduled for " + day_name
	s = ""
	appointment_number = 1
	for i in range(0,len(day)-1,2):
		curr_appointment = [day[i], day[i+1]]
		if -1 in curr_appointment:
			if curr_appointment[0] == -1:
				#if the appointment starts on a different day and ends on this day
				s += "Appointment " + str(appointment_number) + " for " + day_name + " starts on a different day and ends at " + curr_appointment[1] + "\n"
			else:
				#if the appointment starts on this day and ends on a different day
				s += "Appointment " + str(appointment_number) + " for " + day_name + " starts at " + curr_appointment[0] + " and ends on a different day\n"
		else:
			s += "Appointment " + str(appointment_number) + " for " + day_name + " starts at " + curr_appointment[0] + " and ends at " + curr_appointment[1] + "\n"

		appointment_number += 1
	return s






def main():
	week = {
		"monday": [],
		"tuesday": [],
		"wednesday": [],
		"thursday": [],
		"friday": [],
		"saturday": [],
		"sunday": []
	}

	command = input("What do you wish to do?\n")

	while command != "end":

		if command == "add":
			#takes user input and adds an appointment
			start_day = input("Please enter the start day of your appointment\n")
			start_time = input("Please enter the start time of your appointment (HH:MM)\n")
			end_day = input("Please enter the end day of your appointment\n")
			end_time = input("Please enter the end time of your appointment (HH:MM)\n")
			add_appointment(start_day, start_time, end_day, end_time, week)
			print(week)


		elif command == "remove":
			#read user input and remove the task
			pass
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

#print("\033[H\033[J") PRINT STATEMENT TO CLEAR THE CONSOLE