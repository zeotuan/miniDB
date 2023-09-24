from __future__ import annotations
from SQL import SQL


class SQLDropTable(SQL):
    def parse(self, sql_vector: list[str]) -> None:
        if len(sql_vector) <= 2:
            raise SyntaxError
        self._tb_name = sql_vector[2]
        print(f"DROP TABLE: {self.tb_name}")

    @property
    def tb_name(self) -> str:
        return self._tb_name
