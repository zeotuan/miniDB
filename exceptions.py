class DatabaseAlreadyExistException(Exception):
    pass


class DatabaseDoesNotExistException(Exception):
    pass


class NoCurrentDatabaseException(Exception):
    pass


class TableAlreadyExistException(Exception):
    pass


class TableDoesNotExistException(Exception):
    pass
