#! /usr/bin/env python3

"""
Problem 59: XOR Decryption
==========================

Link: https://projecteuler.net/problem=59

Description
===========

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using 0059_cipher.txt (right click and
'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
"""

import itertools

def encrypt_decrypt(source: list[int], key: list[int]) -> list[int]:
    return [source[k] ^ key[k % len(key)] for k in range(len(source))]

def solve() -> int:
    # We assume that the string ' the ' occurs in the decrypted text.
    # This indeed yields the single, unique solution to the problem.
    with open("0059_cipher.txt", "r") as fi:
        data = fi.read()
    ciphertext = list(map(int, data.split(",")))

    candidates = []
    key_codes = range(ord("a"), ord("z") + 1)
    for xor_key in itertools.product(key_codes, repeat=3):
        possible_decryption = encrypt_decrypt(ciphertext, xor_key)
        decryption = "".join(map(chr, possible_decryption))
        if " the " in decryption:
            candidates.append(sum(possible_decryption))
    assert len(candidates) == 1
    return candidates[0]

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
