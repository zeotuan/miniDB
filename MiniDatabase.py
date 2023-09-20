from __future__ import annotations
import os
from exceptions import DatabaseAlreadyExistException, DatabaseDoesNotExistException
from CatalogManager import CatalogManager
from SQLStatement import *


class MiniDatabase:
    def __init__(self, catalog_manager: CatalogManager, path: str) -> None:
        self.path = path
        self.catalog_manager = catalog_manager

    def create_db(self, st: SQLCreateDB) -> None:
        if self.catalog_manager.get_db(st.db_name) is not None:
            raise DatabaseAlreadyExistException
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            db_path = os.path.join(self.path, st.db_name)
            os.mkdir(db_path)

        self.catalog_manager.create_db(st.db_name)
        self.catalog_manager.write_db_archive()

    def drop_db(self, st: SQLDropDB) -> None:
        db = self.catalog_manager.get_db(st.db_name)
        if db is None:
            raise DatabaseDoesNotExistException

        if os.path.exists(os.path.join(self.path, db.name)):
            os.remove(os.path.join(self.path, db.name))

        self.catalog_manager.delete_db(db.name)
        self.catalog_manager.write_db_archive()

    def create_table(self, st: SQLCreateTable) -> None:
        pass

    def drop_table(self, st: SQLDropTable) -> None:
        pass

    def create_index(self, st: SQLCreateIndex) -> None:
        pass

    def drop_index(self, st: SQLDropIndex) -> None:
        pass

    def use(self, st: SQLUse) -> None:
        pass

    def insert(self, st: SQLInsert) -> None:
        pass

    def select(self, st: SQLSelect) -> None:
        pass

    def delete(self, st: SQLDelete) -> None:
        pass

    def update(self, st: SQLUpdate) -> None:
        pass
