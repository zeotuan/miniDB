from  __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Table(ABC):

    @abstractmethod
    def get_column_by_name(self, column_name: str):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def cast_column(self, column_name: str, cast_type: type):
        pass

    @abstractmethod
    def insert(self, row: list, insert_stack: list = []):
        pass
    
    @abstractmethod
    def update(self, set_value: str, set_column: str, condition: str):
        pass

    @abstractmethod
    def delete(self, condition: str):
        pass

    @abstractmethod
    def select(self, return_cols: list[str], condition: str, distinct: bool = False, order_by: Optional[str]  = None, asc: bool = True, limit: Optional[int] = None):
        pass

    @abstractmethod
    def order_by(self, column_name: str):
        pass

    #TODO: create join type
    @abstractmethod
    def join(self, other_table: Table, condition: str, join_type: str):
        pass
    
    @abstractmethod
    def show(self, limit: Optional[int] = None, lock: bool = False):
       pass 
    