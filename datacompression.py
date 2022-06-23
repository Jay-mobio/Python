import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
print(len(t))

zlib.crc32(s)
print(t)

