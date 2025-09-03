from time import sleep
import robot
arlo = robot.Robot()

# figure-8 shape: alternate left and right curves
for _ in range(5):  # repeat twice for a full 8
    # Left curve
    leftSpeed = 35
    rightSpeed = 95
    print(arlo.go_diff(leftSpeed, rightSpeed, 1, 1))
    sleep(6.2)
    # Right curve
    leftSpeed = 95
    rightSpeed = 32.85
    print(arlo.go_diff(leftSpeed, rightSpeed, 1, 1))
    sleep(5.35)


print(arlo.stop())


