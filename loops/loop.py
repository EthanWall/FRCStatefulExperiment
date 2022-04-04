from abc import abstractmethod, ABC


class Loop(ABC):

    @abstractmethod
    def on_start(self, timestamp):
        ...

    @abstractmethod
    def on_update(self, timestamp):
        ...

    @abstractmethod
    def on_end(self, timestamp):
        ...
