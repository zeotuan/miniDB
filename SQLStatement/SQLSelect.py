from __future__ import annotations
from SQL import SQL


class SQLSelect(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        pass

    def parseDType(self, sql_vector: list[str], pos_idx: int) -> int:
        pass
