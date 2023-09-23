from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Tuple
from Attribute import Attribute
from DataType import DataType


class SQL(ABC):
    def __init__(self, sql_vector: list[str]) -> None:
        self.parse(sql_vector)

    @abstractmethod
    def parse(self, sql_vector: list[str]) -> None:
        pass

    def parseDType(
        self, sql_vector: list[str], attr: Attribute, pos: int
    ) -> Tuple[Attribute, int]:
        sql = [item.lower() for item in sql_vector]

        if sql[pos] == "int":
            attr.data_type = DataType.INT
            attr.length = 4
            pos += 2 if sql[pos + 1] == "," else 1

        elif sql[pos] == "float":
            attr.data_type = DataType.FLOAT
            attr.length = 4
            pos += 2 if sql[pos + 1] == "," else 1

        elif sql[pos] == "varchar":
            attr.data_type = DataType.VARCHAR
            pos = self.assert_pos(sql, pos + 1, "(")
            attr.length = int(sql[pos])
            pos = self.assert_pos(sql, pos + 1, ")")
            pos = self.assert_pos(sql, pos, ",")
        else:
            raise SyntaxError("Invalid Type")

        return attr, pos

    def assert_pos(self, sql: list[str], pos: int, expected: str) -> int:
        if sql[pos] != expected:
            raise SyntaxError(f"expected {expected}, found {sql[pos]}")
        return pos + 1
