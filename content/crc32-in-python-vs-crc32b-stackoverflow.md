Title: CRC32 In Python (vs CRC32b) - stackoverflow
Date: 2022-01-18 21:50:18+00:00
Author: FoxMaSk 
Tags: php, python, crc32
Category: link
Status: published





# CRC32 In Python (vs CRC32b) - stackoverflow

[CRC32 In Python (vs CRC32b) - stackoverflow](https://stackoverflow.com/questions/50842434/crc32-in-python-vs-crc32b/50843127#50843127)


I am trying to generate some crc32 hashes, but it seems like `zlib` and
`binascii` use the crc32b algorithm even though their respective
functions are simply `zlib.crc32` and `binascii.crc32`. Are there any
other python resources for hash generation that I can try?
Interestingly, I have previously found that R\&#39;s \&#39;digest\&#39; package also
implements crc32b with no mention of crc32.

Some examples of what I me...
