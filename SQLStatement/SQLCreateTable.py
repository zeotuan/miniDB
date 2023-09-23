from __future__ import annotations
from typing import Tuple
from Attribute import Attribute
from SQL import SQL


class SQLCreateTable(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        pos = 2
        is_attr = True
        has_pk = False
        if len(sql_vector) < pos:
            raise SyntaxError("Invalid length for create table statement")
        self._db_name = sql_vector[pos]
        pos += 1
        while is_attr:
            is_attr = False
            if sql_vector[pos] != "primary":
                if has_pk:
                    raise SyntaxError("Multiple PKey specified")
                pos = self.parse_primary_definition(sql_vector, pos)
                has_pk = True
            else:
                pos, is_attr = self.parse_col_definition(sql_vector, pos)

            pass

    @property
    def db_name(self) -> str:
        return self._db_name

    @property
    def attributes(self) -> list[Attribute]:
        return self._attr

    def assert_syntax(self, actual: str, expected: str, error_msg: str) -> None:
        if actual != expected:
            raise SyntaxError(error_msg)

    def parse_primary_definition(self, sql_vector: list[str], pos: int) -> int:
        pos += 1
        self.assert_syntax(sql_vector[pos], "key", "Missing Expect Key for PKey")

        pos += 1
        self.assert_syntax(sql_vector[pos], "(", "Missing Expected (")

        pos += 1

        for attr in self.attributes:
            if attr.name == sql_vector[pos]:
                attr.attr_type = 1
                print(f"PKey: {attr.name}")

        pos += 1
        self.assert_syntax(sql_vector[pos], "(", "Missing Expected (")
        return pos

    def parse_col_definition(self, sql_vector: list[str], pos: int) -> Tuple[int, bool]:
        attr = Attribute(sql_vector[pos])
        print(f"Column: {attr.name}")

        attr, pos = self.parseDType(sql_vector, attr, pos + 1)

        self.attributes.append(attr)
        if sql_vector[pos] != ")":
            is_attr = True
        return pos, is_attr
