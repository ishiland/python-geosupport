from typing import Dict, Any


class GeosupportError(Exception):
    def __init__(self, message: str, result: Dict[str, Any] = {}) -> None:
        super(GeosupportError, self).__init__(message)
        self.result = result if result is not None else {}
