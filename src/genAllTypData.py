## Generates random data and writes to a CSV file
## Data is written in this format to file
## ( ID(INTEGER), STATE CHAR(2), NAME VARCHAR(200), COMMENTS VARCHAR(257), dt DATE, tm TIME, tmstmp TIMESTAMP, dbl DOUBLE PRECISION ) 

import datetime
import random
from random import randint

def genDate():
    rndmdate=datetime.date(randint(1940,2015),randint(1,12),randint(1,28))
    date=rndmdate+datetime.timedelta(random.randint(1,365))
    return str(date)


import time,random
def genTime():
    HH = random.choice(range(1,23))
    MM = random.choice(range(1,59))
    SS = random.choice(range(1,59))
    return str(HH)+':'+str(MM)+':'+str(SS)


def genVaryingLengthString():
    import random,string
    return ''.join([random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(random.randint(1,256))])
    
    
import random,string,names
def writeDataToFile() :
    f = open('/root/datetime_data/typeall.csv', 'a')
    # (ID(INTEGER), STATE CHAR(2), NAME VARCHAR(200), COMMENTS VARCHAR(257), dt DATE, tm TIME, tmstmp TIMESTAMP, dbl DOUBLE PRECISION)
    state = random.sample(['AZ', 'CA','AR','OR','MI','CT','KS','UT','TX','IL','WA','OH','ID','WI','PA','MA','NY','CO'],1)
    f.write(str(random.randint(1,65000)) + ',' + str(state[0])+','+ str(names.get_full_name())+','+str(genVaryingLengthString())+','+genDate()+','+genTime()+','+genDate()+' '+genTime()+','+str(random.uniform(1,100))+'\n')
    f.flush()
    f.close()
        
for i in range(1,100):
    writeDataToFile()
