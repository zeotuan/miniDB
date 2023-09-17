from __future__ import annotations
from abc import ABC, abstractmethod
from SQLStatement import SQLCreateTable, SQLDropTable, SQLCreateIndex, SQLDropIndex
from Table import Table


class Database(ABC):
    @abstractmethod
    def __init__(self, name: str, load: bool = True, verbose: bool = True) -> None:
        self.tables = {}
        self.name = name
        self.verbose = verbose

    @abstractmethod
    def create_table(self, st: SQLCreateTable) -> None:
        pass

    @abstractmethod
    def drop_table(self, st: SQLDropTable) -> None:
        pass

    @abstractmethod
    def create_index(self, st: SQLCreateIndex) -> None:
        pass

    @abstractmethod
    def drop_index(self, st: SQLDropIndex) -> None:
        pass

    @abstractmethod
    def get_table(self, name: str) -> Table:
        pass

    @abstractmethod
    def is_idx_exist(self, name: str) -> bool:
        pass
