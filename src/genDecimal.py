import random
import string

def generatePrecisionValue(p):
    precision_str = ''.join([random.choice(string.digits) for x in xrange(1,p)])
    if precision_str.startswith('0'):
        precision_str[1:] ='1'
    return precision_str
    
    
def generateScaleValue(s):
    scale_str = ''.join([random.choice(string.digits) for x in xrange(1,s)])
    return scale_str
     
    
def generateDecimalValue(p,s):
    return generatePrecisionValue(p-s+1) + '.' + generateScaleValue(s+1)
    
    
print generateDecimalValue(14,3)
