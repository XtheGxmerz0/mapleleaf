def write_log(log_message):
	try:
		with open('log.txt', 'a') as file:
			file.write(log_message + '\n')
	except FileNotFoundError:
		print("The file 'log.txt' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")
def get_stall_y():
	write_log('gsy')
	return True
def move_y(mode, distance, speed):
	if mode == "rel":
		pass
		write_log('relm')
	elif mode == "abs":
		pass
		write_log('absm')
