import wpilib

import globe
from control_boards.gamepad import XboxControlBoard
from loops.auto.example_auto import ExampleAuto
from loops.teleop_loop import TeleOpLoop
from scheduling import Scheduler
from subsystems.drivetrain_subsystem import Drivetrain


class Robot(wpilib.TimedRobot):

    def __init__(self):
        super().__init__()

        globe.scheduler = Scheduler()
        self.teleop_loop = TeleOpLoop()
        self.auto_loop = ExampleAuto()

        globe.stick = XboxControlBoard()
        globe.drivetrain = Drivetrain()

    def robotInit(self) -> None:
        globe.scheduler.start()

    def robotPeriodic(self) -> None:
        globe.scheduler.run_periodic()

    def autonomousInit(self) -> None:
        globe.scheduler.register(self.auto_loop)

    def autonomousPeriodic(self) -> None:
        pass

    def autonomousExit(self) -> None:
        globe.scheduler.unregister(self.auto_loop)

    def teleopInit(self) -> None:
        globe.scheduler.register(self.teleop_loop)

    def teleopPeriodic(self) -> None:
        pass

    def teleopExit(self) -> None:
        globe.scheduler.unregister(self.teleop_loop)

    def disabledInit(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
