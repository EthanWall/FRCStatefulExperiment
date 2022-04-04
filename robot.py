import wpilib

from loops.loop import Loop
from loops.subsystem_loop import SubsystemLoop
from scheduling import Scheduler


class Robot(wpilib.TimedRobot):

    def __init__(self):
        super().__init__()

        self.scheduler = Scheduler()
        self.subsystem_manager = SubsystemLoop()

    def robotInit(self) -> None:
        # Register our subsystem manager with the scheduler, so that subsystems will be periodically updated
        self.scheduler.register(self.subsystem_manager)

    def autonomousInit(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def autonomousExit(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        pass

    def teleopExit(self) -> None:
        pass

    def disabledInit(self) -> None:
        pass
