from __future__ import annotations
from SQL import SQL


class SQLDropDB(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        if len(sql_vector) <= 2:
            raise SyntaxError
        self._db_name = sql_vector[2]

    def parseDType(self, sql_vector: list[str], pos_idx: int) -> int:
        pass

    @property
    def db_name(self) -> str:
        return self._db_name
