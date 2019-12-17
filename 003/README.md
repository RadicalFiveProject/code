# 003
There are no tricks in 003 as seen in the previous problems.

## One-Time Pad
The one-time pad (OTP) is secure *as long as it is correctly used*.

There are many cases where OTP becomes insecure.

I take up one of them in this problem, which is very simplified.

For example, encrypting two messages with the same key breaks its secrecy,
because the key is *reused*.

If you know why, you can skip this problem.

At first I was going to make a more difficult problem, but I realized I didn't
have the knowledge and skills enough to make one.
精進します。

## Problem
Let's assume that you have a pair of plaintext `known_plain` (Pa) and
ciphertext `known_cipher` (Ca) encrypted by OTP
(Vernam cipher with truly random key),
and have found that another ciphertext `unknown_cipher` (Cb) was also
encrypted with the same key.

In other words, the cipher is not OTP.

Your task is to recover the plaintext Pb of Cb.

`known_plain` is just a text file,
and the two ciphertexts are simply written by `fwrite(text, 1, text_len, fp)`.

### Note
You can't recover all content of Pb unless you know the key.

But this is an answer to the problem.

### More difficult problem
Cryptanalysis of Lorenz cipher is related to this problem
although the cipher is not OTP.

It's Very Hard (I don't understand it at all).

## Vernam cipher and RC4
A Vernam cipher is a stream cipher.

If the cipher uses truly random keystream only once, it is OTP.

In the problem, however, I used RC4, which is a Vernam cipher variant
that uses a pseudorandom keystream.

Don't ask me why.

You can regard RC4 as a Vernam cipher in the problem.

You don't have to think about the details of RC4 such as its
key-scheduling algorithm and pseudo-random generation algorithm.

### Note
RC4 is now considered as a unsafe stream cipher because multiple
vulnerabilities have been discovered in it.

Using RC4 is dangerous in itself (で合ってるよね？),
so don't use RC4 for security purpose.

## History
* 2019-12-17: Published
