from abc import ABC, abstractmethod

class CommandPlugin(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def get_command_name(self) -> str:
        raise NotImplementedError("This method should be overridden by subclasses")