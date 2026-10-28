import pytest
from calculator.core import modulo
def test_modulo():
    assert modulo(10, 3) == 1
def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(1, 0)
