from __future__ import annotations
from SQL import SQL


class SQLInsert(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        pos = 1
        is_attr = True

        if sql_vector[pos].lower() != "into":
            raise SyntaxError

        pos += 1
        tb_name = sql_vector[pos]

        pos += 1
        if sql_vector[pos].lower != "values":
            raise SyntaxError
