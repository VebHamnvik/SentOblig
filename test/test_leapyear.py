from leapyear.function import is_LeapYear

#General test for leap year
def test_is_year_a_leapyear():
    leap_year = is_LeapYear(2000)
    assert leap_year == True

#Test for checking a year that is divisible by 4 and not divisible by 100
def test_year_that_is_divisible_by_4_and_not_100():
    leap_year = is_LeapYear(40)
    assert leap_year == True

#Test for checking a year that is divisible by 400
def test_year_that_is_divisible_by_400():
    leap_year = is_LeapYear(1600)
    assert leap_year == True

#General test for not leap year
def test_is_not_leap_year():
    leap_year = is_LeapYear(1700)
    assert leap_year == False

#Test for checking a year that is divisible by 100, but not 400
def test_year_divisible_with_100_but_not_400():
    leap_year = is_LeapYear(1900)
    assert leap_year == False

#Test for checking a year that is not divisible by 4
def test_year_not_divisible_with_4():
    leap_year = is_LeapYear(1573)
    assert leap_year == False




