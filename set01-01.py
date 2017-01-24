# cryptopals
# set 1
# convert hex to base64
import binascii
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
str_bin = binascii.unhexlify(hex_str)
#binascii.b21_base64 appends a newline to the string so slice it off
b64_str_res = binascii.b2a_base64(str_bin)[:-1]

if b64_str == b64_str_res:
    x = "Success!"
else:
    x = "Failure!"
print(x)
