from __future__ import annotations
from abc import ABC, abstractmethod


class BaseOperator(ABC):
    def __init__(self, **kwargs) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass
