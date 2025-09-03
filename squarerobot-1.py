from time import sleep
import robot
# Create a robot object and initialize
arlo = robot.Robot()
print("Running ...")
# send a go_diff command to drive forward


#LOOP

for j in range(0,4):
	for i in range(0,4):
		leftSpeed = 62
		rightSpeed = 64
		print(arlo.go_diff(leftSpeed, rightSpeed, 1, 1))
		# Wait a bit while robot moves forward
		sleep(2.564)
		# send a stop command
		leftSpeed = 31
		rightSpeed = 32
		print(arlo.go_diff(leftSpeed, rightSpeed, 1, 0))
		# Wait a bit while robot moves forward
		sleep(1.72)
print(arlo.stop())

'''
leftSpeed = 62
rightSpeed = 64
print(arlo.go_diff(leftSpeed, rightSpeed, 1, 1))
# Wait a bit while robot moves forward
sleep(8)
print(arlo.stop())

'''
