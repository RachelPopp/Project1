# So, we have this variable we pull from our dataset
variable = b'Hav\xc3\xad\xc5\x99ov'

# and then we know how to decode it into a unicode character, this part works just fine
var = variable.decode('UTF-8')

print('Hey, code got to here just fine!')

# But trying to print it... dies
print(var)
# Expected output:
# Havířov

# Actual output:
# File "4_test_analysis.py", line 9, in <module>
#    print(var)
#  File "D:\Anaconda\envs\PythonData\lib\encodings\cp1252.py", line 19, in encode
#    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
# UnicodeEncodeError: 'charmap' codec can't encode character '\u0159' in position 4: character maps to <undefined>

# Note that this exact code works on some people's computers, but not mine (Daniel's)??