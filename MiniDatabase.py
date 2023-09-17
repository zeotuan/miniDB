from __future__ import annotations
from abc import ABC, abstractmethod
from CatalogManager import CatalogManager
from SQLStatement import *


class MiniDatabase(ABC):
    @abstractmethod
    def __init__(self, catalog_manager: CatalogManager) -> None:
        self.catalog_manager = catalog_manager

    @abstractmethod
    def create_db(self, st: SQLCreateDB) -> None:
        pass

    @abstractmethod
    def drop_db(self, st: SQLDropDB) -> None:
        pass

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
    def use(self, st: SQLUse) -> None:
        pass

    @abstractmethod
    def insert(self, st: SQLInsert) -> None:
        pass

    @abstractmethod
    def select(self, st: SQLSelect) -> None:
        pass

    @abstractmethod
    def delete(self, st: SQLDelete) -> None:
        pass

    @abstractmethod
    def update(self, st: SQLUpdate) -> None:
        pass
