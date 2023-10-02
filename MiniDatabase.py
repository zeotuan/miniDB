from __future__ import annotations
import os
from exceptions import (
    DatabaseAlreadyExistException,
    DatabaseDoesNotExistException,
    NoCurrentDatabaseException,
    TableAlreadyExistException,
    TableDoesNotExistException,
)
from CatalogManager import CatalogManager
from Buffer import BufferManager
from SQLStatement import *
from RecordManager import RecordManager


class MiniDatabase:
    def __init__(self, catalog_manager: CatalogManager, path: str) -> None:
        self.path = path
        self.catalog_manager = catalog_manager
        self.current_db: str | None = None
        self._buffer_manager: BufferManager | None = None

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
        print(f"Create Table {st.tb_name}")
        if not self.current_db:
            raise NoCurrentDatabaseException

        db = self.catalog_manager.get_db(self.current_db)
        if not db:
            raise DatabaseDoesNotExistException

        if db.get_table(st.tb_name) is not None:
            raise TableAlreadyExistException

        table_path = os.path.join(self.path, self.current_db, st.tb_name + ".records")

        if os.path.exists(table_path):
            print(f"found existing table file at {table_path}. deleting...")
            os.remove(table_path)

        print("creating new table path")
        os.mkdir(table_path)

        print("creating table")
        db.create_table(st)

        print("writing to archive")
        self.catalog_manager.write_db_archive()

    def drop_table(self, st: SQLDropTable) -> None:
        if not self.current_db:
            raise NoCurrentDatabaseException

        db = self.catalog_manager.get_db(self.current_db)
        if not db:
            raise DatabaseDoesNotExistException

        table = db.get_table(st.tb_name)
        if not table:
            raise TableDoesNotExistException

        table_file_path = os.path.join(
            self.path, self.current_db, st.tb_name + ".records"
        )
        if not os.path.exists(table_file_path):
            print(f"Table file does not exist {table_file_path}")
        else:
            os.remove(table_file_path)
            print(f"table file removed at {table_file_path}")

        for index in table.indexes:
            index_path = os.path.join(self.path, self.current_db, index.name + ".index")
            if not os.path.exists(index_path):
                print(f"Index path for {index.name}: {index_path} does not exist")
            else:
                os.remove(index_path)

        db.drop_table(st)

        self.catalog_manager.write_db_archive()

    def create_index(self, st: SQLCreateIndex) -> None:
        pass

    def drop_index(self, st: SQLDropIndex) -> None:
        pass

    def use(self, st: SQLUse) -> None:
        if self.catalog_manager.get_db(st.db_name) is None:
            raise DatabaseDoesNotExistException(f"cannot find database {st.db_name}")

        if self.current_db is not None:
            self.catalog_manager.write_db_archive()
            self._buffer_manager = None
        self.current_db = st.db_name
        self._buffer_manager = BufferManager(self.path)

    def insert(self, st: SQLInsert) -> None:
        if not self.current_db:
            raise NoCurrentDatabaseException

        db = self.catalog_manager.get_db(self.current_db)
        if db is None:
            raise DatabaseDoesNotExistException

        assert self._buffer_manager is not None
        rm = RecordManager(self.current_db, self.catalog_manager, self._buffer_manager)
        rm.insert(st)

    def select(self, st: SQLSelect) -> None:
        pass

    def delete(self, st: SQLDelete) -> None:
        pass

    def update(self, st: SQLUpdate) -> None:
        pass
