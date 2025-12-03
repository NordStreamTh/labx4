from square import area, perimeter

# simple tests for isrpo

def test_area():
    assert area(0) == 0
    assert area(2) == 4
    assert area(-3) == 9
    assert area(5.5) == 30.25

def test_perimeter():
    assert perimeter(0) == 0
    assert perimeter(2) == 8
    assert perimeter(-3) == -12
    assert perimeter(5.5) == 22
