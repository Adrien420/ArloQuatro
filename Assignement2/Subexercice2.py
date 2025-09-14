from time import sleep
import functions_for_arlo
import robot

# Création de l'objet robot
arlo = robot.Robot()

print("Reading loop")

try:
    for i in range(5):
        # Lecture des 4 sonars
        front  = arlo.read_front_ping_sensor()/10
        left   = arlo.read_left_ping_sensor()/10
        right  = arlo.read_right_ping_sensor()/10
        back   = arlo.read_back_ping_sensor()/10

        # Affichage clair dans le terminal
        print(f"----- sonar reading (Measure {i+1}-----")
        print(f"Front : {front} cm")
        print(f"Left  : {left} cm")
        print(f"Right  : {right} cm")
        print(f"Back : {back} cm")
        print("------------------------")

        # Attente de 3 secondes avant prochaine lecture
        sleep(3)

except KeyboardInterrupt:
    print("\nClosing program.")

