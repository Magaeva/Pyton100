# TODO решить с помощью list comprehension и распечатать его
from pprint import *
list_comprehension = [{'bin':bin(x),'dec':x,'hex':hex(x),'oct':oct(x)} for x in range (16)]

pprint(list_comprehension)