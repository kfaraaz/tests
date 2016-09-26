## To print a random date value.

import datetime
import random
somedate=datetime.date(1980,01,01)
date=somedate+datetime.timedelta(random.randint(1,365))
print date
