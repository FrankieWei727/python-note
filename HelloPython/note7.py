# Logical Operators: and, or, and or
is_high_incom = True
is_good_credit = True
is_criminal_record = False

if is_high_incom and is_good_credit:
    print('Eligible for loan')
else:
    print('No loan')

if is_high_incom or is_good_credit:
    print('Eligible for loan')
else:
    print('No loan')

if is_good_credit and not is_criminal_record:
    print('good')
else:
    print('bad')


# Comparison Operators: > ,>=, ==, !=
temperature = 30
if temperature >= 30:
    print('hot')
else:
    print('cold')
