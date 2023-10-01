from dataclasses import dataclass


@dataclass
class SQLValue:
    data_type: int
    value: str
