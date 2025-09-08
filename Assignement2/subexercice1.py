from time import sleep
import functions_for_arlo
import robot
'''
# Création de l'objet robot
arlo = robot.Robot()

front  = arlo.read_front_ping_sensor()
left   = arlo.read_left_ping_sensor()
right  = arlo.read_right_ping_sensor()
back   = arlo.read_back_ping_sensor()
mini = min(front,left,right)
while mini > 100:
	functions_for_arlo.advance_dist(1)
print("Obstacle détecté")
print("----- sonar reading -----")
print(f"Front : {front} cm")
print(f"Left  : {left} cm")
print(f"Right  : {right} cm")
print(f"Back : {back} cm")
print("------------------------")
functions_for_arlo.turn_angle_(90)
print(arlo.stop())
'''
# Création de l'objet robot
arlo = robot.Robot()

front  = arlo.read_front_ping_sensor()
left   = arlo.read_left_ping_sensor()
right  = arlo.read_right_ping_sensor()
back   = arlo.read_back_ping_sensor()
mini = min(front,left,right)
while mini > 200:
	front  = arlo.read_front_ping_sensor()
	left   = arlo.read_left_ping_sensor()
	right  = arlo.read_right_ping_sensor()
	back   = arlo.read_back_ping_sensor()
	mini = min(front,left,right)
	functions_for_arlo.advance_dist(31,0.05)
print("Obstacle détecté")
print("----- sonar reading -----")
print(f"Front : {front} cm")
print(f"Left  : {left} cm")
print(f"Right  : {right} cm")
print(f"Back : {back} cm")
print("------------------------")
functions_for_arlo.turn_angle_(90)
print(arlo.stop())
