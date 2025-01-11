import pytest
from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


@pytest.mark.parametrize("input_value, expected", [
    (0, 0),
    (180, -180.0),
    (-180, -180.0),
    (190, -170.0),
    (-190, 170.0),
    (360, 0.0),
    (-360, 0.0),
    (540, -180.0),
    (-540, -180.0),
    (730, 10.0),
])
def test_bound_to_180(input_value, expected):
    assert bound_to_180(input_value) == expected

# def test_bound_basic1():
#     assert bound_to_180(0) == 0


""" Tests for is_angle_between() """


@pytest.mark.parametrize("first_angle, middle_angle, second_angle, expected", [
    (0, 1, 2, True),
    (0, 0, 0, True),
    (0, 5, 10, True),
    (0, 10, 10, True),
    (-10, -5, -1, True),
    (5, 2, 10, False),
    (-10, -3, -5, False),
    (0, 45, 90, True),
    (45, 90, 270, False),
    (460, 500, 702, False),
    (460, 461, 462, True),
    (0, 360, 10, False),
])
def test_is_angle_between(first_angle, middle_angle, second_angle, expected):
    assert is_angle_between(first_angle, middle_angle, second_angle) == expected


# def test_between_basic1():
#     assert is_angle_between(0, 1, 2)
