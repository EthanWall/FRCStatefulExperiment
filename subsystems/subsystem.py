from abc import ABC, abstractmethod


class SubsystemBase(ABC):

    @abstractmethod
    def update(self, timestamp):
        """
        Runs periodically. Update outputs and State Machine here.

        :param timestamp: The current time as an FPGA timestamp.
        """

    @abstractmethod
    def stop(self):
        """
        Stop all outputs.

        """

    @abstractmethod
    def read_inputs(self):
        """
        Read sensor values periodically.

        """

    @abstractmethod
    def write_outputs(self):
        """
        Write to the HAL/CAN bus periodically.

        """

    @abstractmethod
    def update_on_dashboard(self):
        """
        Write to the Smart Dashboard.

        """
