import geom_analysis as ga
import pytest

def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)
    assert observed == expected

def test_bond_check_True():
    distance = 0.5
    expected = True
    observed = ga.bond_check(distance)
    assert observed == expected

def test_bond_check_False():
    distance = 2.0
    expected = False
    observed = ga.bond_check(distance)
    assert observed == expected

def test_bond_check_0():
    distance = 0.0
    expected = False
    observed = ga.bond_check(distance)
    assert observed == expected

def test_bond_check_1_5():
    distance = 1.5
    expected = True
    observed = ga.bond_check(distance)
    assert observed == expected

def test_bond_check_negative():
    distance = -1
    expected = False
    with pytest.raises(ValueError):
        calculated = ga.bond_check(distance)
    assert expected == calculated

def test_value_error():
    fname = 'hello.txt'
    with pytest.raises(ValueError):
        ga.open_xyz(fname)