from main import Sum, Sub, Mul, Div

def test_sum():
    assert Sum(1, 2) == 3
    assert Sum(2, 2) == 4
    assert Sum(3, 3) == 6

def test_sub():
    assert Sub(1, 2) == -1
    assert Sub(2, 2) == 0
    assert Sub(3, 3) == 0

def test_mul():
    assert Mul(1, 2) == 2
    assert Mul(2, 2) == 4
    assert Mul(3, 3) == 9

def test_div():
    assert Div(1, 2) == 0.5
    assert Div(2, 2) == 1
