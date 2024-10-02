#Command List:
#M1: Home all axes (XYZ)

# MODULE IMPORTS
from xcontrol import move_x, get_stall_x
from ycontrol import move_y, get_stall_y
from zcontrol import move_z, get_stall_z, get_z_sensor
from threading import Thread

#VARIABLE DEFINITIONS
stall_z=['n/a', 0, 0, 0, 0]
corner1=[]
corner2=[]
corner3=[]
corner4=[]
cornerz=[]
xl=350
yl=350
zl=350
xp=0
yp=0
zp=0

#FUNCTION & THREAD DEFINITIONS
def write_log(log_message):
	try:
		with open('log.txt', 'a') as file:
			file.write(log_message + '\n')
	except FileNotFoundError:
		print("The file 'log.txt' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

def get_data():
	data_dict = {}
	try:
		with open('data.txt', 'r') as file:
			for line in file:
				if line.strip():  # Check if the line is not empty
					key, value = line.strip().split(':', 1)  # Split line by the first occurrence of ':'
					data_dict[key.strip()] = value.strip()  # Remove any leading/trailing whitespace
	except FileNotFoundError:
		print("The file 'data.txt' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")
	return data_dict

def detect_stall_z(motor):
	while get_stall_z(motor) != True:
		stall_z[motor]=0
	stall_z[motor]=1

z1_stall_thread=Thread(target=detect_stall_z(1), args=(1,))
z2_stall_thread=Thread(target=detect_stall_z(2), args=(2,))
z3_stall_thread=Thread(target=detect_stall_z(3), args=(3,))
z4_stall_thread=Thread(target=detect_stall_z(4), args=(4,))

def probe_z(speed):
	while get_z_sensor != True:
		move_z("rel", "all", -1, speed)

def M1():
	write_log('homing')
	while get_stall_x() != True:
		move_x("rel", -1, 20)
	while get_stall_y() != True:
		move_y("rel", -1, 20)
	while get_z_sensor() != True:
		move_z("rel", "all", -1, 20)
	move_z("abs", "all", 5, 20)

def QGL(precision, speed, travel):
	M1()
	writedata=['X_POSITION=0', 'Y_POSITION=0', 'Z_POSITION=0', 'E_RATE=0', 'LOADED=0']
	with open('data.txt', "w+") as data:
		for wdata in writedata:
			data.writelines(wdata + '\n')
	move_z("abs", "all", 5, 20)
	move_x("abs", xl, travel)
	i=0
	while i<precision:
		probe_z(speed)
		write_log('probe')
	corner1.append(zp)
	cornerz.append(sum(corner1)/len(corner1))
	cornerz.append(sum(corner2)/len(corner2))
	cornerz.append(sum(corner3)/len(corner3))
	cornerz.append(sum(corner4)/len(corner4))

QGL(1, 20, 50)
print("woo")
