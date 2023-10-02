from __future__ import annotations


class TableKey:
    def __init__(self, key_type: int, length: int) -> None:
        self.key_type = key_type
        self.length = length if key_type == 2 else 4
        self.key = bytearray([0] * self.length)

    @classmethod
    def from_table_key(cls, tbl_key: TableKey) -> TableKey:
        new_table_key = cls(tbl_key.key_type, tbl_key.length)
        new_table_key.key = tbl_key.key.copy()
        return new_table_key

    # def read_value(self, content: str) -> None:
