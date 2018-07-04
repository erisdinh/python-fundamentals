print("Hello World");

# every character in python has an index
# ex: i am an international -> index: i -> 0, a -> 2, m -> 3
# a string -> automatically be an array
# ex: sentence = "I am an international student at Sheridan College"
#
# string[firstCharacter : lastCharacter + 1]
#
# -> sentence[3] -> Output: 'm'
# -> sentence[8:21] -> Output: 'international'
# -> sentence[:4] -> Output: 'I am'
# -> sentence[:-3] -> Output: 'I am an international student at Sheridan Coll'

# name = "Quynh"
# name += " is 22 year olds"
# -> Output: 'Quynh is 22 year olds'
#
# sentence = "%s is 22 year olds"
# sentence%name
# -> Output: 'Quynh is 22 year olds'

# sentence = "%s is 22 year olds"
# sentence%("Hai")
# -> Output: 'Hai is 22 year olds'

# sent = "%s %s is the President of the US"
# sent%("Barrack", "Obama")
# 'Barrack Obama is the President of the US'