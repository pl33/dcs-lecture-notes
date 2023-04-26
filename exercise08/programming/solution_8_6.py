#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2023 Philipp Le
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.

import numpy as np
import matplotlib.pyplot as plt

# Input data
DATA = np.array(
    [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ]
)
    
# Decoded data with error due to double bit error at row 2
DECODED_DATA = np.array(
    [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
    ]
)
    
# Parity matrix
PARITY_MATRIX = np.array(
    [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]
).transpose()


def matmul_mod2(mat, vec):
    """
    Matrix multiplication with modulo 2
    
    :param mat: Input matrix
    :param vec: Input vector
    :return: Output = (input matrix * input vector) mod 2
    """
    mul = np.matmul(mat, vec)
    mod = np.mod(mul, 2)
    return mod.astype(np.int32)


def syndome_lookup(H, syndrome):
    """
    Find the index of the faulty bit for error correction
    :param H: Parity check matrix
    :param syndrome: Syndrome vector
    :return: Index of the faulty bit
    """
    for index, vec in enumerate(H):
        if (vec == syndrome).all():
            return index
    raise AssertionError("Null vector does not indicate a bit error")


def main():
    """
    Entry point
    """
    
    # Construct parity matrix
    G = np.concatenate([np.eye(4), PARITY_MATRIX])
    
    # Encode the data words
    coded_words = []
    for d in DATA:
        word = matmul_mod2(G, d)
        coded_words.append(word)
    coded_words = np.array(coded_words)
        
    print("Coded words:", coded_words)
        
    # Introduce some single bit errors
    coded_words[1][4] = 0
    coded_words[5][6] = 1
    coded_words[14][4] = 1
    # Introduce some souble bit errors
    coded_words[2][0] = 1
    coded_words[2][2] = 0
    
    # Construct parity check matrix
    H = np.concatenate([np.mod(-1 * PARITY_MATRIX.transpose(), 2), np.eye(3)])
    
    # Check all received words and correct them if necessary
    decoded_words = []
    for word in coded_words:
        # Calculate syndrome vector
        syndrome = matmul_mod2(word, H)
        # Check syndrome vector
        if (syndrome != 0).any():
            # Find index of faulty bit
            index = syndome_lookup(H, syndrome)
            # Flip the bit
            word[index] = (word[index] + 1) % 2
        decoded_words.append(word)
        
    # Take first 4 bits from systematic code words
    data = np.array(decoded_words)[:, 0:4]
        
    print("Decoded data:", data)
    
    # Check data
    if (data == DECODED_DATA).all():
        print("Your solution is correct")
    else:
        raise AssertionError(f"Data mismatch: {data} != {DECODED_DATA}")


if __name__ == "__main__":
    main()
