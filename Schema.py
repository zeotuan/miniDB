from __future__ import annotations
from abc import ABC, abstractmethod


class Schema(ABC):
    def __init__(
        self,
        schema_version: int,
        generation_counter: int,
        tables: dict,
        indexes: dict,
        fkeys: dict,
        **kwargs,
    ) -> None:
        pass
