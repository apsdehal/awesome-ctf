xortool.py
====================

A tool to do some xor analysis:

  - guess the key length (based on count of equal chars)
  - guess the key (base on knowledge of most frequent char)

Usage
---------------------

! *python3 is not supported, use python 2.x*

```
  xortool [-h|--help] [OPTIONS] [&lt;filename&gt;]
Options:
  -l,--key-length       length of the key (integer)
  -c,--char             most possible char (one char or hex code)
  -m,--max-keylen=32    maximum key length to probe (integer)
  -x,--hex              input is hex-encoded str
  -b,--brute-chars      brute-force all possible characters
  -o,--brute-printable  same as -b but will only use printable
                        characters for keys
```

Example
---------------------

```bash
# xor is xortool/xortool-xor
tests $ xor -f /bin/ls -s "secret_key" > binary_xored

tests $ xortool binary_xored
The most probable key lengths:
   2:   5.0%
   5:   8.7%
   8:   4.9%
  10:   15.4%
  12:   4.8%
  15:   8.5%
  18:   4.8%
  20:   15.1%
  25:   8.4%
  30:   14.9%
Key-length can be 5*n
Most possible char is needed to guess the key!

# 00 is the most frequent byte in binaries
tests $ xortool binary_xored -l 10 -c 00
...
1 possible key(s) of length 10:
secret_key

# decrypted ciphertexts are placed in ./xortool_out/Number_&lt;key repr&gt;
# ( have no better idea )
tests $ md5sum xortool_out/0_secret_key /bin/ls
29942e290876703169e1b614d0b4340a  xortool_out/0_secret_key
29942e290876703169e1b614d0b4340a  /bin/ls
```

The most common use is to pass just the encrypted file and the most frequent character (usually 00 for binaries and 20 for text files) - length will be automatically chosen:

```bash
tests $ xortool tool_xored -c 20
The most probable key lengths:
   2:   5.6%
   5:   7.8%
   8:   6.0%
  10:   11.7%
  12:   5.6%
  15:   7.6%
  20:   19.8%
  25:   7.8%
  28:   5.7%
  30:   11.4%
Key-length can be 5*n
1 possible key(s) of length 20:
an0ther s3cret \xdd key
```

Here, the key is longer then default 32 limit:

```bash
tests $ xortool ls_xored -c 00 -m 64
The most probable key lengths:
   3:   3.3%
   6:   3.3%
   9:   3.3%
  11:   7.0%
  22:   6.9%
  24:   3.3%
  27:   3.2%
  33:   18.4%
  44:   6.8%
  55:   6.7%
Key-length can be 3*n
1 possible key(s) of length 33:
really long s3cr3t k3y... PADDING
```

So, if automated decryption fails, you can calibrate:

- (`-m`) max length to try longer keys
- (`-l`) selected length to see some interesting keys
- (`-c`) the most frequent char to produce right plaintext

Author: hellman ( hellman1908@gmail.com )

License: MIT License (opensource.org/licenses/MIT)
