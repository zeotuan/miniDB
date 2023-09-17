from __future__ import annotations
from abc import ABC, abstractmethod
from Database import Database


class CatalogManager(ABC):
    @abstractmethod
    def __init__(self, archive_path: str) -> None:
        self.db_path = archive_path

    @abstractmethod
    def write_db_archive(self) -> None:
        pass

    @abstractmethod
    def read_db_archive(self) -> None:
        pass

    @abstractmethod
    def create_db(self, name: str) -> None:
        pass

    @abstractmethod
    def delete_db(self, name: str) -> None:
        pass

    def get_db(self, name: str) -> Database:
        pass
