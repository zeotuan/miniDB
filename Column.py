from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Column(ABC):
    # TODO: col_type enum
    def __init__(self, name: str, not_null: int, col_type: int, hash_name: str) -> None:
        self.name = name
        self.not_null = not_null
        self.col_type = col_type
        self.hash_name = hash_name
