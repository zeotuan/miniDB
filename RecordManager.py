from __future__ import annotations
from CatalogManager import CatalogManager
from Buffer import BufferManager
from SQLStatement import SQLInsert, SQLDelete, SQLSelect, SQLUpdate, SQLWhere
from Table import Table
from Buffer import BlockInfo


class RecordManager:
    def __init__(
        self, db_name: str, catalog_manager: CatalogManager, buffer_manager: BufferError
    ) -> None:
        self.catalog_manager = catalog_manager
        self.buffer_manager = buffer_manager
        self.db_name = db_name

    def insert(self, st: SQLInsert) -> None:
        pass

    def update(self, st: SQLUpdate) -> None:
        pass

    def select(self, st: SQLSelect) -> None:
        pass

    def delete(self, st: SQLDelete) -> None:
        pass

    def get_block_info(self, tbl: Table, block_num: int) -> BlockInfo:
        pass

    # TODO: incomplete typing
    def get_record(self, tbl: Table, block_num: int, offset: int) -> list:
        pass

    def delete_record(self, tbl: Table, block_num: int, offset: int) -> None:
        pass

    def update_record(
        self, tbl: Table, block_num: int, offset: int, indices: list[int], values: list
    ) -> None:
        pass

    def satisfy_where(self, tbl: Table, keys: list, where: SQLWhere) -> bool:
        pass
