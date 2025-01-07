#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
intake_motor_a = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
intake_motor_b = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
intake = MotorGroup(intake_motor_a, intake_motor_b)
rightFront = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
rightMiddle = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
rightBack = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
leftFront = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
leftMiddle = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
leftBack = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
rightDrive = MotorGroup(rightFront, rightMiddle, rightBack)
leftDrive = MotorGroup(leftFront, leftMiddle, leftBack)
intake = MotorGroup
bot = DriveTrain(leftDrive, rightDrive, 2.75, 15, 17.5, INCHES)
controller_1 = Controller(PRIMARY)

# wait for rotation sensor to fully initialize
wait(30, MSEC)
# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)

# clear the console to make sure we don't have the REPL in the console
print("\033[2J")


# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3 + axis1
            # right = axis3 - axis1
            drivetrain_left_side_speed = controller_1.axis3.position() + controller_1.axis1.position()
            drivetrain_right_side_speed = controller_1.axis3.position() - controller_1.axis1.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    leftDrive.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    rightDrive.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                leftDrive.set_velocity(drivetrain_left_side_speed, PERCENT)
                leftDrive.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                rightDrive.set_velocity(drivetrain_right_side_speed, PERCENT)
                rightDrive.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *
def intake():
    intake.spin(FORWARD)
def intakestop():
    intake.stop()
def intakereverse():
    intake.spin(REVERSE)
controller_1.buttonL1.pressed(intakereverse)
controller_1.buttonR1.pressed(intake)
controller_1.buttonR2.pressed(intakestop)

