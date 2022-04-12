import typing
from abc import ABC, abstractmethod


class StateMachine(ABC):

    @property
    @abstractmethod
    def state(self) -> typing.Any:
        ...
