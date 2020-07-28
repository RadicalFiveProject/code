# 005
This problem is the first problem associated with RSA.

Note that in this problem *she* does not appear. Sorry.

## RSA
If you don't know RSA, google it.

I may write a simple explanation of it here later
(I don't have much time now).

## Problem
Your task is recover a plaintext, a large part of which is already known.
The plaintext is encrypted by 2048-bit RSA.

### How to Encrypt a Message
You have the public key (*n*, *e*).
*n* is a 2048-bit composite number consisting of
the product of two unknown primes.
This is used as the modulus.
*e* is the public exponent.

Thus, if we let *a* be a plaintext and *c* be the encryption of *a*,
then we have *c* = *a^e* mod *n*.

As a example, let's encrypt a message `Hello`.
We convert each character in a message to ASCII:
0x48, 0x65, 0x6c, 0x6c, 0x6f.
The plaintext is the concatenated number *a* =  0x48656c6c6f (310939249775 in decimal).
The encryption *c* of plaintext is *a^e* mod *n*.

Note that when using RSA in practice we must use padding to avoid
many attacks against plain RSA.

### Unknown Part
The unknown part is the last part of the plaintext.
An example of this type of plaintext includes the following:

`The password is XXXX` (XXXX is an unknown part).

### Input File
`problem.txt` has the following lines:

1. (← line number) Modulus *n*
2. Public exponent *e*
3. Known part of plaintext (string)
4. Known part of plaintext (number)
5. Ciphertext *c* (number)
6. Bit-length of the unknown part

The numbers are all decimal numbers.

## Difficulty
I don't know if there are any tools that solves this problem.
I think that if you use one it is not so Hard problem.

## History
* 2020-07-28: Publilshed
