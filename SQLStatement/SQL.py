from __future__ import annotations
from abc import ABC, abstractmethod


class SQL(ABC):
    @abstractmethod
    def parse(self, sql_vector: list[str]) -> None:
        pass

    @abstractmethod
    def parseDType(self, sql_vector: list[str], pos_idx: int) -> int:
        pass
