from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Index(ABC):
    def __init__(
        self, name: str, table_name: str, skip_scan: bool = False, **kwargs
    ) -> None:
        self.name = name
        self.table_name = table_name
        self.skip_scan = skip_scan
