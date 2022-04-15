import typing
from enum import Enum

import wpilib

import globe
from loops import Loop
from state_machines import StateMachine


class ExampleAutoState(Enum):
    DRIVE_FORWARD = 0
    TURN_90_DEG = 1
    FINISHED = 2


class ExampleAuto(Loop, StateMachine):
    """
    Drive in a square.
    """

    _state: ExampleAutoState
    _square_itr: int
    _timer: wpilib.Timer

    def __init__(self):
        self._timer = wpilib.Timer()

    def _update_state(self):
        match self._state:

            case ExampleAutoState.DRIVE_FORWARD:

                if self._timer.get() > 1:
                    self._state = ExampleAutoState.TURN_90_DEG
                    self._timer.reset()

            case ExampleAutoState.TURN_90_DEG:

                if self._timer.get() > 0.5:  # Lazy timed turn
                    self._state = ExampleAutoState.DRIVE_FORWARD
                    self._timer.reset()
                    self._square_itr += 1

                    if self._square_itr == 4:
                        # The square is complete
                        self._state = ExampleAutoState.FINISHED
                        globe.drivetrain.stop()

    def _run_state(self):
        match self._state:

            case ExampleAutoState.DRIVE_FORWARD:

                globe.drivetrain.arcade_drive(0.6, 0)

            case ExampleAutoState.TURN_90_DEG:

                globe.drivetrain.arcade_drive(0, 0.3)

    def on_start(self, timestamp):
        self._state = ExampleAutoState.DRIVE_FORWARD
        self._square_itr = 0

        self._timer.reset()
        self._timer.start()

    def on_update(self, timestamp):
        self._update_state()
        self._run_state()

    def on_end(self, timestamp):
        pass

    @property
    def state(self) -> typing.Any:
        return self._state
