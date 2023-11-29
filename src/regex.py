import re
str = 'phone: 079-777-1122'
# Usage: re.search(<regex_pattern>, <string_to_be_searched>)
match = re.search(r'\d{3}-\d{3}-\d{4}', str)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group())
else:
    print('did not find')
