import wpilib

from util import deadband
from control_boards import ControlBoardBase


class XboxControlBoard(ControlBoardBase):

    def __init__(self):
        self.drive_stick = wpilib.XboxController(0)

    @property
    def forward(self) -> float:
        val = -self.drive_stick.getLeftY()
        val = deadband(val, 0.05)
        return val

    @property
    def rotation(self) -> float:
        val = self.drive_stick.getRightX()
        val = deadband(val, 0.05)
        return val
