from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union
from table import Table


class Database(ABC):
    @abstractmethod
    def __init__(self, name: str, load: bool = True, verbose: bool = True) -> None:
        self.tables: dict = {}
        self._name = name
        self.verbose: bool = verbose

    @abstractmethod
    def save_dbs(self) -> None:
        pass

    @abstractmethod
    def save_lock(self) -> None:
        pass

    @abstractmethod
    def load_db(self) -> None:
        pass

    @abstractmethod
    def create_table(
        self,
        name: str,
        col_names: list[str],
        col_types: list[type],
        p_key: Optional[str] = None,
        unique=None,
        load: Optional[list] = None,
    ) -> None:
        pass

    @abstractmethod
    def drop_table(self, name: str) -> None:
        pass

    @abstractmethod
    def load_table(
        self,
        name: str,
        path: str,
        col_names: list[str],
        col_types: list[type],
        p_key: Optional[str] = None,
        infer_schema: bool = False,
    ) -> None:
        pass

    @abstractmethod
    def save_table(self, name: str, path: str) -> None:
        pass

    @abstractmethod
    def is_table_locked(self, name: str) -> bool:
        pass

    @abstractmethod
    def lock_table(self, name: str) -> None:
        pass

    @abstractmethod
    def unlock_table(self, name: str) -> None:
        pass

    @abstractmethod
    def create_index(
        self, index_name: str, table_name: str, index_col: str | list[str]
    ) -> None:
        pass

    @abstractmethod
    def drop_index(self, index_name: str) -> None:
        pass

    @abstractmethod
    def has_index(self, index_name: str) -> bool:
        pass
