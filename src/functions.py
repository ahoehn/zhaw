def myFunction(test):
    print('test: ', test)
    return {test: 5}


key = 'me'
x = myFunction(key)
if not x is None: print(x[key])  # if it has any return value


def checkCC(cc_nr="no credit card nr"):
    print("start checking", cc_nr)
    if cc_nr is not None:
        cc_parts = cc_nr.split(' ')
        if len(cc_parts) != 4:
            return False
        cc_sum = 0
        for part in cc_parts:
            for nr in part:
                try:
                    cc_sum += int(nr)
                except ValueError:
                    return False
        check = cc_sum % 10
        print('Checksum is: ', check)
        return check == 0


print(checkCC())
print(checkCC("9384 3495 3297 0123"))
print(checkCC("9384 3495 3297 0121"))


# return function
def outer(test):
    def inner():
        return test + 1

    return inner()


print(outer(5))

import my_module as my
my.my_function('test')
