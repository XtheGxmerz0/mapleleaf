# MODULE IMPORTS
from xcontrol import move_x, get_stall_x
from ycontrol import move_y, get_stall_y
from zcontrol import move_z, get_stall_z
from threading import *

#VARIABLE DEFINITIONS
stall_z=[0, 0, 0, 0]

#THREAD DEFINITIONS
z1_stall_thread=Thread(target=detect_stall_z(), args=(1,))
z2_stall_thread=Thread(target=detect_stall_z(), args=(2,))
z3_stall_thread=Thread(target=detect_stall_z(), args=(3,))
z4_stall_thread=Thread(target=detect_stall_z(), args=(4,))

#FUNCTION DEFINITIONS
def detect_stall_z(motor):
	while get_stall_z != True:
		stall_z[motor]=0
	stall_z[motor]=1

def M1():
	while get_stall_x() != True:
		move_x("rel", -1, 20)
	while get_stall_y() != True:
		move_y("rel", -1, 20)
	z1_stall_thread.run()
	z2_stall_thread.run()
	z3_stall_thread.run()
	z4_stall_thread.run()
	while stall_z[1] != 1 and stall_z[2] != 1 and stall_z[3] != 1 and stall_z[4] != 1:
		move_z("rel", "all", -1, 20)

def QGL(precision, speed, travel):
	M1()
