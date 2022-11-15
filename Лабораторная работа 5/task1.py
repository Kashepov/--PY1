from pprint import pprint

dict_ = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]

pprint(dict_)
# TODO решить с помощью list comprehension и распечатать его