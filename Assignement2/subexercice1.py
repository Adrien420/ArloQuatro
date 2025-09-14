from time import sleep
import functions_for_arlo
import robot
import numpy as np

def main():
	# Création de l'objet robot
	arlo = robot.Robot()

	#path = np.array([[100,0],[100,100], [0,100], [0,0]])
 
	avoiding_obj = False
 
	current_orientation = 0

	data = functions_for_arlo.read_sonars()
	print(data)
	mini = min(data["front"],data["left"],data["right"])
	while True:
		while mini > 30:
			if avoiding_obj:
				functions_for_arlo.advance_in_curve(32.85, 0.05)
				current_orientation += 5.5
				print(current_orientation)
				if current_orientation > 90:
					functions_for_arlo.turn_angle_(-90)
					current_orientation -= 90
					avoiding_obj = False
			else:
				functions_for_arlo.advance_dist(31,0.05)
			data = functions_for_arlo.read_sonars()
			mini = min(data["front"],data["left"],data["right"])
		print("Object detected : turning left")
		avoiding_obj = True
		while data["right"] > 40:
			functions_for_arlo.turn_angle_(-1)
			current_orientation -= 3
			data = functions_for_arlo.read_sonars()
		print(arlo.stop())
		functions_for_arlo.turn_angle_(-20)
		current_orientation -= 20
		print(current_orientation)
		data = functions_for_arlo.read_sonars()
		mini = min(data["front"],data["left"],data["right"])
		functions_for_arlo.print_sonars(data)
	print(arlo.stop())

	return

if __name__ == '__main__':
    main()
