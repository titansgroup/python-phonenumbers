# Short veryfication of whether mobile numbers
# for Brazilian area codes (6x) are working
# with either 8 or 9 digits


import phonenumbers

def test_area_6_code_with_9_digits_is_valid():
    p = phonenumbers.parse("+5561998881234")
    assert phonenumbers.is_valid_number(p)


# When the transition phase for 8 digits in 6x prefix is
# over, update the resourses/PhoneNumbersMetada.xml file, ~3437
def test_area_6_code_with_8_digits_is_valid():
    p = phonenumbers.parse("+556198881234")
    assert phonenumbers.is_valid_number(p)


def test_area_4_code_with_9_digits_is_invalid():
    p = phonenumbers.parse("+5541998881234")
    assert not phonenumbers.is_valid_number(p)
