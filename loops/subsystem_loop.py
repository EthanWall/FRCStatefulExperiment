import typing

from loops.loop import Loop
from subsystems.subsystem import SubsystemBase


class SubsystemLoop(Loop):

    def __init__(self):
        self.subsystems: typing.List[SubsystemBase] = []

    def register(self, subsystem: SubsystemBase | typing.Iterable[SubsystemBase]):
        if isinstance(subsystem, SubsystemBase):
            # A singular Subsystem has been passed into the function, so append it to the list
            self.subsystems.append(subsystem)
        else:
            # An array of Subsystems has been passed into the function, so add each item onto the list
            self.subsystems.extend(subsystem)

    def on_start(self, timestamp):
        pass

    def on_update(self, timestamp):
        for subsystem in self.subsystems:
            subsystem.read_inputs()
            subsystem.update(timestamp)
            subsystem.write_outputs()
            subsystem.update_on_dashboard()

    def on_end(self, timestamp):
        for subsystem in self.subsystems:
            subsystem.stop()
