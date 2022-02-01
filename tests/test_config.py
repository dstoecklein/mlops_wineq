
import pytest





def test_generic():
    a = 5
    with pytest.raises(OutOfRange):  # expected exception
        if a not in range(10, 20):
            raise OutOfRange
