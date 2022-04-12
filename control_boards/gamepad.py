import wpilib

from control_boards.board import ControlBoardBase


class XboxControlBoard(ControlBoardBase):

    def __init__(self):
        self.drive_stick = wpilib.XboxController(0)

    @property
    def forward(self) -> float:
        return -self.drive_stick.getLeftY()

    @property
    def rotation(self) -> float:
        return self.drive_stick.getRightX()
