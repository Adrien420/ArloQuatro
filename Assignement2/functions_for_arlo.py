from time import sleep
import robot
import numpy as np
# Create a robot object and initialize
arlo = robot.Robot()


def turn_angle_(angle):
	leftSpeed = 31
	rightSpeed = 32
	if np.sign(angle) >= 0:
		print(arlo.go_diff(leftSpeed, rightSpeed, 1, 0))
	else:
		angle = abs(angle)
		print(arlo.go_diff(leftSpeed, rightSpeed, 0, 1))
	# Wait a bit while robot moves forward
	sleep(1.72*angle/90)
	
def advance_dist(dist):
	leftSpeed = 62
	rightSpeed = 64
	print(arlo.go_diff(leftSpeed, rightSpeed, 1, 1))
	# Wait a bit while robot moves forward
	sleep(2.564*dist/102)

def advance_dist(speed,duration):
	print(arlo.go_diff(speed, speed*(1+1/31), 1, 1))
	# Wait a bit while robot moves forward
	sleep(duration)
 
def advance_in_curve(speed, duration):
    # Right curve
    print(arlo.go_diff(speed*2, speed, 1, 1))
    sleep(duration)
 
def read_sonars():
	front  = arlo.read_front_ping_sensor()/10
	left   = arlo.read_left_ping_sensor()/10
	right  = arlo.read_right_ping_sensor()/10
	back   = arlo.read_back_ping_sensor()/10
 
	data = {"front":front, "left":left, "right":right, "back":back}
 
	return data

def print_sonars(data):
	print("----- sonar reading -----")
	print(f"Front : {data['front']} cm")
	print(f"Left  : {data['left']} cm")
	print(f"Right  : {data['right']} cm")
	print(f"Back : {data['back']} cm")
	print("------------------------")

