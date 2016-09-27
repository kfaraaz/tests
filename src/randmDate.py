## To print random date values.

import datetime
import random
from random import randint
for i in range(1,50):
    somedate=datetime.date(randint(1945,2015),randint(1,12),randint(1,28))
    date=somedate+datetime.timedelta(random.randint(1,365))
    print date
