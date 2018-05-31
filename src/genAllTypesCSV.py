# BIGINT,VARCHAR(65535),CHAR(2),DATE,TIME,DOUBLE PRECISION, DECIMAL(10,3),
# BOOLEAN

# col_bigint, col_vrchar, col_char, col_date, col_time, col_double, col_decimal, col_boolean

import datetime
import random
import time
import string
import names
from random import randint


# col_bigint
def genRandomBigInt():
    """ Returns a random big integer value. """
    return str(randint(1, 2147483648))


# col_date
def genDate():
    """ Returns a random date value in YYYY-MM-DD format
    Note that the day value will always be <= 28
    """
    yr = randint(1940, 2015)
    month = randint(1, 12)
    day = randint(1, 28)
    rndmdate = datetime.date(yr, month, day)
    date = rndmdate + datetime.timedelta(random.randint(1, 365))
    return str(date)


# col_time
def genTime():
    """ Returns a random time value in HH:MM:SS format """
    HH = random.choice(range(1, 23))
    MM = random.choice(range(1, 59))
    SS = random.choice(range(1, 59))
    return str(HH) + ':' + str(MM) + ':' + str(SS)


# col_varchar_65535
def genVaryingLengthString():
    """ Returns a random variable length string of alpha numeric characters
    length of the random string could range from 1 - 256 characters
    """
    return ''.join(
        [
            random.choice(
                string.ascii_uppercase +
                string.digits +
                string.ascii_lowercase) for i in range(
                random.randint(
                    1,
                    255))])


# col_char_2
def genRandomUSAState():
    """ Returns a random USA state """
    state = random.sample(['AL', 'AK', 'DE', 'FL', 'GA', 'HI', 'AZ',
                           'CA', 'AR', 'OR', 'IN', 'IA', 'MI', 'CT',
                           'KS', 'KY', 'UT', 'LA', 'TX', 'TN', 'IL',
                           'WA', 'VA', 'WV', 'OH', 'NV', 'NH', 'NJ',
                           'NM', 'NC', 'ND', 'NE', 'ID', 'OK', 'SC',
                           'SD', 'WI', 'WY', 'PA', 'RI', 'MA', 'MN',
                           'MO', 'MT', 'NY', 'CO'],
                          1)
    return str(state[0])


# col_boolean
def genBoolean():
    """ Returns a random boolean values, either true or false."""
    return random.choice([str('true'), str('false')])


# col_name
def genName():
    """ Returns a random name """
    return str(names.get_full_name())


# col_double
def genDouble():
    """ Returns a random floating point number """
    return str(random.uniform(1, 65000))


def generatePrecisionValue(p):
    precision_str = ''.join([random.choice(string.digits)
                             for x in xrange(1, p)])
    if precision_str.startswith('0'):
        precision_str = '1' + precision_str[1:]
    return precision_str


def generateScaleValue(s):
    scale_str = ''.join([random.choice(string.digits) for x in xrange(1, s)])
    return scale_str


# col_decimal
def generateDecimalValue(p, s):
    return str(generatePrecisionValue(p - s + 1) + '.' + generateScaleValue(s + 1))


def writeDataToFile():
    with open('/Users/maprit/data4HashJoin.csv', 'a') as f:
        f.write(genRandomBigInt() +
                ',' +
                genRandomUSAState() +
                ',' +
                genName() +
                ',' +
                genVaryingLengthString() +
                ',' +
                generateDecimalValue(14, 3) +
                ',' +
                genDate() +
                ',' +
                genTime() +
                ',' +
                genDouble() +
                ',' +
                genBoolean() +
                '\n')


if __name__ == "__main__":
    for i in xrange(1, 100):
        writeDataToFile()
