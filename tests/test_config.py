
import pytest


class OutOfRange(Exception):
    def __init__(self, msg="Input value out of range") -> None:
        self.msg = msg
        super().__init__(self.msg)

def test_generic():
    a = 5
    with pytest.raises(OutOfRange): # expected exception
        if a not in range(10, 20):
            raise OutOfRange