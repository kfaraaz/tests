#!/usr/bin/python

# Generates random data and writes it to a CSV file in the below format.
# ( ID(INTEGER), STATE CHAR(2), NAME VARCHAR(200), COMMENTS VARCHAR(257), dt DATE, tm TIME, tmstmp TIMESTAMP, dbl DOUBLE PRECISION, durn INTERVAL, bln BOOLEAN )

# Pre-requisites
# Python names module is required to generate random names.
# To install names with pip, sudo pip install names

# To run this script, run the below command
# python genAllTypData.py

import datetime
import random
import time
import string
import names
from random import randint


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


def genTime():
    """ Returns a random time value in HH:MM:SS format """
    HH = random.choice(range(1, 23))
    MM = random.choice(range(1, 59))
    SS = random.choice(range(1, 59))
    return str(HH) + ':' + str(MM) + ':' + str(SS)


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
                    256))])


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


def genDuration():
    """ Returns a random duration value in ISO 8601 format """
    return 'P' + str(randint(1, 30)) + \
        'Y' + str(randint(1, 12)) + \
        'M' + str(randint(1, 31)) + \
        'D' + \
        'T' + str(randint(1, 12)) + \
        'H' + str(randint(1, 59)) + \
        'M' + str(randint(1, 59)) + \
        'S'


def genBoolean():
    """ Returns a random boolean values, either true or false."""
    return random.choice([str('true'), str('false')])


def genName():
    """ Returns a random name """
    return str(names.get_full_name())


def genFloat():
    """ Returns a random floating point number """
    return str(random.uniform(1, 100))


def genTimestamp():
    """ Returns a timestamp value """
    return genDate() + ' ' + genTime()


def writeDataToFile():
    with open('/root/datetime_data/typeall.csv', 'a') as f:
        f.write(str(random.randint(1, 65000)) +
                ',' +
                genRandomUSAState() +
                ',' +
                genName() +
                ',' +
                genVaryingLengthString() +
                ',' +
                genDate() +
                ',' +
                genTime() +
                ',' +
                genTimestamp() +
                ',' +
                genFloat() +
                ',' +
                str(genDuration()) +
                ',' +
                genBoolean() +
                '\n')


if __name__ == "__main__":
    for i in xrange(1, 100):
        writeDataToFile()
