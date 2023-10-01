from dataclasses import dataclass


@dataclass
class SQLWhere:
    key: str
    sign_type: int
    value: str
