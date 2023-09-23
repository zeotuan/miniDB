from __future__ import annotations
from SQL import SQL


class SQLUse(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        if len(sql_vector) <= 1:
            raise SyntaxError
        self._db_name = sql_vector[1]
        print(f"Use DB: {self.db_name}")

    @property
    def db_name(self) -> str:
        return self._db_name
