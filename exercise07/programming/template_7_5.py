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

# DSSS code and spreading factor
DSSS_CODE = np.array([+1, +1, +1, -1, -1, -1, +1, -1, -1, +1, -1])
SPREADING_FACTOR = len(DSSS_CODE)

# Decision boundaries. When the output of the accumulator is evaluated (at decoder),
# everything above is considered a logical HIGH (1) and everything
# below is considered a logical LOW (0).
DECISION_BOUNDARY = 0

# Original data for later checking
ORIGINAL_DATA = np.array([+1, +1, -1, -1, +1, -1, +1, -1])



def main():
    """
    Entry point
    """
    # Load received signal.
    # - The signal is after BPSK demodulation.
    # - It contains noise.
    # - Each sample is a DSSS symbol
    # - The sample stream is synchronized. The first sample is the beginning of a data symbol.
    with open("data_7_5_dsss.dat", "rb") as fh:
        signal = np.frombuffer(fh.read(), dtype=np.int16)
    
    # Number of data
    nof_data = int(len(signal) / SPREADING_FACTOR)
    
    # Allocate memory for decoded data. All decoded data goes here
    data = np.zeros((nof_data, ))
    
    # Accumulate
    for data_index in range(nof_data):
        accumulator = 0
        # TODO: Despreading and accumulate
        
        # Decoder: Evaluate accumulator
        # TODO
    
    if (data == ORIGINAL_DATA).all():
        print("Your solution is correct")
    else:
        raise AssertionError(f"Data mismatch: {data} != {ORIGINAL_DATA}")


if __name__ == "__main__":
    main()
