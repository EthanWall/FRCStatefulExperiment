import typing

import wpilib
from plum import dispatch

from loops.loop import Loop


class Scheduler:

    def _periodic(self):
        now = wpilib.Timer.getFPGATimestamp()

        for loop in self.loops:
            loop.on_update(now)

    def __init__(self):
        self.loops: typing.List[Loop] = []
        self.running = False
        self.notifier = wpilib.Notifier(self._periodic)

    @dispatch
    def register(self, loop: Loop):
        self.loops.append(loop)

        if self.running:
            now = wpilib.Timer.getFPGATimestamp()
            loop.on_start(now)

    @dispatch
    def register(self, loops: typing.Iterable[Loop]):
        for loop in loops:
            self.register(loop)

    def unregister(self, loop: Loop):
        self.loops.remove(loop)

        if self.running:
            now = wpilib.Timer.getFPGATimestamp()
            loop.on_end(now)

    def start(self):
        if self.running:
            return

        now = wpilib.Timer.getFPGATimestamp()
        for loop in self.loops:
            loop.on_start(now)

        self.notifier.startPeriodic(0.02)
        self.running = True

    def stop(self):
        if self.running:
            return

        now = wpilib.Timer.getFPGATimestamp()
        for loop in self.loops:
            loop.on_end(now)

        self.notifier.stop()
        self.running = True
