from dataclasses import dataclass
from DataType import DataType


@dataclass
class Attribute:
    name: str = ""
    data_type: DataType = DataType.VARCHAR
    length: int = (0,)
    attr_type: int | None = (None,)
