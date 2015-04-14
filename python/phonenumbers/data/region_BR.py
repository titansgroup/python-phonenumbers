"""Auto-generated file, do not edit by hand. BR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_BR = PhoneMetadata(id='BR', country_code=55, international_prefix='00(?:1[45]|2[135]|31|4[13])',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-46-9]\\d{7,10}|5\\d{8,9}', possible_number_pattern='\\d{8,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1[1-9][2-5]\\d{7}|(?:[4689][1-9]|2[12478]|3[1-578]|5[13-5]|7[13-579])[2-5]\\d{7}', possible_number_pattern='\\d{8,11}', example_number='1123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='1[1-9](?:7|9\\d)\\d{7}|(?:2[12478]|8[1-9]|9[1-9])9?[6-9]\\d{7}|(?:3[1-578]|[46][1-9]|5[13-5]|7[13-579])[6-9]\\d{7}', possible_number_pattern='\\d{10,11}', example_number='11961234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6,7}', possible_number_pattern='\\d{8,11}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='[359]00\\d{6,7}', possible_number_pattern='\\d{8,11}', example_number='300123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='[34]00\\d{5}', possible_number_pattern='\\d{8}', example_number='40041234'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='[34]00\\d{5}', possible_number_pattern='\\d{8}', example_number='40041234'),
    national_prefix='0',
    national_prefix_for_parsing='0(?:(1[245]|2[135]|31|4[13])(\\d{10,11}))?',
    national_prefix_transform_rule='\\2',
    number_format=[NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['[2-9](?:[1-9]|0[1-9])'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{5})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['9(?:[1-9]|0[1-9])'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{3,5})', format='\\1', leading_digits_pattern=['1[125689]'], national_prefix_formatting_rule='\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{5})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['(?:1[1-9]|2[12478]|9[1-9])9'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='0 $CC (\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['[1-9][1-9]'], national_prefix_formatting_rule='(\\1)', domestic_carrier_code_formatting_rule='0 $CC (\\1)'),
        NumberFormat(pattern='([34]00\\d)(\\d{4})', format='\\1-\\2', leading_digits_pattern=['[34]00']),
        NumberFormat(pattern='([3589]00)(\\d{2,3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[3589]00'], national_prefix_formatting_rule='0\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{5})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['(?:1[1-9]|2[12478]|9[1-9])9']),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['[1-9][1-9]']),
        NumberFormat(pattern='([34]00\\d)(\\d{4})', format='\\1-\\2', leading_digits_pattern=['[34]00']),
        NumberFormat(pattern='([3589]00)(\\d{2,3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[3589]00'])],
    mobile_number_portable_region=True)
