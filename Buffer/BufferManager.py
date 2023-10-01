from __future__ import annotations
from Buffer import FileHandle, BlockHandle, BlockInfo, FileInfo


class BufferManager:
    def __init__(self, path: str) -> None:
        self._block_handle = BlockHandle(path)
        self._file_handle = FileHandle(path)
        self.path = path

    def get_file_block(
        self, db_name: str, tb_name: str, file_type: int, block_num: int
    ) -> BlockInfo:
        self._file_handle.inc_age()
        file = self._file_handle.get_file_info(db_name, tb_name, file_type)
        if file:
            block = self._file_handle.get_block_info(file, block_pos=block_num)
            if block:
                return block
            block = self._get_usable_block()
            assert block is not None
            block.block_num = block_num
            block.file = file
            block.read_info(self.path)
            self._file_handle.add_block_info(block)
            return block

        block = self._get_usable_block()
        assert block is not None
        block.block_num = block_num
        file = FileInfo(
            db_name,
            file_type=file_type,
            file_name=tb_name,
            record_num=0,
            record_len=0,
            next_file=None,
            first_block=None,
        )
        self._file_handle.add_file_info(file)
        block.file = file
        block.read_info(self.path)
        self._file_handle.add_block_info(block)
        return block

    def _get_usable_block(self) -> BlockInfo | None:
        if self._block_handle.block_count > 0:
            return self._block_handle.usable_block
        return self._file_handle.recycle_block()

    def write_block(self, block: BlockInfo) -> None:
        block.dirty = True

    def write_to_disk(self) -> None:
        self._file_handle.write_to_disk()
