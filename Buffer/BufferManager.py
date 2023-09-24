from __future__ import annotations
from Buffer import FileHandle, BlockHandle, BlockInfo


class BufferManager:
    def __init__(self, path: str) -> None:
        self._block_handle = BlockHandle(path)
        self._file_handle = FileHandle(path)
        self.path = path

    def GetFileBlock(
        self, db_name: str, tb_name: str, file_type: int, block_num: int
    ) -> BlockInfo:
        pass

    def WriteBlock(self, block: BlockInfo) -> None:
        pass

    def WriteToDisk(self) -> None:
        pass
