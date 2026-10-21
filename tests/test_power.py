from calculator.core import power
def test_power():
    assert power(2, 3) == 9
def test_power_zero_exponent():
    assert power(5, 0) == 1
