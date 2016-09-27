## To print a random date value.

import datetime
import random
from random import randint
somedate=datetime.date(randint(1945,2015),randint(1,12),randint(1,28))
date=somedate+datetime.timedelta(random.randint(1,365))
print date
