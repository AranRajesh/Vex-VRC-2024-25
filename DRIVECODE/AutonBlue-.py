#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# Different drivetrain motors
rightFront = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
rightMiddle = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
rightBack = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
leftFront = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
leftMiddle = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
leftBack = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)
rightDrive = MotorGroup(rightFront, rightMiddle, rightBack)
leftDrive = MotorGroup(leftFront, leftMiddle, leftBack)


# Drivetrain Inertial
drivetrain_inertial = Inertial(Ports.PORT3)

#Intake Motors
intakeFront = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
intakeConveyor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
fullIntake= MotorGroup(intakeFront, intakeConveyor)

# Mogo Mech
mogo = DigitalOut(brain.three_wire_port.a)

# Defining drivetrain using two motor groups
bot = SmartDrive(leftDrive, rightDrive, drivetrain_inertial, 2.75, 15, 17.5, INCHES)

# Getting controller defined
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

# Defining mogo mech functions to control pistons
def mogoout():
    mogo.set(True)

def mogoin():
    mogo.set(False)


# Defining intake functions for intake toggle
def startIntake():
    fullIntake.set_velocity(100,PERCENT)
    fullIntake.spin(FORWARD)

def stopIntake():
    fullIntake.stop()

def reverseIntake():
    fullIntake.set_velocity(100,PERCENT)
    fullIntake.spin(REVERSE)

# Defining controller buttons and actions

controller_1.buttonR2.pressed(startIntake)
controller_1.buttonR1.pressed(reverseIntake)
controller_1.buttonL2.pressed(stopIntake)
controller_1.buttonA.pressed(mogoout)
controller_1.buttonB.pressed(mogoin)

# Fun Controller message
controller_1.rumble(".-.-.")
controller_1.screen.print("Ready to drive! Good luck")

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
            drivetrain_left_side_speed = controller_1.axis1.position() + controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis1.position() - controller_1.axis3.position()
            
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
                leftDrive.spin(REVERSE)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                rightDrive.set_velocity(drivetrain_right_side_speed, PERCENT)
                rightDrive.spin(REVERSE)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

drivetrain.set_heading(0, degrees)

#endregion VEXcode Generated Robot Configuration


def autonoumous_blue_-():
drivetrain.drive_for(REVERSE, 20.9, INCHES)
drivetrain.turn_for(RIGHT, 45, DEGREES)
drivetrain.drive_for(REVERSE, 17, INCHES)
mogoout()
drivetrain.turn_for(LEFT, 135, DEGREES)
intake()
drivetrain.drive_for(FORWARD, 25.4, INCHES)
drivtrain.turn_for(RIGHT, 90, INCHES)
drivtrain.drive_for(FORWARD, 44.7, INCHES)
intakestop()

# Library imports
from vex import *

# Begin project code
