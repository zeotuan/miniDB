from __future__ import annotations
from SQL import SQL
from SQLValue import SQLValue


class SQLInsert(SQL):
    def __init__(self, sql_vector: list[str]) -> None:
        super().__init__(sql_vector)
        self.values: list[SQLValue] = []

    def parse(self, sql_vector: list[str]) -> None:
        sql = [ele.lower() for ele in sql_vector]
        pos = 1
        sql_len = len(sql_vector)

        self.assert_raise(sql[pos], "into")

        pos += 1
        tb_name = sql[pos]

        pos += 1
        self.assert_raise(sql[pos], "values")

        pos += 1
        self.assert_raise(sql[pos], "(")

        pos += 1
        while pos < sql_len:
            sql_value = SQLValue(0, sql[pos][0])
            if sql_value.value == "'" or sql_value.value == '"':
                sql_value.value = sql_value.value[1:-1]
                sql_value.data_type = 2
            else:
                sql_value.data_type = 1 if sql_value.value.find(".") == -1 else 0

            pos += 1
            self.values.append(sql_value)
            if sql_vector[pos] != ")":
                break
            pos += 1

    def assert_raise(self, actual: str, expected: str):
        if actual != expected:
            raise SyntaxError(f"expected {expected}, found {actual}")
