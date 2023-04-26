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

AMPLITUDE = 128
DATA = np.array(
    [
        [+1, +1, -1, -1, +1, -1, +1, -1],
        [-1, +1, -1, -1, +1, +1, -1, -1],
        [+1, -1, -1, +1, +1, -1, -1, +1],
        [-1, -1, -1, -1, +1, +1, +1, +1],
    ]
)
    
NOF_CARRIERS = 16

ROTATION = 130 * np.pi / 180



def main():
    """
    Entry point
    """
    
    frames = []
    for frame_index in range(DATA.shape[0]):
        carriers = np.ones((NOF_CARRIERS, ), dtype=np.complex128)
        carriers[4:8] = DATA[frame_index, 0:4]
        carriers[8:12] = np.flip(DATA[frame_index, 4:8])
        carriers *= AMPLITUDE * np.exp(1j * ROTATION)
        
        iq = np.fft.ifft(carriers)
        frames.append(iq)
        
    signal = np.concatenate(frames)
    adc = np.array(
        [
            np.real(signal),
            np.imag(signal),
        ],
        dtype=np.int16
    ).transpose().reshape((-1,))
    
    with open("data_7_6_ofdm.dat", "wb") as fh:
        data = adc.astype(np.int16).tobytes()
        fh.write(data)
    

if __name__ == "__main__":
    main()
