from __future__ import annotations
from SQL import SQL


class SQLCreateDB(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        if len(sql_vector) <= 2:
            raise SyntaxError
        self._db_name = sql_vector[2]

    @property
    def db_name(self) -> str:
        return self._db_name
