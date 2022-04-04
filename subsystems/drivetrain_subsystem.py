import ctre
import wpilib
import wpilib.drive
from wpimath.geometry import Rotation2d

from constants import PortConstants, DrivetrainConstants
from state_machines.drive_state_machine import DrivetrainStateMachine, DrivetrainState
from subsystems.subsystem import SubsystemBase


class PeriodicIO:
    # Outputs
    left_demand: float = 0
    right_demand: float = 0

    # Inputs
    left_position: float = 0
    right_position: float = 0
    heading: float = 0


class Drivetrain(SubsystemBase):

    def __init__(self):
        self._io = PeriodicIO()

        self._state_machine = DrivetrainStateMachine()

        # Motors
        left_motors = wpilib.MotorControllerGroup(
            wpilib.Spark(PortConstants.FRONT_LEFT_MOTOR_PORT),
            wpilib.Spark(PortConstants.REAR_LEFT_MOTOR_PORT)
        )
        left_motors.setInverted(DrivetrainConstants.LEFT_SIDE_INVERTED)

        right_motors = wpilib.MotorControllerGroup(
            wpilib.Spark(PortConstants.FRONT_RIGHT_MOTOR_PORT),
            wpilib.Spark(PortConstants.REAR_RIGHT_MOTOR_PORT)
        )
        right_motors.setInverted(DrivetrainConstants.RIGHT_SIDE_INVERTED)

        # Drivetrain
        self._drive = wpilib.drive.DifferentialDrive(left_motors, right_motors)

        # Encoders
        self._left_encoder = ctre.CANCoder(PortConstants.LEFT_DRIVE_ENCODER_PORT)
        self._right_encoder = ctre.CANCoder(PortConstants.RIGHT_DRIVE_ENCODER_PORT)

        # Gyros
        self._imu = ctre.PigeonIMU(PortConstants.IMU_PORT)

        # Sensor offsets
        self._left_position_offset = 0
        self._right_position_offset = 0
        self._heading_offset = 0

    def update(self, timestamp):
        pass

    def stop(self):
        self._io.left_demand = 0
        self._io.right_demand = 0

    def read_inputs(self):
        self._io.left_position = self._left_encoder.getPosition()
        self._io.right_position = self._right_encoder.getPosition()
        self._io.heading = self._imu.getFusedHeading()

    def write_outputs(self):
        # Drive the robot
        left_demand = self._io.left_demand
        right_demand = self._io.right_demand

        self._drive.tankDrive(left_demand, right_demand, False)

    def update_on_dashboard(self):
        pass

    def zero_sensors(self):
        self._left_position_offset = self.left_distance
        self._right_position_offset = self.right_distance
        self._heading_offset = self.heading.degrees()

    # Getters

    @property
    def left_distance(self) -> float:
        return self._io.left_position - self._left_position_offset

    @property
    def right_distance(self) -> float:
        return self._io.right_position - self._right_position_offset

    @property
    def average_distance(self) -> float:
        return (self.left_distance + self.right_distance) / 2

    @property
    def heading(self) -> Rotation2d:
        return Rotation2d.fromDegrees(self._io.heading - self._heading_offset)

    # Setters

    def arcade_drive(self, forward: float, rotation: float):
        """
        Drive the robot with forward and rotation controls.

        :param forward: Movement in the heading direction.
        :param rotation: Movement around the robot's center.
        """

        # Set our state to open loop driving
        self._state_machine.want_state(DrivetrainState.OPEN_LOOP)

        # Calculate the wheel speeds for arcade drive
        speeds = self._drive.arcadeDriveIK(forward, rotation, False)

        # Set the left and right motor powers
        self._io.left_demand = speeds.left
        self._io.right_demand = speeds.right
