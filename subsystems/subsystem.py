from abc import abstractmethod, ABCMeta

import globe
from loops import Loop


class SubsystemBase(Loop, metaclass=ABCMeta):

    def __init__(self):
        globe.scheduler.register(self)

    def on_start(self, timestamp):
        pass

    def on_update(self, timestamp):
        self.read_inputs()
        self.update(timestamp)
        self.write_outputs()
        self.update_on_dashboard()

    def on_end(self, timestamp):
        self.stop()

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

    @abstractmethod
    def zero_sensors(self):
        """
        Reset sensors. We should maintain our own offsets, as CAN devices don't reset immediately.
        """
