from ctypes import *

# sa = cdll.LoadLibrary("./sa_demo_CID_level2.dll")
# seed = b"67 09 55 97 9D BE"
# key = "27 0A 25 5A D3 78"
sa = CDLL("./sa_demo_CID_level2.dll")
seed = c_char_p(bytes([0x55, 0x97, 0x9D, 0xBE]))
seed_size = c_short(4)
security_level = c_int(9)
Variant = c_char_p("".encode())
KeyArray = c_char_p(b"")
KeyArraySize = byref(c_short(4))
out = sa.ZLGKey(seed, seed_size, security_level, Variant, KeyArray, KeyArraySize)
key = KeyArray.value
for i in key:
    print('%02X' % i)

