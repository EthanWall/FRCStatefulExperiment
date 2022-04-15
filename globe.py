from control_boards.board import ControlBoardBase
from scheduling import Scheduler
from subsystems.drivetrain_subsystem import Drivetrain

scheduler: Scheduler
drivetrain: Drivetrain
stick: ControlBoardBase
