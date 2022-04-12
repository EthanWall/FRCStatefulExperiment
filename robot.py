import wpilib

import globe
from control_boards.gamepad import XboxControlBoard
from loops.subsystem_loop import SubsystemLoop
from loops.teleop_loop import TeleOpLoop
from scheduling import Scheduler


class Robot(wpilib.TimedRobot):

    def __init__(self):
        super().__init__()

        self.scheduler = Scheduler()
        self.subsystem_manager = SubsystemLoop()
        self.teleop_loop = TeleOpLoop()

        globe.stick = XboxControlBoard()

    def robotInit(self) -> None:
        # Register our subsystem manager with the scheduler, so that subsystems will be periodically updated
        self.scheduler.register(self.subsystem_manager)

        # Start the robot loop
        self.scheduler.start()

    def autonomousInit(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def autonomousExit(self) -> None:
        pass

    def teleopInit(self) -> None:
        self.scheduler.register(self.teleop_loop)

    def teleopPeriodic(self) -> None:
        pass

    def teleopExit(self) -> None:
        self.scheduler.unregister(self.teleop_loop)

    def disabledInit(self) -> None:
        pass
