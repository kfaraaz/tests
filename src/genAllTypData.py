#!/usr/bin/python

# Generates random data and writes it to a CSV file
# Data is written in the below format to the CSV file
# ( ID(INTEGER), STATE CHAR(2), NAME VARCHAR(200), COMMENTS VARCHAR(257), dt DATE, tm TIME, tmstmp TIMESTAMP, dbl DOUBLE PRECISION )

import datetime
import random
import time
import string
import names
from random import randint


def genDate():
    rndmdate = datetime.date(
        randint(
            1940, 2015), randint(
            1, 12), randint(
                1, 28))
    date = rndmdate + datetime.timedelta(random.randint(1, 365))
    return str(date)


def genTime():
    HH = random.choice(range(1, 23))
    MM = random.choice(range(1, 59))
    SS = random.choice(range(1, 59))
    return str(HH) + ':' + str(MM) + ':' + str(SS)


def genVaryingLengthString():
    return ''.join(
        [
            random.choice(
                string.ascii_uppercase +
                string.digits +
                string.ascii_lowercase) for i in range(
                random.randint(
                    1,
                    256))])


def getRandomUSAState():
    state = random.sample(['AZ',
                           'CA',
                           'AR',
                           'OR',
                           'MI',
                           'CT',
                           'KS',
                           'UT',
                           'TX',
                           'IL',
                           'WA',
                           'OH',
                           'ID',
                           'WI',
                           'PA',
                           'MA',
                           'NY',
                           'CO'],
                          1)
    return state[0]


def writeDataToFile():
    with open('/root/datetime_data/typeall.csv', 'a') as f:
        # (ID(INTEGER), STATE CHAR(2), NAME VARCHAR(200), COMMENTS VARCHAR(257), dt DATE, tm TIME, tmstmp TIMESTAMP, dbl DOUBLE PRECISION)
        f.write(str(random.randint(1, 65000)) +
                ',' +
                str(getRandomUSAState()) +
                ',' +
                str(names.get_full_name()) +
                ',' +
                str(genVaryingLengthString()) +
                ',' +
                genDate() +
                ',' +
                genTime() +
                ',' +
                genDate() +
                ' ' +
                genTime() +
                ',' +
                str(random.uniform(1, 100)) +
                '\n')


if __name__ == "__main__":
    for i in range(1, 100):
        writeDataToFile()
