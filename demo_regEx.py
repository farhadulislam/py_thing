import re

phone_num_regEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
us_num = phone_num_regEx.search('An US number is 123-3456-0098')
print('An US phone number found : ' + us_num.group())
