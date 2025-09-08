from time import sleep
import robot
# Create a robot object and initialize
arlo = robot.Robot()


def turn_angle_(angle):
	leftSpeed = 31
	rightSpeed = 32
	print(arlo.go_diff(leftSpeed, rightSpeed, 1, 0))
	# Wait a bit while robot moves forward
	sleep(1.72*angle/90)
	
def advance_dist(dist):
	leftSpeed = 62
	rightSpeed = 64
	print(arlo.go_diff(leftSpeed, rightSpeed, 1, 1))
	# Wait a bit while robot moves forward
	sleep(2.564*dist/102)

def advance_dist(vitesse,duree):
	print(arlo.go_diff(vitesse, vitesse*(1+1/31), 1, 1))
	# Wait a bit while robot moves forward
	sleep(duree)

