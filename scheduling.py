import typing

import wpilib
from plum import dispatch

from loops.loop import Loop


class Scheduler:

    def __init__(self):
        self.loops: typing.List[Loop] = []
        self.running = False

    @dispatch
    def register(self, loop: Loop):
        print(f"Registering {str(loop)}")
        self.loops.append(loop)

        if not self.running:
            return

        now = wpilib.Timer.getFPGATimestamp()
        loop.on_start(now)

    @dispatch
    def register(self, loops: typing.Iterable[Loop]):
        for loop in loops:
            self.register(loop)

    def unregister(self, loop: Loop):
        self.loops.remove(loop)

        if not self.running:
            return

        now = wpilib.Timer.getFPGATimestamp()
        loop.on_end(now)

    def run_periodic(self):
        now = wpilib.Timer.getFPGATimestamp()

        if not self.running:
            return

        for loop in self.loops:
            loop.on_update(now)

    def start(self):
        if self.running:
            return

        now = wpilib.Timer.getFPGATimestamp()
        for loop in self.loops:
            loop.on_start(now)

        self.running = True

    def stop(self):
        if self.running:
            return

        now = wpilib.Timer.getFPGATimestamp()
        for loop in self.loops:
            loop.on_end(now)

        self.running = True
