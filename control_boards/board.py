from abc import ABC, abstractmethod


class ControlBoardBase(ABC):

    @property
    @abstractmethod
    def forward(self) -> float:
        """
        The forward vector of the robot. Ranges from -1 to 1.
        """

    @property
    @abstractmethod
    def rotation(self) -> float:
        """
        The rotation vector of the robot. Ranges from -1 to 1.
        """
