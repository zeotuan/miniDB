from __future__ import annotations
from typing import Annotated
import os

BLOCK_SIZE = 4 * 1024


class BlockHandle:
    def __init__(self, path: str) -> None:
        self._first_block = BlockInfo(0)
        self._block_size = 300
        self._block_count = 0
        self.path = path


class FileHandle:
    def __init__(self, path: str):
        pass


class BlockInfo(object):
    def __init__(self, block_num: int) -> None:
        self.block_num = block_num
        self.data: Annotated[bytearray, BLOCK_SIZE] = bytearray([0] * BLOCK_SIZE)
        self.dirty = False
        self.age = 0
        self.next: BlockInfo | None = None
        self.file: FileInfo | None = None

    def inc_age(self) -> None:
        self.age += 1

    def reset_age(self) -> None:
        self.age = 0

    @property
    def prev_block_num(self) -> int:
        return int(self.data[:4])

    @prev_block_num.setter
    def prev_block_num(self, num: int) -> None:
        self.data[:4] = num.to_bytes(4, byteorder="big", signed=False)

    @property
    def next_block_num(self) -> int:
        return int(self.data[4:8])

    @next_block_num.setter
    def next_block_num(self, num: int) -> None:
        self.data[4:8] = num.to_bytes(4, byteorder="big", signed=False)

    @property
    def record_count(self) -> int:
        return int(self.data[8:12])

    @record_count.setter
    def record_count(self, count: int) -> None:
        self.data[8:12] = count.to_bytes(4, byteorder="big", signed=False)

    def decrease_record_count(self) -> None:
        self.record_count -= 1

    @property
    def block_content(self) -> bytearray:
        return self.data[12:]

    def read_info(self, path: str) -> None:
        assert self.file is not None
        path = os.path.join(path, self.file.file_path)
        with open(path, "rb") as file:
            file.seek(self.block_num * BLOCK_SIZE)
            file.readinto(self.data)

    def write_info(self, path: str) -> None:
        pass


class FileInfo:
    def __init__(
        self,
        db_name: str,
        file_name: str,
        file_type: int,
        path: str,
        record_num: int,
        record_len: int,
        first_block: BlockInfo,
        next: FileInfo,
    ) -> None:
        self.db_name = db_name
        self.file_type = file_type
        self.file_name = file_name

    @property
    def file_path(self) -> str:
        return os.path.join(self.db_name, self.file_name, self.extension)

    @property
    def extension(self) -> str:
        return ".index" if self.file_type == 1 else ".records"
