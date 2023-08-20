from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from table import Table


class DataBase(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.tables: dict = {}
        self.__dir__

    @abstractmethod
    def save_dbs(self):
        pass

    @abstractmethod
    def save_lock(self):
        pass

    @abstractmethod
    def load_db(self):
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
    ):
        pass

    @abstractmethod
    def drop_table(self, name: str):
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
    ):
        pass

    @abstractmethod
    def save_table(self, name: str, path: str):
        pass

    @abstractmethod
    def is_table_locked(self, name: str):
        pass

    @abstractmethod
    def lock_table(self, name: str):
        pass

    @abstractmethod
    def unlock_table(self, name: str):
        pass
