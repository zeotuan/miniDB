from __future__ import annotations
from abc import ABC, abstractmethod
from Column import Column
from Index import Index
from typing import Optional


class Table(ABC):
    def __init__(self, name: str, cols: list[Column], indexes: list[Index]) -> None:
        self.name = name
        self.cols = cols
        self.indexes = indexes

    @abstractmethod
    def get_column_by_name(self, column_name: str) -> list:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def cast_column(self, column_name: str, cast_type: type) -> None:
        pass

    @abstractmethod
    def insert(self, row: list, insert_stack: list = []) -> None:
        pass

    @abstractmethod
    def update(self, set_value: str, set_column: str, condition: str) -> None:
        pass

    @abstractmethod
    def delete(self, condition: str) -> list:
        pass

    @abstractmethod
    def select(
        self,
        return_cols: list[str],
        condition: str,
        distinct: bool = False,
        order_by: Optional[str] = None,
        asc: bool = True,
        limit: Optional[int] = None,
    ) -> Table:
        pass

    @abstractmethod
    def order_by(self, column_name: str) -> list:
        pass

    # TODO: create join type
    @abstractmethod
    def join(self, other_table: Table, condition: str, join_type: str) -> Table:
        pass

    @abstractmethod
    def show(self, limit: Optional[int] = None, lock: bool = False) -> None:
        pass

    @abstractmethod
    def sort(self, asc: bool = True) -> Table:
        pass
