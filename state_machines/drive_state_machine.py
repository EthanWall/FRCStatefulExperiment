from enum import Enum


class DrivetrainState(Enum):
    OPEN_LOOP = 0,
    PATH_FOLLOWING = 1


class DrivetrainStateMachine:

    def __init__(self):
        self._state = DrivetrainState.OPEN_LOOP

    def want_state(self, desired_state: DrivetrainState):

        match self._state:

            case DrivetrainState.OPEN_LOOP:

                if desired_state is DrivetrainState.PATH_FOLLOWING:
                    self._state = DrivetrainState.PATH_FOLLOWING

            case DrivetrainState.PATH_FOLLOWING:

                if desired_state is DrivetrainState.OPEN_LOOP:
                    self._state = DrivetrainState.OPEN_LOOP

    @property
    def state(self):
        return self._state
