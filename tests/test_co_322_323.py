# coding: utf-8

# Short veryfication of whether mobile numbers
# for Colombian ranges 322 700 0000 - 322 999 9999
#                      323 200 0000 - 323 599 9999
# (#COMPS 184 - letter from COMCEL S.A. 2016-04-26)
# with either 8 or 9 digits

import phonenumbers
import pytest


def makenum(text):
    return phonenumbers.parse(text.replace(' ', ''))

@pytest.mark.parametrize('n', (
    '+57 322 700 0000',
    '+57 322 855 5555',
    '+57 322 999 9999',
    )
)
def test_colombia_322(n):
    p = makenum(n)
    assert phonenumbers.is_valid_number(p)


@pytest.mark.parametrize('n', (
    '+57 323 200 0000',
    '+57 323 200 0001',
    '+57 323 300 0000',
    '+57 323 400 0000',
    '+57 323 455 5555',
    '+57 323 599 9999',
    )
)
def test_colombia_323(n):
    p = makenum(n)
    assert phonenumbers.is_valid_number(p)


@pytest.mark.parametrize('n', (
    '+57 323 600 0000',
    )
)
def test_colombia_offrange_323(n):
    p = makenum(n)
    assert not phonenumbers.is_valid_number(p)


